from flask import Flask, render_template, request, jsonify, session, send_file
from werkzeug.utils import secure_filename
import os
import pandas as pd
from graph import agent
import uuid
from datetime import datetime
import json
from pdf_generator import generate_analysis_pdf, generate_simple_pdf

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-in-production'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create uploads directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Store analysis results in memory (use database in production)
analysis_results = {}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    task = request.form.get('task', 'Analyze the dataset and recommend complete preprocessing and EDA.')
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not file.filename.endswith('.csv'):
        return jsonify({'error': 'Only CSV files are supported'}), 400
    
    try:
        # Save file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Generate analysis ID
        analysis_id = str(uuid.uuid4())
        
        # Store in session
        session['current_analysis'] = analysis_id
        
        # Store initial status
        analysis_results[analysis_id] = {
            'status': 'processing',
            'filename': filename,
            'filepath': filepath,
            'task': task,
            'started_at': datetime.now().isoformat(),
            'result': None
        }
        
        return jsonify({
            'success': True,
            'analysis_id': analysis_id,
            'filename': filename
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/analyze/<analysis_id>', methods=['POST'])
def analyze(analysis_id):
    if analysis_id not in analysis_results:
        return jsonify({'error': 'Analysis not found'}), 404
    
    try:
        analysis_info = analysis_results[analysis_id]
        
        # Prepare initial state
        initial_state = {
            "task": analysis_info['task'],
            "dataset_path": analysis_info['filepath'],
            "dataset_summary": {},
            "analysis": {},
            "plan": [],
            "result": "",
            "success": False,
            "feedback": "",
            "retry_count": 0,
        }
        
        # Run the agent with timeout handling
        try:
            response = agent.invoke(initial_state)
        except Exception as agent_error:
            print(f"Agent error: {str(agent_error)}")
            # Return partial results if agent fails
            response = {
                'result': f'Analysis partially completed. Error: {str(agent_error)}',
                'success': False,
                'feedback': 'Agent encountered an error during analysis',
                'dataset_summary': {}
            }
        
        # Clean response - remove non-serializable objects
        clean_response = {
            'result': str(response.get('result', '')),
            'success': response.get('success', False),
            'feedback': str(response.get('feedback', '')),
            'dataset_summary': str(response.get('dataset_summary', {}))[:500],  # Limit size
        }
        
        # Update results
        analysis_results[analysis_id].update({
            'status': 'completed',
            'result': clean_response['result'],
            'success': clean_response['success'],
            'feedback': clean_response['feedback'],
            'dataset_summary': clean_response['dataset_summary'],
            'completed_at': datetime.now().isoformat()
        })
        
        return jsonify({
            'success': True,
            'analysis_id': analysis_id,
            'result': clean_response['result'],
            'agent_success': clean_response['success'],
            'feedback': clean_response['feedback']
        })
    
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(f"Error in analysis: {error_details}")
        
        analysis_results[analysis_id]['status'] = 'failed'
        analysis_results[analysis_id]['error'] = str(e)
        
        # Return error response instead of 500
        return jsonify({
            'success': False,
            'error': str(e),
            'analysis_id': analysis_id,
            'result': f'Analysis failed: {str(e)}',
            'agent_success': False,
            'feedback': 'Error occurred during analysis'
        }), 200  # Changed to 200 to prevent fetch error


@app.route('/status/<analysis_id>')
def get_status(analysis_id):
    if analysis_id not in analysis_results:
        return jsonify({'error': 'Analysis not found'}), 404
    
    return jsonify(analysis_results[analysis_id])


@app.route('/history')
def history():
    # Return all analysis results
    history_list = []
    for aid, result in analysis_results.items():
        history_list.append({
            'id': aid,
            'filename': result['filename'],
            'status': result['status'],
            'started_at': result['started_at'],
            'task': result['task']
        })
    return jsonify(history_list)


@app.route('/download/<analysis_id>')
def download_pdf(analysis_id):
    """Generate and download PDF report"""
    if analysis_id not in analysis_results:
        return jsonify({'error': 'Analysis not found'}), 404
    
    try:
        analysis_data = analysis_results[analysis_id]
        
        if analysis_data['status'] != 'completed':
            return jsonify({'error': 'Analysis not completed yet'}), 400
        
        # Create reports directory if it doesn't exist
        reports_dir = 'reports'
        os.makedirs(reports_dir, exist_ok=True)
        
        # Generate PDF
        filename = f"analysis_report_{analysis_id[:8]}.pdf"
        output_path = os.path.join(reports_dir, filename)
        
        pdf_data = {
            'filename': analysis_data['filename'],
            'task': analysis_data['task'],
            'result': analysis_data.get('result', ''),
            'success': analysis_data.get('success', False),
            'feedback': analysis_data.get('feedback', ''),
            'started_at': analysis_data.get('started_at', ''),
            'completed_at': analysis_data.get('completed_at', '')
        }
        
        generate_analysis_pdf(pdf_data, output_path)
        
        return send_file(
            output_path,
            as_attachment=True,
            download_name=f"AI_Analysis_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
            mimetype='application/pdf'
        )
    
    except Exception as e:
        import traceback
        print(f"Error generating PDF: {traceback.format_exc()}")
        return jsonify({'error': str(e)}), 500


@app.route('/download-qr/<analysis_id>')
def download_qr(analysis_id):
    """Generate QR code image for the analysis"""
    if analysis_id not in analysis_results:
        return jsonify({'error': 'Analysis not found'}), 404
    
    try:
        from pdf_generator import generate_qr_code
        
        analysis_data = analysis_results[analysis_id]
        qr_text = f"Autonomous AI Data Scientist Report\nDate: {datetime.now().strftime('%Y-%m-%d')}\nDataset: {analysis_data.get('filename', 'N/A')}\nID: {analysis_id}"
        
        qr_buffer = generate_qr_code(qr_text)
        
        return send_file(
            qr_buffer,
            mimetype='image/png',
            as_attachment=True,
            download_name=f"analysis_qr_{analysis_id[:8]}.png"
        )
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    # Run without auto-reload to prevent connection issues during analysis
    app.run(debug=True, port=5000, use_reloader=False)

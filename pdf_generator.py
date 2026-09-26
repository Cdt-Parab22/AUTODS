from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
import qrcode
from io import BytesIO
from datetime import datetime
import os


def generate_qr_code(data):
    """Generate QR code image"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save to BytesIO
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    
    return buffer


def generate_analysis_pdf(analysis_data, output_path):
    """
    Generate a professional PDF report of the analysis
    
    Args:
        analysis_data: Dictionary containing analysis results
        output_path: Path where PDF will be saved
    """
    
    # Create the PDF document
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=18,
    )
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#4f46e5'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#6366f1'),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=11,
        alignment=TA_JUSTIFY,
        spaceAfter=12,
        leading=14
    )
    
    code_style = ParagraphStyle(
        'CustomCode',
        parent=styles['Code'],
        fontSize=9,
        leftIndent=20,
        textColor=colors.HexColor('#1e293b'),
        backColor=colors.HexColor('#f1f5f9'),
        borderPadding=10,
        spaceAfter=12
    )
    
    # Title
    title = Paragraph("🤖 Autonomous AI Data Scientist", title_style)
    elements.append(title)
    
    subtitle = Paragraph("Analysis Report", styles['Heading3'])
    subtitle.alignment = TA_CENTER
    elements.append(subtitle)
    elements.append(Spacer(1, 0.3*inch))
    
    # Info section
    info_data = [
        ['Report Date:', datetime.now().strftime('%B %d, %Y at %I:%M %p')],
        ['Dataset:', analysis_data.get('filename', 'N/A')],
        ['Analysis Task:', analysis_data.get('task', 'N/A')],
        ['Status:', '✅ Success' if analysis_data.get('success') else '⚠️ Completed with Feedback']
    ]
    
    info_table = Table(info_data, colWidths=[2*inch, 4*inch])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f1f5f9')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e2e8f0'))
    ]))
    elements.append(info_table)
    elements.append(Spacer(1, 0.3*inch))
    
    # Analysis Results
    elements.append(Paragraph("Analysis Results", heading_style))
    elements.append(Spacer(1, 0.1*inch))
    
    result_text = analysis_data.get('result', 'No results available')
    
    # Parse and format the result
    sections = result_text.split('\n\n')
    
    for section in sections:
        if section.strip():
            # Check if it's a finding, recommendation, or reason
            if 'Finding:' in section:
                parts = section.split('Finding:', 1)
                if len(parts) > 1:
                    elements.append(Paragraph("<b>🔍 Finding:</b>", body_style))
                    elements.append(Paragraph(parts[1].strip(), body_style))
            elif 'Recommendation:' in section:
                parts = section.split('Recommendation:', 1)
                if len(parts) > 1:
                    elements.append(Paragraph("<b>💡 Recommendation:</b>", body_style))
                    elements.append(Paragraph(parts[1].strip(), body_style))
            elif 'Reason:' in section:
                parts = section.split('Reason:', 1)
                if len(parts) > 1:
                    elements.append(Paragraph("<b>📝 Reason:</b>", body_style))
                    elements.append(Paragraph(parts[1].strip(), body_style))
                    elements.append(Spacer(1, 0.2*inch))
            else:
                elements.append(Paragraph(section.strip(), body_style))
    
    # Feedback section if available
    if analysis_data.get('feedback'):
        elements.append(Spacer(1, 0.3*inch))
        elements.append(Paragraph("Reviewer Feedback", heading_style))
        elements.append(Paragraph(analysis_data['feedback'], body_style))
    
    # Add QR code for sharing
    elements.append(Spacer(1, 0.5*inch))
    elements.append(PageBreak())
    
    # QR Code page
    elements.append(Paragraph("Share This Report", heading_style))
    elements.append(Spacer(1, 0.2*inch))
    
    qr_text = f"Autonomous AI Data Scientist Report\nDate: {datetime.now().strftime('%Y-%m-%d')}\nDataset: {analysis_data.get('filename', 'N/A')}"
    qr_buffer = generate_qr_code(qr_text)
    
    # Save QR code temporarily
    qr_img_path = output_path.replace('.pdf', '_qr.png')
    with open(qr_img_path, 'wb') as f:
        f.write(qr_buffer.read())
    
    qr_image = Image(qr_img_path, width=2*inch, height=2*inch)
    qr_image.hAlign = 'CENTER'
    elements.append(qr_image)
    elements.append(Spacer(1, 0.2*inch))
    
    qr_caption = Paragraph("Scan to view analysis details", styles['Normal'])
    qr_caption.alignment = TA_CENTER
    elements.append(qr_caption)
    
    # Footer
    elements.append(Spacer(1, 0.5*inch))
    footer = Paragraph(
        "Generated by Autonomous AI Data Scientist<br/>"
        "Powered by LangGraph, LangChain, and Groq<br/>"
        f"© {datetime.now().year}",
        styles['Normal']
    )
    footer.alignment = TA_CENTER
    elements.append(footer)
    
    # Build PDF
    doc.build(elements)
    
    # Clean up QR code image
    try:
        os.remove(qr_img_path)
    except:
        pass
    
    return output_path


def generate_simple_pdf(analysis_data, output_path):
    """Generate a simpler, faster PDF version"""
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    # Title
    elements.append(Paragraph("Autonomous AI Data Scientist - Analysis Report", styles['Title']))
    elements.append(Spacer(1, 0.3*inch))
    
    # Info
    elements.append(Paragraph(f"<b>Date:</b> {datetime.now().strftime('%Y-%m-%d %H:%M')}", styles['Normal']))
    elements.append(Paragraph(f"<b>Dataset:</b> {analysis_data.get('filename', 'N/A')}", styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))
    
    # Results
    elements.append(Paragraph("<b>Analysis Results:</b>", styles['Heading2']))
    result_text = analysis_data.get('result', 'No results available')
    elements.append(Paragraph(result_text.replace('\n', '<br/>'), styles['Normal']))
    
    doc.build(elements)
    return output_path

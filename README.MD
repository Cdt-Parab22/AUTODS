# 🤖 Autonomous AI Data Scientist - Web UI Edition

A fully autonomous AI-powered data analysis system with a modern web interface, parallax effects, and professional PDF report generation.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green)
![LangGraph](https://img.shields.io/badge/LangGraph-Latest-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

### 🤖 **Multi-Agent AI System**
- **Dataset Loader Agent** - Automatically loads and validates CSV files
- **Analysis Agent** - Detects patterns, correlations, missing values, outliers
- **Planner Agent** - Creates comprehensive preprocessing strategies
- **Executor Agent** - Implements preprocessing and feature engineering
- **Reviewer Agent** - Validates results and provides feedback

### 🎨 **Modern Web Interface**
- **Beautiful UI** - Dark theme with gradient animations
- **Parallax Effects** - Mouse-tracking and scroll-based parallax layers
- **Drag & Drop Upload** - Easy CSV file upload
- **Real-Time Progress** - Visual progress tracking for each agent
- **Responsive Design** - Works on desktop, tablet, and mobile

### 📄 **Professional Reports**
- **PDF Generation** - ReportLab-based professional reports
- **QR Code Integration** - Shareable QR codes for each analysis
- **Smart Formatting** - Automatic parsing of AI analysis results
- **Download Options** - PDF report and QR code downloads

### ⚡ **Performance**
- **Powered by Groq** - Ultra-fast LPU inference
- **Hardware Accelerated** - 60fps smooth animations
- **Optimized CSS** - Efficient rendering and transitions
- **Error Handling** - Robust error recovery and user feedback

## 🚀 Quick Start

### **Prerequisites**
- Python 3.8 or higher
- pip (Python package manager)
- Groq API key ([Get one here](https://console.groq.com))

### **Installation**

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR-USERNAME/Autonomous-AI-Data-Scientist.git
   cd Autonomous-AI-Data-Scientist
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file
   echo GROQ_API_KEY=your_groq_api_key_here > .env
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   Navigate to: http://localhost:5000

## 📖 Usage

### **Web Interface**

1. **Upload Dataset**
   - Drag & drop a CSV file or click to browse
   - Optionally customize the analysis task

2. **Watch AI Agents Work**
   - Real-time progress visualization
   - See each agent's contribution

3. **Download Results**
   - Professional PDF report
   - QR code for easy sharing

### **Command Line (Original)**

```bash
python main.py
```

Follow the prompts to:
- Load dataset
- Perform analysis
- Get recommendations

## 🏗️ Project Structure

```
Autonomous-AI-Data-Scientist/
├── 📄 app.py                    # Flask web server
├── 📄 main.py                   # CLI version
├── 📄 graph.py                  # LangGraph agent workflow
├── 📄 agents.py                 # Agent definitions
├── 📄 state.py                  # State management
├── 📄 models.py                 # LLM models configuration
├── 📄 prompts.py                # Agent prompts
├── 📄 analysis_agent.py         # Analysis agent logic
├── 📄 pdf_generator.py          # PDF generation
├── 📁 templates/
│   └── 📄 index.html           # Main HTML template
├── 📁 static/
│   ├── 📄 style.css            # Styles with parallax effects
│   └── 📄 script.js            # Interactive JavaScript
├── 📁 tools/                    # Data analysis tools
│   ├── 📄 loader.py
│   ├── 📄 statistics.py
│   ├── 📄 correlation.py
│   ├── 📄 missing_values.py
│   ├── 📄 outliers.py
│   ├── 📄 duplicates.py
│   ├── 📄 feature_types.py
│   ├── 📄 feature_engineering.py
│   ├── 📄 preprocessing.py
│   ├── 📄 visualisation.py
│   └── 📄 model_reccomendation.py
├── 📁 data/                     # Sample datasets
├── 📁 uploads/                  # User uploaded files (not committed)
├── 📁 reports/                  # Generated reports (not committed)
└── 📄 requirements.txt          # Python dependencies
```

## 🛠️ Technology Stack

### **Backend**
- **Flask** - Lightweight Python web framework
- **LangGraph** - Multi-agent orchestration
- **LangChain** - LLM integration framework
- **Groq** - Ultra-fast AI inference (qwen3.8-27b model)
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **ReportLab** - PDF generation
- **qrcode** - QR code generation

### **Frontend**
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with animations
- **JavaScript (ES6+)** - Interactive functionality
- **No frameworks** - Vanilla JS for optimal performance

### **AI Models**
- **Primary**: qwen/qwen3.8-27b (Groq)
- **Fallback options**: Various LLaMA and Gemma models

## 🔧 Configuration

### **Environment Variables**
Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### **Model Configuration**
Edit `models.py` to change the AI model:

```python
chat = ChatGroq(
    model="qwen/qwen3.8-27b",  # Change model here
    temperature=0.0,
    max_retries=2,
)
```

### **Server Configuration**
Edit `app.py` to change server settings:

```python
app.run(
    debug=True,           # Set to False for production
    port=5000,           # Change port if needed
    use_reloader=False   # Prevents restart during analysis
)
```

## 📊 Supported Features

### **Data Analysis**
- ✅ Missing value detection
- ✅ Outlier identification
- ✅ Correlation analysis
- ✅ Duplicate detection
- ✅ Feature type classification
- ✅ Statistical summaries
- ✅ Distribution analysis

### **Preprocessing**
- ✅ Missing value imputation
- ✅ Outlier handling
- ✅ Feature scaling
- ✅ Encoding categorical variables
- ✅ Feature engineering suggestions

### **Recommendations**
- ✅ Model selection guidance
- ✅ Preprocessing strategies
- ✅ Feature engineering ideas
- ✅ Hyperparameter suggestions

## 🎨 UI Customization

### **Colors**
Edit `static/style.css`:

```css
:root {
    --primary: #6366f1;      /* Main brand color */
    --secondary: #8b5cf6;    /* Secondary accent */
    --accent: #06b6d4;       /* Highlight color */
    --bg-dark: #0f172a;      /* Background */
    --bg-darker: #020617;    /* Darker background */
}
```

### **Animations**
Adjust animation speeds in `static/style.css`:

```css
animation: float 3s ease-in-out infinite;  /* Change duration */
```

## 🐛 Troubleshooting

### **Port Already in Use**
```bash
# Kill process on port 5000 (Windows)
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Or change port in app.py
app.run(port=5001)
```

### **Groq API Errors**
- Check your API key is correct in `.env`
- Verify you have API credits
- Try a different model if rate limited

### **File Upload Fails**
- Ensure file is valid CSV format
- Check file size is under 16MB
- Verify uploads/ directory exists and is writable

### **"Failed to Fetch" Error**
- Server is set to not auto-reload during analysis
- If you see this, refresh the page and try again
- Check server logs for specific errors

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Original Project**: Based on [OmShelar2004/Autonomous-AI-Data-Scientist](https://github.com/OmShelar2004/Autonomous-AI-Data-Scientist)
- **LangGraph**: For multi-agent orchestration framework
- **Groq**: For ultra-fast AI inference
- **Flask**: For lightweight web framework

## 📧 Contact

**Pranav Parab**
- Email: pranavparab.2004.22@gmail.com
- GitHub: [@YOUR-GITHUB-USERNAME](https://github.com/YOUR-GITHUB-USERNAME)

## 🎯 Roadmap

- [ ] Real-time streaming of agent outputs via WebSocket
- [ ] Dark/Light theme toggle
- [ ] Analysis history with search and filtering
- [ ] Export to multiple formats (JSON, Excel, etc.)
- [ ] Visualization charts in the web UI
- [ ] User authentication and saved sessions
- [ ] API endpoints for programmatic access
- [ ] Docker containerization
- [ ] Cloud deployment guides (AWS, Azure, GCP)

## 📸 Screenshots

### Landing Page
Modern hero section with parallax effects and floating agent cards

### Upload Interface
Drag & drop file upload with real-time validation

### Analysis Progress
Live progress tracking showing each agent's work

### Results Display
Professional results with formatted output and download options

---

Made with ❤️ by Pranav Parab | Powered by LangGraph & Groq

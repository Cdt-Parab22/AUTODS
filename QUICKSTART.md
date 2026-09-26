# 🚀 Quick Start Guide

## Your Autonomous AI Data Scientist is Ready!

The web UI with beautiful parallax effects is now running at:

### 🌐 **http://localhost:5000**

---

## ✨ What's Included

### 🎨 **Modern Web UI with Parallax Effects**
- Mouse-tracking parallax background
- Smooth scroll animations
- Floating agent visualization cards
- Animated gradients and stars
- Glass-morphism design
- Responsive for all devices

### 🤖 **Multi-Agent System**
1. **Dataset Loader** - Loads and summarizes your CSV
2. **Analysis Agent** - Performs initial exploration
3. **Planner Agent** - Creates execution strategy
4. **Executor Agent** - Runs analysis steps
5. **Reviewer Agent** - Validates and provides feedback

---

## 📋 How to Use

### Step 1: Open Your Browser
Navigate to: **http://localhost:5000**

### Step 2: Upload Your Dataset
- Click "Start Analysis" or scroll down
- **Drag & drop** your CSV file OR click "Choose File"
- Optionally customize the analysis task
- Click "Start Analysis"

### Step 3: Watch the Magic
- See real-time progress through each agent
- Watch the status indicators update
- Get comprehensive analysis results

---

## 🎯 Try It Out

### Sample Dataset
The Titanic dataset is already in `data/Titanic.csv`

### Example Tasks You Can Try

**Basic EDA:**
```
Analyze the dataset and recommend complete preprocessing and EDA.
```

**Feature Focus:**
```
Analyze feature correlations and recommend feature engineering strategies.
```

**Missing Data:**
```
Analyze missing values and recommend imputation strategies.
```

**Model Prep:**
```
Prepare the dataset for machine learning and recommend suitable algorithms.
```

---

## 🎨 UI Features to Explore

### Parallax Effects
- **Move your mouse** around to see background layers shift
- **Scroll down** to see sections move at different speeds
- Watch the **floating agent cards** animate

### Interactive Elements
- Hover over feature cards
- Drag and drop files
- See progress animations
- View formatted results

---

## 🛠️ Project Structure

```
Autonomous-AI-Data-Scientist/
│
├── app.py                    # Flask web server ⭐ NEW
├── templates/
│   └── index.html           # UI template ⭐ NEW
├── static/
│   ├── style.css            # Parallax styles ⭐ NEW
│   └── script.js            # Interactions ⭐ NEW
│
├── main.py                  # Original CLI version
├── graph.py                 # Agent workflow
├── agents.py                # Agent definitions
├── models.py                # Pydantic models
├── state.py                 # State management
├── prompts.py               # LLM prompts
│
├── tools/                   # Analysis tools
│   ├── loader.py
│   ├── missing_values.py
│   ├── duplicates.py
│   ├── statistics.py
│   └── ...
│
├── data/
│   └── Titanic.csv         # Sample dataset
│
├── .env                     # API keys
└── requirements.txt         # Dependencies
```

---

## 💡 Pro Tips

### 1. Best Browser Experience
- Use **Chrome** or **Edge** for best performance
- Enable hardware acceleration
- Use full screen for immersive parallax

### 2. File Uploads
- CSV files only
- Max size: 16MB
- Files saved to `uploads/` folder

### 3. Customization
- Edit colors in `static/style.css`
- Adjust parallax speed in `static/script.js`
- Modify animations as needed

### 4. API Access
The Flask server also provides REST API:
- `POST /upload` - Upload file
- `POST /analyze/<id>` - Start analysis
- `GET /status/<id>` - Check status

---

## 🔄 Running Both Versions

### Web UI (Current)
```bash
python app.py
# Opens on http://localhost:5000
```

### CLI Version (Original)
```bash
python main.py
# Runs in terminal
```

Both versions use the same AI agents!

---

## ⚙️ Configuration

### Change Port
Edit `app.py`:
```python
app.run(debug=True, port=5001)  # Use different port
```

### Update API Key
Edit `.env`:
```
GROQ_API_KEY=your_key_here
```

### Adjust Model
Edit `agents.py`:
```python
llm = ChatGroq(
    model="qwen/qwen3.8-27b",  # Change model
    temperature=0
)
```

---

## 🐛 Troubleshooting

### Server Won't Start
```bash
# Kill existing Python processes
Get-Process python | Stop-Process

# Restart server
python app.py
```

### Port Already in Use
```bash
# Use different port
python app.py --port 5001
```

### File Upload Fails
- Check file is CSV format
- Ensure size < 16MB
- Verify `uploads/` directory exists

### Parallax Laggy
- Close other browser tabs
- Enable hardware acceleration
- Reduce animation complexity

---

## 📚 Learn More

- **UI_README.md** - Detailed UI documentation
- **README.MD** - Project overview
- **Code comments** - Inline documentation

---

## 🎉 Enjoy!

Your autonomous AI data scientist is ready to analyze datasets with a beautiful, modern interface featuring smooth parallax effects!

### Key Highlights:
- ✅ Fully autonomous multi-agent system
- ✅ Beautiful parallax UI
- ✅ Drag & drop file upload
- ✅ Real-time progress tracking
- ✅ Comprehensive analysis results
- ✅ Self-correcting with retry logic
- ✅ Production-ready architecture

**Happy analyzing! 🚀**

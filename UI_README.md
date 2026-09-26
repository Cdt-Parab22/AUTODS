# 🤖 Autonomous AI Data Scientist - Modern Web UI

**A production-ready, perfectly centered web interface** with enhanced parallax effects, PDF report generation, and professional design.

## ✨ Enhanced Features

### 🎨 **Perfect Centered UI**
- ✅ **Complete Visual Alignment** - Fixed all text shifting and alignment issues
- ✅ **Flexbox-Based Layout** - Responsive centering across all screen sizes  
- ✅ **Professional Typography** - Inter font with consistent spacing and hierarchy

### 🎭 **Advanced Parallax Effects**
- ✅ **Hardware-Accelerated Performance** - Uses `translate3d()` for 60fps smooth animations
- ✅ **Mouse-Tracking Parallax** - Interactive background layers responding to mouse movement
- ✅ **Scroll Parallax** - Depth effects on scroll with throttled performance optimization
- ✅ **Starry Background** - Animated star field with CSS animations

### 📄 **Professional PDF Reports**
- ✅ **ReportLab Integration** - Professional PDF generation with custom styling
- ✅ **QR Code Generation** - Dynamic QR codes for easy report sharing
- ✅ **Smart Formatting** - Automatic parsing of AI analysis results
- ✅ **Direct Downloads** - PDF and QR code download buttons

### 🤖 **Multi-Agent Workflow**
- ✅ **Real-Time Progress Tracking** - Animated progress steps for each agent
- ✅ **Agent Status Visualization** - Visual indicators for Loader, Analyzer, Planner, Executor, Reviewer
- ✅ **Live Status Updates** - Emoji-based visual feedback system
- ✅ **Analysis History** - Track all previous analyses

### 🎯 UI Components
1. **Hero Section** - Eye-catching landing with gradient text and animations
2. **Features Section** - Showcase of multi-agent capabilities
3. **Upload Section** - Interactive file upload with drag-drop
4. **Results Section** - Real-time analysis display with progress tracking
5. **Footer** - Professional footer with links

## 📁 File Structure

```
Autonomous-AI-Data-Scientist/
├── app.py                 # Flask web server
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   ├── style.css         # Styles with parallax effects
│   └── script.js         # Interactive JavaScript
├── uploads/              # Uploaded CSV files (created automatically)
├── main.py              # Original CLI version
├── graph.py             # LangGraph agent workflow
├── agents.py            # Agent definitions
└── requirements.txt     # Python dependencies
```

## 🚀 How to Run

### 1. Start the Flask Server

```bash
python app.py
```

The server will start on `http://localhost:5000`

### 2. Open in Browser

Navigate to: **http://localhost:5000**

### 3. Upload and Analyze

1. Scroll down to the "Start Your Analysis" section
2. Drag and drop a CSV file or click "Choose File"
3. Optionally customize the analysis task
4. Click "Start Analysis"
5. Watch the AI agents work in real-time!

## 🎨 Parallax Effects

The UI features multiple parallax layers:

### Mouse Parallax
- Move your mouse around to see the background layers shift
- Smooth lerp animation for natural movement
- Multiple layers with different speeds

### Scroll Parallax
- Sections move at different speeds while scrolling
- Creates depth and visual interest
- Controlled via `data-speed` attributes

### Floating Animations
- Agent cards float independently
- Staggered animation delays
- Continuous loop for dynamic feel

## 🛠️ Customization

### Change Colors

Edit `static/style.css` variables:

```css
:root {
    --primary: #6366f1;      /* Main brand color */
    --secondary: #8b5cf6;    /* Secondary accent */
    --accent: #06b6d4;       /* Highlight color */
    --bg-dark: #0f172a;      /* Background */
    --bg-darker: #020617;    /* Darker background */
}
```

### Adjust Parallax Speed

In `static/script.js`:

```javascript
// Mouse parallax sensitivity
currentX += (mouseX * 100 - currentX) * 0.05; // Change 0.05 for speed

// Scroll parallax
const speed = section.dataset.speed || 0.5; // Default speed
```

### Modify Animations

Edit animation durations in `static/style.css`:

```css
@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}
/* Duration: 3s in animation property */
animation: float 3s ease-in-out infinite;
```

## 📊 API Endpoints

### POST `/upload`
Upload a CSV file for analysis

**Request:**
- `file`: CSV file (multipart/form-data)
- `task`: Analysis task description (optional)

**Response:**
```json
{
    "success": true,
    "analysis_id": "uuid",
    "filename": "data.csv"
}
```

### POST `/analyze/<analysis_id>`
Start analysis on uploaded file

**Response:**
```json
{
    "success": true,
    "analysis_id": "uuid",
    "result": "Analysis findings...",
    "agent_success": true,
    "feedback": "Reviewer feedback..."
}
```

### GET `/status/<analysis_id>`
Get current analysis status

**Response:**
```json
{
    "status": "completed",
    "filename": "data.csv",
    "result": "Analysis results...",
    "success": true
}
```

## 🎯 Browser Compatibility

- ✅ Chrome/Edge (Recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Mobile browsers

## 💡 Tips

1. **Best Experience**: Use Chrome or Edge for optimal performance
2. **File Size**: Keep CSV files under 16MB for best results
3. **Smooth Scrolling**: Works best with a mouse/trackpad
4. **Dark Mode**: UI is designed for dark theme lovers
5. **Responsiveness**: Try on mobile for a different experience!

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Change port in app.py
app.run(debug=True, port=5001)  # Use different port
```

### File Upload Fails
- Check file is actually CSV format
- Ensure file size < 16MB
- Check uploads/ directory permissions

### Parallax Not Smooth
- Reduce number of animated elements
- Check browser hardware acceleration
- Lower animation frame rate

## 🎨 Screenshots

### Hero Section
- Gradient animated title
- Floating agent cards
- Interactive parallax background

### Upload Interface
- Drag and drop zone
- File information display
- Custom task input

### Results Display
- Step-by-step progress
- Formatted analysis output
- Status indicators

## 📝 Notes

- The UI is a **separate layer** from the core AI logic
- Original `main.py` still works for CLI usage
- All analysis logic remains in `graph.py` and `agents.py`
- Flask serves as a thin API layer between UI and agents

## 🚀 Future Enhancements

- [ ] Real-time streaming of agent outputs
- [ ] WebSocket support for live updates
- [ ] Download results as PDF
- [ ] Visualization charts
- [ ] Dark/Light theme toggle
- [ ] Analysis history with search
- [ ] User authentication
- [ ] Multiple file comparison

---

Enjoy the beautiful parallax UI! 🎨✨

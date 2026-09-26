// Parallax Effect - Optimized
let mouseX = 0;
let mouseY = 0;
let currentX = 0;
let currentY = 0;
let rafId = null;

document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX / window.innerWidth - 0.5;
    mouseY = e.clientY / window.innerHeight - 0.5;
});

function animateParallax() {
    currentX += (mouseX * 100 - currentX) * 0.05;
    currentY += (mouseY * 100 - currentY) * 0.05;
    
    const layer1 = document.querySelector('.layer-1');
    const layer2 = document.querySelector('.layer-2');
    const layer3 = document.querySelector('.layer-3');
    
    if (layer1) layer1.style.transform = `translate3d(${currentX * 0.5}px, ${currentY * 0.5}px, 0)`;
    if (layer2) layer2.style.transform = `translate3d(${currentX * 0.3}px, ${currentY * 0.3}px, 0)`;
    if (layer3) layer3.style.transform = `translate3d(${currentX * 0.7}px, ${currentY * 0.7}px, 0)`;
    
    rafId = requestAnimationFrame(animateParallax);
}

// Start animation
animateParallax();

// Stop animation when tab is not visible (performance optimization)
document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
        if (rafId) cancelAnimationFrame(rafId);
    } else {
        animateParallax();
    }
});

// Scroll Parallax - Optimized with throttling
let scrollTimeout;
let ticking = false;

function updateScrollParallax() {
    const scrolled = window.pageYOffset;
    const parallaxSections = document.querySelectorAll('.parallax-section');
    
    parallaxSections.forEach(section => {
        const speed = parseFloat(section.dataset.speed) || 0.5;
        const yPos = -(scrolled * speed);
        section.style.transform = `translate3d(0, ${yPos}px, 0)`;
    });
    
    ticking = false;
}

window.addEventListener('scroll', () => {
    if (!ticking) {
        window.requestAnimationFrame(updateScrollParallax);
        ticking = true;
    }
}, { passive: true });

// Smooth Scroll
function scrollToUpload() {
    document.getElementById('upload').scrollIntoView({ behavior: 'smooth' });
}

function showFeatures() {
    document.getElementById('features').scrollIntoView({ behavior: 'smooth' });
}

// File Upload
let selectedFile = null;
let analysisId = null;

const fileInput = document.getElementById('fileInput');
const uploadBox = document.getElementById('uploadBox');
const analyzeBtn = document.getElementById('analyzeBtn');

fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (file) {
        handleFileSelect(file);
    }
});

// Drag and Drop
uploadBox.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadBox.classList.add('drag-over');
});

uploadBox.addEventListener('dragleave', () => {
    uploadBox.classList.remove('drag-over');
});

uploadBox.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadBox.classList.remove('drag-over');
    
    const file = e.dataTransfer.files[0];
    if (file && file.name.endsWith('.csv')) {
        handleFileSelect(file);
    } else {
        showNotification('Please upload a CSV file', 'error');
    }
});

function handleFileSelect(file) {
    selectedFile = file;
    
    // Update UI
    uploadBox.querySelector('h3').textContent = file.name;
    uploadBox.querySelector('p').textContent = `${(file.size / 1024).toFixed(2)} KB`;
    analyzeBtn.disabled = false;
    
    showNotification(`File "${file.name}" selected successfully!`, 'success');
}

// Start Analysis
async function startAnalysis() {
    if (!selectedFile) {
        showNotification('Please select a file first', 'error');
        return;
    }
    
    const task = document.getElementById('taskInput').value;
    
    // Disable button and show loader
    analyzeBtn.disabled = true;
    const btnText = analyzeBtn.querySelector('span');
    const btnLoader = analyzeBtn.querySelector('.btn-loader');
    btnText.style.display = 'none';
    btnLoader.style.display = 'block';
    
    try {
        // Upload file
        const formData = new FormData();
        formData.append('file', selectedFile);
        formData.append('task', task);
        
        showNotification('Uploading file...', 'info');
        
        const uploadResponse = await fetch('/upload', {
            method: 'POST',
            body: formData
        });
        
        if (!uploadResponse.ok) {
            const error = await uploadResponse.json();
            throw new Error(error.error || 'Upload failed');
        }
        
        const uploadResult = await uploadResponse.json();
        analysisId = uploadResult.analysis_id;
        
        showNotification('File uploaded! Starting analysis...', 'success');
        
        // Show results section
        document.getElementById('results').style.display = 'block';
        document.getElementById('results').scrollIntoView({ behavior: 'smooth' });
        
        // Reset progress
        resetProgress();
        updateStatus('processing', 'AI agents analyzing your dataset...');
        
        // Simulate progress while analysis runs
        const progressPromise = simulateProgress();
        
        // Start analysis with better error handling
        let analyzeResult;
        try {
            const analyzeResponse = await fetch(`/analyze/${analysisId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            
            // Wait for progress animation to complete
            await progressPromise;
            
            if (!analyzeResponse.ok) {
                throw new Error(`Server returned ${analyzeResponse.status}`);
            }
            
            analyzeResult = await analyzeResponse.json();
            
            // Check if analysis succeeded
            if (!analyzeResult.success && analyzeResult.error) {
                throw new Error(analyzeResult.error);
            }
            
        } catch (fetchError) {
            console.error('Fetch error:', fetchError);
            throw new Error(`Analysis request failed: ${fetchError.message}. The server may have restarted. Please try again.`);
        }
        
        // Display results
        displayResults(analyzeResult);
        
        if (analyzeResult.agent_success) {
            updateStatus('success', 'Analysis completed successfully! ✅');
            showNotification('Analysis completed successfully!', 'success');
        } else {
            updateStatus('warning', 'Analysis completed with feedback');
            showNotification('Analysis completed with reviewer feedback', 'warning');
        }
        
    } catch (error) {
        console.error('Error:', error);
        updateStatus('error', `Error: ${error.message}`);
        showNotification(`Error: ${error.message}`, 'error');
        
        // Reset all steps to show error
        const steps = document.querySelectorAll('.step');
        steps.forEach(step => {
            step.classList.remove('active', 'completed');
        });
    } finally {
        // Re-enable button
        analyzeBtn.disabled = false;
        btnText.style.display = 'inline';
        btnLoader.style.display = 'none';
    }
}

// Progress Simulation
async function simulateProgress() {
    const steps = ['loader', 'analysis', 'planning', 'execution', 'review'];
    
    for (let i = 0; i < steps.length; i++) {
        await sleep(800);
        markStepComplete(steps[i]);
        if (i < steps.length - 1) {
            markStepActive(steps[i + 1]);
        }
    }
}

function resetProgress() {
    const steps = document.querySelectorAll('.step');
    steps.forEach(step => {
        step.classList.remove('active', 'completed');
    });
    
    // Mark first step as active
    if (steps.length > 0) {
        steps[0].classList.add('active');
    }
}

function markStepActive(stepName) {
    const step = document.querySelector(`[data-step="${stepName}"]`);
    if (step) {
        step.classList.add('active');
    }
}

function markStepComplete(stepName) {
    const step = document.querySelector(`[data-step="${stepName}"]`);
    if (step) {
        step.classList.remove('active');
        step.classList.add('completed');
    }
}

function updateStatus(type, message) {
    const statusIcon = document.getElementById('statusIcon');
    const statusText = document.getElementById('statusText');
    
    const icons = {
        processing: '⏳',
        success: '✅',
        error: '❌',
        warning: '⚠️'
    };
    
    statusIcon.textContent = icons[type] || '⏳';
    statusText.textContent = message;
}

function displayResults(result) {
    const resultContent = document.getElementById('resultContent');
    const downloadButtons = document.getElementById('downloadButtons');
    
    let formattedResult = result.result;
    
    // Format the result with better readability
    formattedResult = formattedResult
        .replace(/Finding:/g, '\n🔍 Finding:')
        .replace(/Recommendation:/g, '\n💡 Recommendation:')
        .replace(/Reason:/g, '\n📝 Reason:')
        .replace(/\n\n/g, '\n')
        .trim();
    
    resultContent.textContent = formattedResult;
    
    // Add feedback if available
    if (result.feedback) {
        resultContent.textContent += '\n\n' + '─'.repeat(80) + '\n';
        resultContent.textContent += '\n📋 Reviewer Feedback:\n' + result.feedback;
    }
    
    // Show download buttons
    if (downloadButtons) {
        downloadButtons.style.display = 'flex';
    }
}

// Download PDF
function downloadPDF() {
    if (!analysisId) {
        showNotification('No analysis available to download', 'error');
        return;
    }
    
    showNotification('Generating PDF report...', 'info');
    
    // Create a download link
    const downloadUrl = `/download/${analysisId}`;
    const link = document.createElement('a');
    link.href = downloadUrl;
    link.download = `AI_Analysis_Report_${new Date().toISOString().split('T')[0]}.pdf`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    
    setTimeout(() => {
        showNotification('PDF downloaded successfully!', 'success');
    }, 1000);
}

// Download QR Code
function downloadQR() {
    if (!analysisId) {
        showNotification('No analysis available to download', 'error');
        return;
    }
    
    showNotification('Generating QR code...', 'info');
    
    // Create a download link
    const downloadUrl = `/download-qr/${analysisId}`;
    const link = document.createElement('a');
    link.href = downloadUrl;
    link.download = `analysis_qr_${new Date().toISOString().split('T')[0]}.png`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    
    setTimeout(() => {
        showNotification('QR code downloaded successfully!', 'success');
    }, 500);
}

// Notification System - Optimized
const notificationQueue = [];
let isShowingNotification = false;

function showNotification(message, type = 'info') {
    // Add to queue
    notificationQueue.push({ message, type });
    
    // Process queue if not already showing
    if (!isShowingNotification) {
        processNotificationQueue();
    }
}

function processNotificationQueue() {
    if (notificationQueue.length === 0) {
        isShowingNotification = false;
        return;
    }
    
    isShowingNotification = true;
    const { message, type } = notificationQueue.shift();
    
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    
    // Style notification
    Object.assign(notification.style, {
        position: 'fixed',
        top: '20px',
        right: '20px',
        padding: '1rem 1.5rem',
        background: type === 'success' ? 'var(--success)' : 
                    type === 'error' ? 'var(--error)' : 
                    type === 'warning' ? 'var(--warning)' : 
                    'var(--primary)',
        color: 'white',
        borderRadius: '12px',
        boxShadow: '0 8px 32px rgba(0, 0, 0, 0.3)',
        zIndex: '10000',
        animation: 'slideInRight 0.3s ease-out',
        fontWeight: '600',
        maxWidth: '400px',
        wordWrap: 'break-word'
    });
    
    document.body.appendChild(notification);
    
    // Remove after 3 seconds and process next
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease-out';
        setTimeout(() => {
            notification.remove();
            processNotificationQueue();
        }, 300);
    }, 3000);
}

// Add animation keyframes
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            transform: translateX(400px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Utility
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Intersection Observer for scroll animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe feature cards
document.addEventListener('DOMContentLoaded', () => {
    const featureCards = document.querySelectorAll('.feature-card');
    featureCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = `all 0.6s ease ${index * 0.1}s`;
        observer.observe(card);
    });
});

console.log('🤖 Autonomous AI Data Scientist - Ready!');

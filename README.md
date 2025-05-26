# 🧠 AI-Based Mood & Emotion Tracker

[![Streamlit](https://img.shields.io/badge/Streamlit-Online-brightgreen)](https://moodtracker20-kx8geglx7f75uhuhxnnph2.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)](https://moodtracker20-kx8geglx7f75uhuhxnnph2.streamlit.app/)

🚀 **Track and analyze your emotions with AI-powered sentiment analysis.**  
🔗 **Live Demo:** [Try the App Here](https://moodtracker20-kx8geglx7f75uhuhxnnph2.streamlit.app/)

---

## 📖 Overview
This AI-powered **Mood & Emotion Tracker** helps users log their thoughts, analyzes their emotional state, and visualizes mood trends over time. The app utilizes **Google's Gemini AI** for sentiment analysis and provides insightful feedback for emotional well-being.

### ✨ **Features**
- 🤖 **AI-Powered Sentiment Analysis** of user inputs.
- 📝 **Mood Logging** with CSV storage for historical tracking.
- 📈 **Mood Trends Visualization** with Matplotlib.
- 📆 **Weekly Mood Reports** summarizing emotional trends.
- 📥 **Downloadable Reports** for personal tracking.

---

## 🛠 Tech Stack
- **Frontend & UI:** Streamlit
- **AI Processing:** Google's Gemini API
- **Data Handling:** Pandas, CSV
- **Visualization:** Matplotlib
- **Deployment:** Streamlit Cloud

---

## 🔧 Setup & Installation

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/MohammadHR10/Mood_tracker_2.0.git
cd Mood_tracker_2.0
```
### 2️⃣ **Set Up a Virtual Environment (Optional)**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ **Install Dependencies**
```
pip install -r requirements.txt
```

### 4️⃣ **Run the Application**
```
streamlit run mood_tracker.py
```

## 🔄 CI/CD Workflow

This project uses GitHub Actions for continuous integration:

### 📋 **CI Pipeline**
- Runs automatically on every push and pull request
- Performs linting with flake8
- Runs unit tests with pytest
- Generates test coverage reports

### 🏷️ **PR Labeling**
Pull requests are automatically labeled based on the files changed:
- `documentation`: Changes to README and other markdown files
- `tests`: Changes to test files
- `dependencies`: Updates to requirements.txt or other dependency files
- `ui`: Changes to the Streamlit UI components
- `workflow`: Updates to GitHub Actions or CI configuration
- `configuration`: Changes to configuration files
- `bugfix`: Bug fixes
- `feature`: New features

### 🧪 **Running Tests Locally**
```bash
# Install test dependencies
pip install pytest pytest-cov flake8

# Run tests
pytest tests/
```

## 🌐 Live Demo
Try the [AI Mood Tracker here](https://moodtracker20-kx8geglx7f75uhuhxnnph2.streamlit.app/)! 🚀

---

## 📜 License
This project is licensed under the MIT License.





# Mood_tracker_2.0
AI-Based Mood & Emotion Tracker
🚀 Track and analyze your emotions with AI-powered sentiment analysis.

🔗 Live Demo: Try the App Here

📖 Overview
This AI-powered Mood & Emotion Tracker helps users log their thoughts, analyzes their emotional state, and visualizes mood trends over time. The app leverages Google's Gemini AI for sentiment analysis and provides insightful feedback for emotional well-being.

Core Features
✨ AI-Powered Sentiment Analysis of user inputs.
📊 Mood Logging with CSV storage for historical tracking.
📈 Mood Trends Visualization with Matplotlib.
📆 Weekly Mood Reports summarizing emotional trends.
📥 Downloadable Reports for personal tracking.
🛠 Tech Stack
Frontend & UI: Streamlit
AI Processing: Google's Gemini API
Data Handling: Pandas, CSV
Visualization: Matplotlib
Deployment: Streamlit Cloud
🔧 Setup & Installation
Clone the Repository
bash
git clone https://github.com/MohammadHR10/Mood_tracker_2.0.git
cd Mood_tracker_2.0
Set Up a Virtual Environment (Optional)
bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
Install Dependencies
bash
pip install -r requirements.txt
Set Up API Key for Gemini AI
Create a .env file in the root directory and add:

plaintext
GEMINI_API_KEY=your_google_gemini_api_key
Run the Application
bash
streamlit run mood_tracker.py
🚀 Deploying on Streamlit Cloud
Push the Code to GitHub
Ensure your repository is updated:

bash
git add .
git commit -m "Initial commit"
git push origin main
Deploy on Streamlit Cloud
Go to Streamlit Cloud.
Select "New App" → Choose your GitHub repository.
Set the .env variables in "Advanced Settings".
Click Deploy.
✅ Your app is now live at: Mood Tracker Web App

📈 How It Works
Enter Your Thoughts → The AI analyzes your mood.
AI Provides Insights → Get real-time emotional feedback.
Weekly Report → Track emotional patterns over time.
Mood Trends Visualization → Understand your emotional journey.
Download Your Mood History → Keep track of your mental health.
🏆 Future Enhancements
🧠 Advanced NLP Insights for deeper sentiment analysis.
🔄 User Authentication to save personal data securely.
📅 Daily Reminders to encourage mood tracking.
💡 Contributions & suggestions are welcome!

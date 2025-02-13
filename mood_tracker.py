import streamlit as st
import google.generativeai as genai
import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
os.environ['ABSL_LOGGING_FLAG'] = 'off'
load_dotenv()

# Set up Gemini API key
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# File path for mood historyimport tempfile
import tempfile
# Create a temporary file path
FILE_PATH = os.path.join(tempfile.gettempdir(), "mood_history.csv")



# Use a temporary directory for Streamlit Cloud
if "STREAMLIT" in os.environ:
    FILE_PATH = "/tmp/mood_history.csv"  # Streamlit Cloud allows writing here
else:
    FILE_PATH = "mood_history.csv"  # Local path for development



# Initialize CSV with headers if it doesn't exist

def initialize_csv():
    """Ensure the CSV file exists before writing to it."""
    if not os.path.exists(FILE_PATH):
        df = pd.DataFrame(columns=['Date', 'Input', 'Mood', 'Detailed Analysis'])
        df.to_csv(FILE_PATH, index=False)


def log_mood(user_input, detailed_analysis):
    """Logs mood entries into a CSV file."""
    simple_mood = "Neutral"
    if "negative" in detailed_analysis.lower():
        simple_mood = "Negative"
    elif "positive" in detailed_analysis.lower():
        simple_mood = "Positive"

    cleaned_analysis = detailed_analysis.replace("\n", " ").replace('"', "'")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = pd.DataFrame([[date, user_input, simple_mood, cleaned_analysis]],
                             columns=['Date', 'Input', 'Mood', 'Detailed Analysis'])

    if not os.path.exists(FILE_PATH):
        log_entry.to_csv(FILE_PATH, mode='w', header=True, index=False)
    else:
        log_entry.to_csv(FILE_PATH, mode='a', header=False, index=False)


# Define weekly report function
def generate_weekly_report():
    """Generates an automated progress report based on mood history."""
    file_path = "/Users/mohammad/Downloads/Anum_Agent/mood_history.csv"

    if not os.path.exists(file_path):
        return "No mood history available yet."

    try:
        df = pd.read_csv(file_path)
        if df.empty:
            return "No mood history available yet."
        
        if 'Date' not in df.columns or 'Mood' not in df.columns:
            return "CSV file is missing required columns."
        
        df['Date'] = pd.to_datetime(df['Date'])
        last_week = df[df['Date'] >= (datetime.now() - pd.Timedelta(days=7))]
        summary = last_week['Mood'].value_counts().to_dict()
        return summary
    except Exception as e:
        return f"Error reading CSV: {e}"


# Define plot function for mood trends
def plot_mood_trends():
    """Plots mood trends over time with a professional design."""
    if not os.path.exists(FILE_PATH) or os.stat(FILE_PATH).st_size == 0:
        st.warning("⚠️ No mood history available yet.")
        return

    # Load and prepare data
    df = pd.read_csv(FILE_PATH)
    
    if 'Date' not in df.columns or 'Mood' not in df.columns:
        st.error("The CSV file is missing required columns ('Date' and 'Mood').")
        return

    df['Date'] = pd.to_datetime(df['Date']).dt.date
    mood_counts = df.groupby(['Date', 'Mood']).size().unstack(fill_value=0)

    # Reindex to ensure all dates are present
    date_range = pd.date_range(start=df['Date'].min(), end=df['Date'].max())
    mood_counts = mood_counts.reindex(date_range, fill_value=0).reset_index()
    mood_counts = mood_counts.rename(columns={'index': 'Date'})

    # Plotting
    fig, ax = plt.subplots(figsize=(12, 6))
    for mood in mood_counts.columns[1:]:
        ax.plot(
            mood_counts['Date'],
            mood_counts[mood],
            label=mood,
            marker='o',
            linestyle='-',
            linewidth=2,
        )

    # Enhancements
    ax.set_title("📈 Mood Trends Over Time", fontsize=16, fontweight='bold')
    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Mood Frequency", fontsize=12)
    ax.grid(visible=True, linestyle='--', alpha=0.7)
    ax.legend(title="Mood", fontsize=10, loc="upper left")
    plt.xticks(rotation=45, fontsize=10)
    plt.tight_layout()

    # Display plot in Streamlit
    st.pyplot(fig)




# Streamlit UI
st.title("🧠 AI-Based Mood & Emotion Tracker")
st.write("Analyze your mood using AI-powered sentiment analysis.")

# Ensure the CSV is initialized
initialize_csv()

# User input for text analysis
user_text = st.text_area("Enter your thoughts or feelings:")

if st.button("Analyze Mood"):
    if user_text:
        # Generate detailed analysis using Gemini
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(
            "You are a psychologist's AI assistant. Analyze the mood of the following text "
            "and provide a clear and insightful response:\n"
            f"{user_text}"
        )
        
        detailed_analysis = response.text
        st.success(f"**AI Analysis:** {detailed_analysis}")
        
        # Log mood into CSV
        log_mood(user_text, detailed_analysis)
    else:
        st.warning("⚠️ Please enter some text.")

# Display Weekly Mood Report
st.subheader("📊 Weekly Mood Report")
weekly_report = generate_weekly_report()
if isinstance(weekly_report, dict):
    st.json(weekly_report)
else:
    st.warning(weekly_report)

# Display Mood Trends Plot
st.subheader("📈 Mood Trends Over Time")
plot_mood_trends()

# Download Mood History
st.subheader("📥 Download Mood Report")
if os.path.exists(FILE_PATH) and os.stat(FILE_PATH).st_size > 0:
    with open(FILE_PATH, "rb") as file:
        st.download_button(label="Download CSV", data=file, file_name="mood_history.csv", mime="text/csv")
else:
    st.warning("⚠️ No mood history available yet.")

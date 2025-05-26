import unittest
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
from unittest.mock import patch, MagicMock

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Create mock objects for all needed modules
streamlit_mock = MagicMock()
matplotlib_mock = MagicMock()
genai_mock = MagicMock()
dotenv_mock = MagicMock()

# Configure the genai mock
genai_mock.configure = MagicMock()
genai_model_mock = MagicMock()
genai_model_mock.generate_content.return_value.text = "Test analysis"
genai_mock.GenerativeModel.return_value = genai_model_mock

# Apply mocks to all the modules
sys.modules['streamlit'] = streamlit_mock
sys.modules['matplotlib.pyplot'] = matplotlib_mock
sys.modules['google.generativeai'] = genai_mock
sys.modules['dotenv'] = dotenv_mock

# Set environment variable
os.environ['GEMINI_API_KEY'] = 'test_api_key'

# Import the app after mocking
import mood_tracker

# Patch plt.figure and plt.savefig in the module after import
mood_tracker.plt.figure = MagicMock(return_value=MagicMock())
mood_tracker.plt.savefig = MagicMock()

# Also patch streamlit's pyplot to avoid errors
mood_tracker.st.pyplot = MagicMock()

class TestMoodTracker(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.test_file = "test_mood_history.csv"
        mood_tracker.FILE_PATH = self.test_file
        
        # Initialize the CSV file
        mood_tracker.initialize_csv()
    
    def tearDown(self):
        # Remove test file after tests
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_initialize_csv(self):
        """Test that initialize_csv creates a new CSV file with correct headers"""
        # File should exist after initialize_csv
        self.assertTrue(os.path.exists(self.test_file))
        
        # Check headers
        df = pd.read_csv(self.test_file)
        expected_columns = ['Date', 'Input', 'Mood', 'Detailed Analysis']
        self.assertListEqual(list(df.columns), expected_columns)
    
    def test_log_mood_positive(self):
        """Test that log_mood correctly adds a positive entry to the CSV"""
        test_input = "I am feeling happy"
        test_analysis = "This text shows positive sentiment"
        
        # Log a mood
        mood_tracker.log_mood(test_input, test_analysis)
        
        # Verify entry was added
        df = pd.read_csv(self.test_file)
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]['Input'], test_input)
        self.assertEqual(df.iloc[0]['Mood'], "Positive")
        self.assertEqual(df.iloc[0]['Detailed Analysis'], test_analysis)
    
    def test_log_mood_negative(self):
        """Test that log_mood correctly adds a negative entry to the CSV"""
        test_input = "I am feeling sad"
        test_analysis = "This text shows negative sentiment"
        
        # Log a mood
        mood_tracker.log_mood(test_input, test_analysis)
        
        # Verify entry was added
        df = pd.read_csv(self.test_file)
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]['Input'], test_input)
        self.assertEqual(df.iloc[0]['Mood'], "Negative")
        self.assertEqual(df.iloc[0]['Detailed Analysis'], test_analysis)
    
    def test_log_mood_neutral(self):
        """Test that log_mood correctly adds a neutral entry to the CSV"""
        test_input = "I am feeling okay"
        test_analysis = "This text shows neutral sentiment"
        
        # Log a mood
        mood_tracker.log_mood(test_input, test_analysis)
        
        # Verify entry was added
        df = pd.read_csv(self.test_file)
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]['Input'], test_input)
        self.assertEqual(df.iloc[0]['Mood'], "Neutral")
        self.assertEqual(df.iloc[0]['Detailed Analysis'], test_analysis)

if __name__ == '__main__':
    unittest.main() 
AI Assistant Using Gemini API
Overview
This AI Assistant is a Flask-based web application that leverages Google's Gemini API to answer user questions in natural language. It also supports text-to-speech functionality for verbal responses. The project demonstrates the integration of generative AI with a web-based user interface.

Features
User-friendly interface for asking questions via a web browser.
Integration with Google Gemini API for natural language processing and AI-generated answers.
Text-to-speech functionality using the gTTS library.
Local deployment with Flask for testing and debugging.
Secure handling of API keys using environment variables.
Setup and Installation
Prerequisites
Python 3.8 or later
A Google API key with access to Gemini
pip (Python package installer)
Installation Steps
Clone the Repository

bash
Copy code
git clone https://github.com/SHUBHANKARPOLYGON/Shubhankar-AI.git
cd SHUBHANKAR-AI
Create a Virtual Environment (Optional but Recommended)

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Set Up Environment Variables Create a .env file in the project directory and add your Google API key:

env
Copy code
GOOGLE_API_KEY=your_google_api_key
Run the Application

bash
Copy code
python app.py
Access the Web Interface Open your browser and navigate to:

arduino
Copy code
http://127.0.0.1:5000/
Usage
Enter your question in the input field on the web page.
Submit the question to receive an AI-generated response.
The response will be displayed on the web page, and audio playback will be available if text-to-speech is enabled.
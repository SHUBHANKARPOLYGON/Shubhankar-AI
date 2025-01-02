
# AI Assistant Using Gemini API
### Overview

This AI Assistant is a Flask-based web application that leverages Google's Gemini API to answer user questions in natural language. It also supports text-to-speech functionality for verbal responses. The project demonstrates the integration of generative AI with a web-based user interface.

### Features

- User-friendly interface for asking questions via a web browser.
- Integration with Google Gemini API for natural language processing and AI-generated answers.
- Text-to-speech functionality using the gTTS library.
- Local deployment with Flask for testing and debugging.
- Secure handling of API keys using environment variables.

## Setup and Installation
### Prerequisites
- Python 3.8 or later
- A Google API key with access to Gemini
- pip (Python Package Installer)

### Installation Steps

- Clone the Repository

```
  git clone https://github.com/SHUBHANKARPOLYGON/Shubhankar-AI.git
  cd Shubhankar-AI
```
- Create a Virtual Environment (Optional)

```
  python -m venv venv
  source venv/bin/activate
```
- Install Dependencies

```
  pip install -r requirements.txt
```
- Set Up Environment Variables Create a ```.env``` file in the     project directory and add your Google API key:

```
  GOOGLE_API_KEY=your_google_api_key
```
- Run the Application

```
  python app.py
```
- Access the Web Interface Open your browser and navigate to:

```
  http://127.0.0.1:5000/
```
  ### Usage
  - Enter your question in the input field on the web page.
  - Submit the question to receive an AI-generated response.
  - The response will be displayed on the web page, and audio playback will be available if text-to-speech is enabled.

### Technologies Used
- Flask: Web framework for Python.
- Google Gemini API: For natural language processing and AI-generated answers.
- gTTS: For text-to-speech conversion.
- HTML/CSS: For the user interface.
  
### Security

- API keys are stored securely in a ```.env``` file and accessed using environment variables.
- Ensure your ```.env``` file is added to ```.gitignore``` to prevent it from being uploaded to GitHub.

### Troubleshooting
  1. App Not Starting
  - Ensure all dependencies are installed: ```pip install -r requirements.txt```
  - Verify your ```.env``` file contains a valid API key.

  2. Flask Server Not Responding
  - Check if another application is using port 5000.
  - Review the logs for errors: ```python app.py```

  3. API Key errors
  - Confirm that the API key has sufficient permissions for the Gemini API.

  ### Contributing
  Contributions are welcome! Please fork this repository and submit a pull request with your improvements.

  ### License
  This project is licensed under the MIT License. See the ```LICENSE``` file for details.

  ### Acknowledgments
  - ```Google Generative AI```
  - ```Flask Framework```


This ```README.md``` provides a clear overview, setup instructions, and important details about the AI Assistant.






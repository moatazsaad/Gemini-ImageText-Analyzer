Gemini AI Image and Text Analyzer

gemini-image-text-analyzer.streamlit.app

Welcome to the Gemini AI Image and Text Analyzer! This Streamlit application allows you to interact with the Gemini AI by providing either a text prompt, an image, or both. The AI generates content based on your input using Google's Generative AI models.
Features:

-Text Prompt Analysis: Enter a text prompt to receive a response from the Gemini AI.
-Image Analysis: Upload an image for the AI to analyze and generate a response.
-Combined Analysis: Provide both a text prompt and an image to get a comprehensive response.
-User-Friendly Interface: Simple and intuitive interface built with Streamlit.

Prerequisites:

Python 3.10
Streamlit
Pillow
Python-dotenv
Google's Generative AI library

Installation
Clone the repository:

git clone https://github.com/your-username/gemini-ai-analyzer.git
cd gemini-ai-analyzer

Install the required packages:

pip install -r requirements.txt

Set up your environment variables:

Create a .env file in the root directory and add your Google API key:

GOOGLE_API_KEY=your_google_api_key_here

Running the Application

Start the Streamlit app:

streamlit run app.py

Usage

Input Prompt:
    Enter a text prompt in the provided text input field.

Upload Image:
    Upload an image file in JPG, JPEG, or PNG format.

Analyze:
    Click the "Analyze" button to get a response from the Gemini AI based on your input.

Clear Inputs:
    Click the "Clear Inputs" button to reset the input fields and start over.

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Configures genai library with the API key from the environment variable
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load OpenAI model and get responses

def get_gemini_response(input, image):
    model = None
    if image:
        model = genai.GenerativeModel('gemini-pro-vision')
    else:
        model = genai.GenerativeModel('gemini-pro')
    
    if model:
        if image and input:
            # Generate content using both input and image
            response = model.generate_content([input, image])
        else:
            response = model.generate_content(input)
        
        return response.text
    else:
        return "Please provide a question or upload an image."

# Initialize our streamlit app

st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini AI Image and Text Analyzer")
# Creates a text input field for the user
input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
# Initializes the image variable as an empty string
image = ""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    # Display the uploaded image.
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit = st.button("Analyze")

# Checks if the submit button is clicked
if submit:
    # Checks if the input is provided
    if input:
        # Calls the function to get response
        response = get_gemini_response(input, image)
        # Displays the response
        st.subheader("The Response is")
        st.write(response)
    else:
        st.error("Please provide a question or upload an image.")

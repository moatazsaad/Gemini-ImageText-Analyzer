from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Configures genai library with the API key from the environment variable
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load OpenAI model and get responses

def get_gemini_response(input_text, image):
    if image:
        model = genai.GenerativeModel('gemini-pro-vision')
    else:
        model = genai.GenerativeModel('gemini-pro')

    if image and input_text:
        # Generate content using both input and image
        response = model.generate_content([input_text, image])
    elif input_text:
        response = model.generate_content(input_text)
    else:
        return "Please provide a question or upload an image."

    return response.text

# Initialize our Streamlit app

st.set_page_config(page_title="Gemini AI Image and Text Analyzer")

st.title("Gemini AI Image and Text Analyzer")
st.write("Upload an image or provide a text prompt to get a response from the Gemini AI.")

# Create columns for better layout
col1, col2 = st.columns(2)

# Text input field for the user
with col1:
    input_text = st.text_input("Input Prompt:", key="input")

# File uploader for image
with col2:
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Display the uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
else:
    image = None

# Analyze button
submit = st.button("Analyze")

# Check if the submit button is clicked
if submit:
    # Check if the input is provided
    if input_text or image:
        with st.spinner("Processing..."):
            # Call the function to get response
            response = get_gemini_response(input_text, image)
        st.success("Analysis Complete!")
        st.subheader("The Response is")
        st.write(response)
    else:
        st.error("Please provide a question or upload an image.")

# Provide example inputs and images for user guidance
with st.expander("Examples"):
    st.write("**Example Prompts:**")
    st.write("- Describe the image I uploaded.")
    st.write("- Analyze the scene in the picture.")
    st.write("- Provide insights on the following image.")
    
    st.write("**Example Images:**")
    example_image_1 = Image.open("example1.jpg")
    st.image(example_image_1, caption="Example Image 1", use_column_width=True)
    
    example_image_2 = Image.open("example2.jpg")
    st.image(example_image_2, caption="Example Image 2", use_column_width=True)

# Option to clear inputs
if st.button("Clear Inputs"):
    st.session_state.input = ""
    st.experimental_rerun()

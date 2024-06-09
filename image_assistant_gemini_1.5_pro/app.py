import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
from PIL import Image

# Load API key securely using dotenv
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configuration and error handling
if GOOGLE_API_KEY is None:
    st.error("GOOGLE_API_KEY not found in .env file. Please set it.")
    st.stop()  # Prevent app from running without the API key

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro')

# Streamlit app structure
st.set_page_config(page_title="Gemini Pro Image Demo")
st.title("Gemini Pro Image Application")

# Using a form for better user experience
with st.form(key="input_form"):
    input_text = st.text_input("Input Prompt:", key="input")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if input_text or uploaded_file:
            if uploaded_file:
                image = Image.open(uploaded_file)
                st.image(image, caption="Uploaded Image.", use_column_width=True)
                content = [input_text, image] if input_text else [image]
            else:
                content = [input_text]

            with st.spinner("Generating response..."):  # Provide visual feedback
                response = model.generate_content(content).text
                st.subheader("Response:")
                st.write(response)
        else:
            st.warning("Please enter a question or upload an image.")

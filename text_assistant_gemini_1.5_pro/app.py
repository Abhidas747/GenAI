import os

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

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
st.set_page_config(page_title="Text Assistant Demo")
st.title("Gemini Pro Application") 

# Using a form for better user experience
with st.form(key="input_form"):
    question = st.text_area("Input your question:", height=100)
    submit_button = st.form_submit_button(label='Submit')

    if submit_button: 
        if question:  # Only proceed if there's input
            with st.spinner("Generating response..."): # Provide visual feedback
                response = model.generate_content(question).text 
                st.subheader("Response:")
                st.write(response) 
        else:
            st.warning("Please enter a question.") 
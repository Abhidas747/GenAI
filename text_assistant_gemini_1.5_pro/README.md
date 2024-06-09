# Simple Text Assistant App 
### Using gemini-1.5-pro model

#### This code creates a user-friendly Streamlit web app that lets users ask questions and get responses from Google's powerful Gemini Pro language model.

Here's what it does in a nutshell:
1. Secure Setup: It safely loads your Google API key from a .env file, ensuring your credentials are kept secret.
2. Connects to Gemini Pro: It sets up a connection to the gemini-1.5-pro model, ready to process text generation requests.
3. Streamlit Interface:
- It builds a simple webpage with a title and an input box where users can type their questions.
- When a user submits a question, the app sends it to Gemini Pro.
- While waiting for a response, it shows a "Generating response..." message so the user knows it's working.
- Finally, it displays Gemini Pro's generated answer clearly on the page.

In short, this code provides a straightforward way for anyone to interact with a cutting-edge AI language model through an easy-to-use web interface.
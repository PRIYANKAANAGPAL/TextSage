import streamlit as st
from transformers import pipeline

# Specify the model and revision
model_name = "facebook/bart-large-cnn"
model_revision = "main"

# Initialize the pipeline with model and revision
summarizer = pipeline("summarization", model=model_name, revision=model_revision)

def summarize_text(text):
    try:
        # Perform summarization
        summary = summarizer(text, max_length=250, min_length=100, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return str(e)

# Define the run function for the Streamlit app
def run():
    # st.title("TextSage: Text Summarization Service")

    st.header("Enter text to summarize")
    user_input = st.text_area("Text to summarize")

    if st.button("Summarize"):
        if user_input.strip():
            summary = summarize_text(user_input)
            st.write("Summary:", summary)
        else:
            st.write("Please enter text to summarize.")

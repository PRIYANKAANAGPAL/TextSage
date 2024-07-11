import streamlit as st
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load T5 model and tokenizer
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Function to perform text translation
def translate_text(input_text, target_language):
    try:
        # Tokenize the input text and prepare inputs for the model
        inputs = tokenizer("translate English to " + target_language + ": " + input_text, return_tensors="pt")

        # Perform translation
        translated_ids = model.generate(inputs.input_ids, max_length=150, num_beams=4, early_stopping=True)

        # Decode the translated text
        translated_text = tokenizer.decode(translated_ids[0], skip_special_tokens=True)
        return translated_text
    except Exception as e:
        return str(e)

# Streamlit UI for Translation Service
def run():
    # st.title("TextSage: Text Translation Service")

    st.header("Enter text to translate")
    input_text = st.text_area("Text to translate", height=150)
    target_language = st.selectbox("Select target language", [
        "Spanish", "French", "German", "Chinese",
        "Arabic", "Italian", "Russian", "Japanese",
        "Korean", "Portuguese", "Dutch", "Swedish",
        "Greek", "Turkish", "Thai", "Hindi",
        "Indonesian", "Vietnamese", "Hebrew", "Polish",
        "Romanian", "Czech", "Hungarian", "Finnish",
        "Danish", "Norwegian", "Ukrainian", "Bengali",
        "Malay", "Tagalog" , "English"
    ])

    if st.button("Translate"):
        if input_text.strip() and target_language:
            translated_text = translate_text(input_text, target_language)
            st.write("Translated Text:")
            st.write(translated_text)
        elif not input_text.strip():
            st.write("Please enter text to translate.")
        elif not target_language:
            st.write("Please select a target language.")

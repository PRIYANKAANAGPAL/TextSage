import streamlit as st
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load the T5 model and tokenizer
model = T5ForConditionalGeneration.from_pretrained('t5-small')
tokenizer = T5Tokenizer.from_pretrained('t5-small')

# Define the paraphrasing function
def paraphrase_text(input_text, word_length):
    inputs = tokenizer.encode_plus(
        input_text,
        max_length=512,
        return_attention_mask=True,
        return_tensors='pt'
    )
    outputs = model.generate(
        inputs['input_ids'],
        attention_mask=inputs['attention_mask'],
        max_length=word_length,
        num_beams=4,
        early_stopping=True
    )
    paraphrased_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return paraphrased_text

# Define the run function for the Streamlit app
def run():
    # st.title("TextSage: Paraphrasing Service")

    # Get user input
    st.header("Enter text to paraphrase")
    user_input = st.text_area("Text to paraphrase")
    max_length = st.slider("Desired length", min_value=10, max_value=400, value=50)

    # Create a button to paraphrase the text
    if st.button("Paraphrase"):
        if user_input.strip():
            paraphrased_text = paraphrase_text(user_input, max_length)
            st.write("Paraphrased Text:", paraphrased_text)
        else:
            st.write("Please enter text to paraphrase.")

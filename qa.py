import streamlit as st
from transformers import pipeline

# Load the QA pipeline with the specific model
model_name = "deepset/roberta-base-squad2"
qa_pipeline = pipeline("question-answering", model=model_name)

# Define function to perform question answering
def answer_question(context, question):
    try:
        result = qa_pipeline(question=question, context=context)
        return result['answer']
    except Exception as e:
        return str(e)

# Define the run function for the Streamlit app
def run():
    # st.title("TextSage: Question Answering Service")

    st.header("Provide context and ask questions")
    context = st.text_area("Context (e.g., a passage of text)", height=300)
    questions = st.text_input("Questions (comma-separated)", "What is the main idea?, How many characters are in the context?")

    if st.button("Answer Questions"):
        if context.strip() and questions.strip():
            questions_list = [q.strip() for q in questions.split(",")]
            st.write("Answers:")
            for q in questions_list:
                answer = answer_question(context, q)
                st.write(f"Question: {q}")
                st.write(f"Answer: {answer}")
        elif not context.strip():
            st.write("Please provide context.")
        elif not questions.strip():
            st.write("Please ask at least one question.")

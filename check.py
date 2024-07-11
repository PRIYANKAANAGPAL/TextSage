import streamlit as st
import language_tool_python

# Define the grammar and spell check function
def grammar_check(text):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    
    # Correct the text
    corrected_text = language_tool_python.utils.correct(text, matches)
    
    # Display corrected text and suggestions
    st.write("Corrected Text:")
    st.write(corrected_text)

    if matches:
        st.write("Suggestions:")
        for match in matches:
            st.write(f"Type: {match.ruleId}, Message: {match.message}")

def run():
    # st.title("TextSage: Grammar and Spell Checking Service")
    st.header("Enter text to check grammar and spelling")
    user_input = st.text_area("Text for grammar and spell check")
    
    if st.button("Check"):
        if user_input.strip():
            grammar_check(user_input)
        else:
            st.write("Please enter text to check.")

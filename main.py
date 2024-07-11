import streamlit as st
from streamlit_option_menu import option_menu

# Import the necessary modules
import check
import paraphrase
import qa
import summarise
import transaltion

# Define the main function to run the app
def main():
    st.title("TextSage Text Processing Suite")
    st.header("Choose a service")

    selected = option_menu(
        menu_title=None,  # required
        options=["Grammar Check", "Paraphrase", "Question and Answer", "Summarization", "Translation"],  # required
        icons=["spellcheck", "sync-alt", "question-circle", "smile", "language"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
    )

    if selected == "Grammar Check":
        check.run()
    elif selected == "Paraphrase":
        paraphrase.run()
    elif selected == "Question and Answer":
        qa.run()
    elif selected == "Summarization":
        summarise.run()
    elif selected == "Translation":
        transaltion.run()

# Run the main function
if __name__ == "__main__":
    main()

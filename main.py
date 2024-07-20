import streamlit as st
from pages import sign_language_detection

def main():
    st.title("Main Dashboard")
    
    st.markdown("## Welcome to the Sign Language Conversion/Detection App")
    st.markdown("### Please select a module below:")

    page = st.selectbox("Choose a page", ["Home", "Sign Language Detection",])

    if page == "Sign Language Detection":
        sign_language_detection.app()
    
    else:
        st.write("Welcome to the homepage. Select a page to navigate.")

if __name__ == "__main__":
    main()

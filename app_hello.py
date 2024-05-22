import streamlit as st

st.set_page_config(
    page_title="Zero-Shot Classification",
    page_icon="👋",
)

st.write("# Welcome to Zero-Shot Classification! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
Zero-shot text classification is a task in natural language processing where a model is trained on a 
set of labeled examples but is then able to classify new examples from previously unseen classes.
"""
)
st.image('capture.png')


#
import streamlit as st
import pandas as pd
import numpy as np

st.title("🤗 Zero Shot Classification")
st.caption(" 🚀 A Streamlit app")

text = st.text_area("Enter text for classification", placeholder = "Reset my password") 

classes = st.text_input("Enter possible class names (comma-separated)")

# st.form_submit_button()

classes_list = classes.split(',')
# l1

from transformers import pipeline

# Home Work use a button to initiate the inference
# to replace pipeline with automodel/autotokenizer 
# How streamlit works ==> How flask api works 
pipe = pipeline('zero-shot-classification','facebook/bart-large-mnli')

if text and classes_list:
    output = pipe(text, classes_list)
    # How do I reset my password
    # ['IT issue', "News", "Entertainment"]
    # IT issue, News, Entertainment

    st_output = dict(zip(output['labels'],output['scores']))
    for i,k in st_output.items():
        # st.write(f"{i}========{k}")
        st.progress(k, text = f"{i:_<95} {k:.2f}")
    ## --> Home Work -- 1. Understand concept of session_state ==== 2. Apply in zeroshot ==== 3. observe feseablity for bison 
    ## --> Home Work -- Use logging
    ## --> add editable df - 
import pandas as pd
import streamlit as st
from transformers import pipeline

st.title("Zeroshot Classification - Batched")
st.caption("A streamlit powered app")

uploaded_file = st.file_uploader("Upload your file here")
if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_excel(uploaded_file)
    st.write(df)
col_name = st.text_input("Which column contains text that you want to classify")

classes = st.text_input("Enter possible class names (comma-separated)")

pipe = pipeline('zero-shot-classification','facebook/bart-large-mnli')
batch_output = pipe(list(df[col_name]),classes)
df['predicted']=[i['labels'][0] for i in batch_output]

st.write(df)

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode("utf-8")

csv = convert_df(df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name="large_df.csv",
    mime="text/csv",
)
# with st.form('upload-form', clear_on_submit=True):
#     uploaded_file = st.file_uploader("Upload your file here")
#     submitted = st.form_submit_button("Upload")
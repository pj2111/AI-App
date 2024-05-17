import pandas as pd
import streamlit as st

st.title("Zeroshot Classification - Batched")
st.caption("A streamlit powered app")

st.write("Upload your file here")
st.button("Upload")
classes = st.text_input("Enter possible class names (comma-separated)")

st.write("Download your labeled file below")
st.button("Download")

import streamlit as st
import pandas as pd
from io import StringIO

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_excel(uploaded_file)
    st.write(dataframe)
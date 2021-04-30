import streamlit as st

st.title("Group 2!")
st.title("DS4B Final Project")

import pandas as pd

uploaded_file = st.file_uploader("GHG avg by food groups.xlsx", type="xlsx")

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    st.dataframe(df)
    st.table(df)

# Load file in dataframe format
#df_plant_starches = pd.read_excel("GHG avg by food groups.xlsx","Plant starches")
st.write("hello")

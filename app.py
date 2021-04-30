import streamlit as st

st.title("Group 2!")
st.title("DS4B Final Project")

import pandas as pd

df = pd.read_csv("GHG avg by food groups.csv")
st.dataframe(df)
st.table(df)

# Load file in dataframe format
#df_plant_starches = pd.read_excel("GHG avg by food groups.xlsx","Plant starches")
st.write("hello")

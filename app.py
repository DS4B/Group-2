import streamlit as st

st.title("Group 2!")
st.title("DS4B Final Project")

import pandas as pd

df = pd.read_csv("GHG avg by food groups.csv")
avg_ghg = df.pop('Avg GHG (kg CO2 equivalent/ kg product)')
df = df.dropna()
st.dataframe(df)

# Load file in dataframe format
#df_plant_starches = pd.read_excel("GHG avg by food groups.xlsx","Plant starches")
st.write("hello")

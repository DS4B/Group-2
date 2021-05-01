import streamlit as st

st.title("Group 2!")
st.title("DS4B Final Project")

import pandas as pd

df = pd.read_csv("GHG avg by food groups.csv")
avg_ghg = df.pop('Avg GHG (kg CO2 equivalent/ kg product)')
df = df.dropna()
st.dataframe(df)


grouped_df = df.groupby(by=['Food group']).mean()
grouped_df = grouped_df.sort_values(by = 'Total GHG (kg CO2 equivalent/ kg product)', ascending = False)
st.write(grouped_df)

# Create bar chart for Total GHG by food group
f = grouped_df.plot.bar(stacked = True)
st.pyplot()

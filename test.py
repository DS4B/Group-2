import streamlit as st
import pandas as pd

st.write("Hello world")
df = pd.read_csv("co2_emissions.csv")
st.write(df)
        

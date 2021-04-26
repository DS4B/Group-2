import streamlit as st
import pandas as pd

st.write("Hello world")
df = pd.read_csv("co2_emission.csv")
st.write(df)
        
st.write("hello")

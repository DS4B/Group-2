import streamlit as st

st.title("Food Carbon Footprint")
st.subheader("DS4B Final Project")
st.text('Britnie Nguyen, Angeline Utomo, JoJo Zhang, Yan Zhou Chen')
st.text('Spring 2021')

import pandas as pd
from PIL import Image

col1, col2 = st.beta_columns(2)
with col1:
        image = Image.open('food_production_chain.jpeg')
        st.image(image, use_column_width = True)
        
with col2:
        st.write('What is this image and why we should be talking about food carbon footprint!')


df = pd.read_csv("GHG avg by food groups.csv")
avg_ghg = df.pop('Avg GHG (kg CO2 equivalent/ kg product)')
df = df.dropna()

grouped_df = df.groupby(by=['Food group']).mean()
grouped_df = grouped_df.sort_values(by = 'Total GHG (kg CO2 equivalent/ kg product)', ascending = False)
st.write(grouped_df)


# Create bar chart for Total GHG by food group
st.set_option('deprecation.showPyplotGlobalUse', False)
rm_total = grouped_df.pop('Total GHG (kg CO2 equivalent/ kg product)')
new_grouped_df = grouped_df
f = new_grouped_df.plot.bar(stacked = True)
st.pyplot()

st.markdown("## " + 'Total GHG Emission by food group')	
st.markdown("#### " +"What food group would you like to see?")

selected_metrics = st.selectbox(
    label="Choose...", options=['Plant starch','Plant protein','Animal protein','Vegetable','Fruit','Dairy','Other'])

if selected_metrics == 'Plant starch':
  food_group = 'Plant starch'
  food_df = df[df['Food group'] == food_group]
  food_df.pop('Total GHG (kg CO2 equivalent/ kg product)')
  food_df = food_df.set_index('Food product')
  fig = food_df.plot.bar(stacked = True)
  st.pyplot()
  
if selected_metrics == 'Plant protein':
  food_group = 'Plant protein'
  food_df = df[df['Food group'] == food_group]
  food_df.pop('Total GHG (kg CO2 equivalent/ kg product)')
  food_df = food_df.set_index('Food product')
  fig = food_df.plot.bar(stacked = True)
  st.pyplot()
  
if selected_metrics == 'Animal protein':
  food_group = 'Animal protein'
  food_df = df[df['Food group'] == food_group]
  food_df.pop('Total GHG (kg CO2 equivalent/ kg product)')
  food_df = food_df.set_index('Food product')
  fig = food_df.plot.bar(stacked = True)
  st.pyplot()
  
if selected_metrics == 'Vegetable':
  food_group = 'Vegetable'
  food_df = df[df['Food group'] == food_group]
  food_df.pop('Total GHG (kg CO2 equivalent/ kg product)')
  food_df = food_df.set_index('Food product')
  fig = food_df.plot.bar(stacked = True)
  st.pyplot()
  
  
if selected_metrics == 'Fruit':
  food_group =  'Fruit'
  food_df = df[df['Food group'] == food_group]
  food_df.pop('Total GHG (kg CO2 equivalent/ kg product)')
  food_df = food_df.set_index('Food product')
  fig = food_df.plot.bar(stacked = True)
  st.pyplot()
  
if selected_metrics == 'Dairy':
  food_group = 'Dairy'
  food_df = df[df['Food group'] == food_group]
  food_df.pop('Total GHG (kg CO2 equivalent/ kg product)')
  food_df = food_df.set_index('Food product')
  fig = food_df.plot.bar(stacked = True)
  st.pyplot()
  
if selected_metrics == 'Other':
  food_group = 'Miscellaneous'
  food_df = df[df['Food group'] == food_group]
  food_df.pop('Total GHG (kg CO2 equivalent/ kg product)')
  food_df = food_df.set_index('Food product')
  fig = food_df.plot.bar(stacked = True)
  st.pyplot()



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



  st.header("How much food GHG does your meal contribute?")

# Make food_dict a global variable so my functions can have access to it
global food_dict

food_dict = {'Wheat & Rye': 1.4,
'Cornmeal': 1.1,
'Barley': 1.1,
'Oatmeal': 1.6,
'Rice': 4,
'Potatoes': 0.3,
'Cassava': 0.9,
'Other Pulses': 1.6,
'Peas': 0.8,
'Nuts': 0.2,
'Groundnuts': 2.4,
'Soymilk': 1,
'Tofu': 3,
'Beef': 59.6,
'Lamb & Mutton': 24.5,
'Pork': 7.2,
'Poultry': 6.1,
'Eggs': 4.5,
'Fish (farmed)': 5.1,
'Shrimps (farmed)': 11.8, 
'Tomatoes': 1.4,
'Onions & Leeks': 0.3,
'Root Vegetables': 0.3,
'Cabbages': 0.4,
'Other Vegetables': 0.5,
'Citrus Fruits': 0.3,
'Bananas': 0.8,
'Apples': 0.3,
'Berries & Grapes': 1.1,
'Other Fruits': 0.7,
'Milk': 2.8,
'Cheese': 21.2, 
'Wine': 1.4,             
'Coffee': 16.5,
'Dark Chocolate': 18.7,
'Cane Sugar': 2.6,
'Beet Sugar': 1.4,
'Soybean Oil': 6,
'Palm Oil': 7.6,
'Sunflower Oil': 3.5,
'Rapeseed Oil': 3.7,
'Olive Oil': 6,
'Average plant starch': 1.5,
'Average plant protein': 1.5,
'Average animal protein': 17,
'Average vegetable': 0.6,
'Average fruit': 0.6,
'Average plant oils': 5.4,
}


save_list = st.multiselect('Which food items would you like to include?', list(food_dict))
st.markdown(" ")


st.subheader("Use the following conversion cheat sheet to help you estimate the mass of your food items in grams:")
st.markdown(" ")
"""- 1 cup of uncooked rice/ beans = 200g
- 1 cup of uncooked pasta = 100g
- 1 medium-sized potato = 150g
- 1 slice of bread = 25g
- 1 egg = 50g
- A palm-sized portion of meat = 85g
- 1 cup of raw non-leafy vegetables = 160g
- 1 cup of raw leafy vegetables = 80g
- A handful of berries/ 1 banana/ 1 apple/ 1 orange = 80g
- 1/3 cup of nuts = 50g
- 1 cup of milk = 240g
- 1 tbsp of ground coffee = 5g
"""
st.markdown(" ")


mass_list = []
x = 0
for item in save_list:
  st.write(save_list[x])
  mass = st.number_input('How many grams of this item did you consume?', min_value=0, key = str(x))
  mass_list.append(mass)
  x += 1  
st.markdown(" ")
  
  
def getGHG(save_list, mass_list):
  ghg_list = []
  for idx,save in enumerate(save_list):  
    ghg_amount = food_dict[save]

    ghg_calculator = ghg_amount *mass_list[idx]
    ghg_list.append(ghg_calculator)
    
  return ghg_list

ghg_list = getGHG(save_list,mass_list)
total_ghg = sum(ghg_list)
st.write(f'These food items contributed {int(total_ghg)} g CO2 equivalent')


import matplotlib.pyplot as plt
import numpy as np

def func(pct, allvals):
    absolute = int(round(pct/100.*np.sum(allvals)))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)
  
st.subheader("Your food GHG breakdown:")
fig = plt.pie(ghg_list, explode=None, labels=save_list, colors=None, autopct=lambda pct: func(pct, ghg_list), shadow=False, radius=0.8)
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)
      

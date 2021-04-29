import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.write("Hello world")
df = pd.read_csv("co2_emission.csv")

food_ghg_map = """<script type='text/javascript' src='https://prod-useast-b.online.tableau.com/javascripts/api/viz_v1.js'></script><div 
class='tableauPlaceholder' style='width: 1000px; height: 850px;'><object class='tableauViz' width='1000' height='850' style='display:none;'><param name='host_url' 
value='https%3A%2F%2Fprod-useast-b.online.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='&#47;t&#47;dsbfinal' /><param 
name='name' value='Food_GHG_1990-2015_by_tonnes&#47;Dashboard1' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='showAppBanner' value='false' /
></object></div>
"""
components.html(food_ghg_map, width = 850, height = 400, scrolling = true)

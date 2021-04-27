import streamlit as st
import streamlit.components.v1 as components

st.title("Tableau Testing")
st.write("Annual consumption-based CO2 emissions, measured in million tonnes per year (1830-2019)")

def main():
  html_temp = "<script type='text/javascript' src='https://prod-useast-b.online.tableau.com/javascripts/api/viz_v1.js'></script><div class='tableauPlaceholder' style='width: 1203px; height: 686px;'><object class='tableauViz' width='100%' height='100%' style='display:none;'><param name='host_url' value='https%3A%2F%2Fprod-useast-b.online.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='&#47;t&#47;btnn' /><param name='name' value='DataScienceforBiotechnology&#47;Sheet1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='showAppBanner' value='false' /></object></div>"
  components.html(html_temp)

if __name__ == "__main__":
  main()

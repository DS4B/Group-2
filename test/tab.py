import streamlit as st
import streamlit.components.v1 as components

st.title("Tableau Testing")
st.write("Annual consumption-based CO2 emissions, measured in million tonnes per year (1830-2019)")

def main():
  html_temp = """
    <p id = "test"></p>
    <script type='text/javascript' src='https://prod-useast-b.online.tableau.com/javascripts/api/viz_v1.js'></script>
    
    <div class='tableauPlaceholder' id='my_map' style='position:relative'>    
    <object class='tableauViz' style='display:none;'>
    <param name='host_url' value='https%3A%2F%2Fprod-useast-b.online.tableau.com%2F' /> 
    <param name='embed_code_version' value='3' /> 
    <param name='site_root' value='&#47;t&#47;btnn' />
    <param name='name' value='DataScienceforBiotechnology&#47;Sheet1' />
    <param name='tabs' value='no' />
    <param name='toolbar' value='yes' />
    <param name='showAppBanner' value='false' /></object></div>"
    
    var divElement = document.getElementById('my_map');
    var vizElement = divElement.getElementsByTagName('object')[0];
    if (divElement.offsetWidth > 800)
    {
      vizElement.style.width = '1130px';
      vizElement.style.height = '727px';
            document.getElementById("test").innerHTML = "ITS ONE";
    } else if (divElement.offsetWidth > 500)
    {
      vizElement.style.width = '1130px';
      vizElement.style.height = '727px';
            document.getElementById("test").innerHTML = "ITS TWO";

    } else {
      vizElement.style.width = '100%';
      vizElement.style.height = '1527px';
            document.getElementById("test").innerHTML = "ITS THREE";

    }
    
  """
  
  components.html(html_temp)

if __name__ == "__main__":
  main()
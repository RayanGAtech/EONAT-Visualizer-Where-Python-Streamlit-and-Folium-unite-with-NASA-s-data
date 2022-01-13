import map_1
import streamlit as st
from streamlit_folium import folium_static


sas = map_1.Geo_map()

class stream_dash():

    sas.wildfire()
    sas.vol()
    sas.iceberg()

    #Bootstap import
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

    #Navbar
    st.markdown("""
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
      <a class="navbar-brand" href="https://www.linkedin.com/in/rayan-g-abukelab-18ab2914a/" target="_blank">EONAT VISUAL</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="https://github.com/morgan-techy" target="_blank">Github</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="https://twitter.com/Captain39Morgan" target="_blank">Twitter</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="https://www.linkedin.com/in/rayan-g-abukelab-18ab2914a/" target="_blank">Linkedin</a>
          </li>
        </ul>
      </div>
    </nav>
    """, unsafe_allow_html=True)

        #sidebar element
    with st.sidebar:
        # day display
        st.session_state.my_slider = 0
        slider = st.slider(
          label='Choose a Value', min_value=1,
          max_value=1000, value=1, key='my_slider')

    #header text
    st.markdown('''# *Earth Observatory Natural Event Tracker*
    A simple Natural Event Tracker pulling data from *NASA API*.''')
    st.header('**Tracker Map**')

    # map display
    folium_static(sas.m)

    # text
    st.info('Credit: Created by @Morgan_techy ([Rayan G. A.](https://www.linkedin.com/in/rayan-g-abukelab-18ab2914a/))')
    st.info(slider)
    #JS import
    st.markdown("""
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    """, unsafe_allow_html=True)
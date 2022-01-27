import folium
import requests
import streamlit as st
from streamlit_folium import folium_static

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

#header text
st.markdown('''# *Earth Observatory Natural Event Tracker*
A simple Natural Event Tracker pulling data from *NASA API*.''')
st.header('**Tracker Map**')

# sidebar to hold the side page features and text
with st.sidebar:
# slider to allow display an event on a particular day on the map
    slider = st.slider('Day Range:', 0, 365)
    st.write('Day Range:', slider)

# API url to get the data from nasa api    
url1 = f'https://eonet.gsfc.nasa.gov/api/v3/events?days={slider}'
#request the data
r = requests.get(url1) 
#convert the data to json format and call the events catagories
p_r = r.json()
events = p_r['events']
#create a map object
m = folium.Map(location= [15,16], tiles="Cartodbdark_matter",zoom_start=2, min_zoom = 2, max_bounds=True)

# volcano events function
def volcano():
            for count in range(len(events)):
                for i in p_r['events'][count]['geometry']:
                    cord_A = i['coordinates'][1]
                    cord_B = i['coordinates'][0]
                for j in p_r['events'][count]['categories']:
                        event_type = j['title']
                        if (event_type) == 'Volcanoes':
                                    #global tooltip
                                    tooltip = 'click for more info'
                                    type = 'Volcano\nGens'
                                    #create markers
                                    folium.Marker([cord_A, cord_B], popup=f'<strong>{type}<\strong>', tooltip=tooltip, icon= folium.features.CustomIcon(icon_image='icon/volcano.png', icon_size=(20,20))).add_to(m)
# wildfire events function
def wildfire():
            for count in range(len(events)):
                for i in p_r['events'][count]['geometry']:
                        cord_A = i['coordinates'][1]
                        cord_B = i['coordinates'][0]
                for j in p_r['events'][count]['categories']:
                    event_type = j['title']
                    if (event_type) == 'Wildfires':
                                #global tooltip
                                tooltip = 'click for more info'
                                type = 'Wildfires'
                                #create markers
                                folium.Marker([cord_A, cord_B], popup=f'<strong>{type}<\strong>', tooltip=tooltip, icon= folium.features.CustomIcon(icon_image='icon/fire-solid.png', icon_size=(20,20))).add_to(m)
# iceberg events function
def iceberg():
                for count in range(len(events)):
                    for i in p_r['events'][count]['geometry']:
                                cord_A = i['coordinates'][1]
                                cord_B = i['coordinates'][0]
                    for j in p_r['events'][count]['categories']:
                        event_type = j['title']
                        if (event_type) == 'Sea and Lake Ice':
                                    #global tooltip
                                    tooltip = 'click for more info'
                                    type = 'Iceberg'
                                    #create markers
                                    folium.Marker([cord_A, cord_B], popup=f'<strong>{type}<\strong>', tooltip=tooltip, icon= folium.features.CustomIcon(icon_image='icon/iceberg.png', icon_size=(20,20))).add_to(m)

 

# sidebar to hold the side page features and text
with st.sidebar:
    genre = st.radio(
     "Please select an event:",
     ('All','volcano', 'wildfire', 'iceberg'))

    if genre == 'volcano':
        # call the function
        volcano()
    elif genre == 'wildfire':
        # call the function
        wildfire()
    elif genre == 'iceberg':
        # call the function
        iceberg()
    else:
        volcano()
        wildfire()
        iceberg()

        
#display map
folium_static(m)



# text
st.info('Credit: Created by @Morgan_techy ([Rayan G. A.](https://www.linkedin.com/in/rayan-g-abukelab-18ab2914a/))')
st.info('Used API: https://eonet.gsfc.nasa.gov/api/v3/events')


#JS import
st.markdown("""
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)
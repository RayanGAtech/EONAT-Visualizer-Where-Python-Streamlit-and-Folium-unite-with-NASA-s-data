import folium
import requests
import bridge

var_bridge = bridge.b()

class Geo_map:
    
    day = var_bridge.var
    r = requests.get(f'https://eonet.gsfc.nasa.gov/api/v3/events?days=20')
    p_r = r.json()  
    events = p_r['events']
    #create a map object
    m = folium.Map(location= [15,16], tiles="Cartodbdark_matter",zoom_start=2, min_zoom = 2, max_bounds=True)

    def vol(self):
            for count in range(len(Geo_map.events)):
                for i in Geo_map.p_r['events'][count]['geometry']:
                    cord_A = i['coordinates'][1]
                    cord_B = i['coordinates'][0]
                for j in Geo_map.p_r['events'][count]['categories']:
                        event_type = j['title']
                        if (event_type) == 'Volcanoes':
                                    #global tooltip
                                    tooltip = 'click for more info'
                                    type = 'Volcano'
                                    #create markers
                                    folium.Marker([cord_A, cord_B], popup=f'<strong>{type}<\strong>', tooltip=tooltip, icon= folium.features.CustomIcon(icon_image='icon/volcano.png', icon_size=(20,20))).add_to(Geo_map.m)

    def wildfire(self):
            for count in range(len(Geo_map.events)):
                for i in Geo_map.p_r['events'][count]['geometry']:
                        cord_A = i['coordinates'][1]
                        cord_B = i['coordinates'][0]
                for j in Geo_map.p_r['events'][count]['categories']:
                    event_type = j['title']
                    if (event_type) == 'Wildfires':
                                #global tooltip
                                tooltip = 'click for more info'
                                type = 'Wildfires'
                                #create markers
                                folium.Marker([cord_A, cord_B], popup=f'<strong>{type}<\strong>', tooltip=tooltip, icon= folium.features.CustomIcon(icon_image='icon/fire-solid.png', icon_size=(20,20))).add_to(Geo_map.m)

    def iceberg(self):
            for count in range(len(Geo_map.events)):
                for i in Geo_map.p_r['events'][count]['geometry']:
                            cord_A = i['coordinates'][1]
                            cord_B = i['coordinates'][0]
                for j in Geo_map.p_r['events'][count]['categories']:
                    event_type = j['title']
                    if (event_type) == 'Sea and Lake Ice':
                                #global tooltip
                                tooltip = 'click for more info'
                                type = 'Iceberg'
                                #create markers
                                folium.Marker([cord_A, cord_B], popup=f'<strong>{type}<\strong>', tooltip=tooltip, icon= folium.features.CustomIcon(icon_image='icon/iceberg.png', icon_size=(20,20))).add_to(Geo_map.m)
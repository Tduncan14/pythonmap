import folium
import pandas


data = pandas.read_csv("Volcanoes.txt")


lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def color_producer(el):
   if el < 1000:
       return 'green'
   elif  1000 <= el < 3000:
       return 'orange'
   else:
       return 'red'



map = folium.Map(location = [38.58, -99.09], zoom_start = 6, tiles = "Stamen Terrain")


fg = folium.FeatureGroup(name="My Map")


# fg.add_child((folium.Marker(location = [38.2, 99.1], popup = "Hi I am here", icon=folium.Icon(color='green'))))



for lt,ln,el in zip(lat,lon,elev): 

  fg.add_child((folium.Marker(location = [lt,ln], popup = el, icon=folium.Icon(color=color_producer(el)))))



# fg.add_child((folium.Marker(location = [35.2, 99.1], popup = "Hi I am here", icon=folium.Icon(color='blue'))))
# map.add_child(folium.Marker(location = [38.2, 99.1], popup = "Hi I am here", icon=folium.Icon(color='green')))


map.add_child(fg)

map.save("Map1.html")



import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
print(lat)
map= folium.Map(location=[38.58,-99.09], zoom_start=5, tiles='Stamen Terrain')
fg= folium.FeatureGroup(name='My Map')

for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup='hi there im a volcano', icon=folium.Icon(color='red')))

map.add_child(fg)
map.save('Map1.html')
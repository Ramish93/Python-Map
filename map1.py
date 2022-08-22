import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
# print(lat)
map= folium.Map(location=[38.58,-99.09], zoom_start=5, tiles='Stamen Terrain')

fg= folium.FeatureGroup(name='My Map')

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=f'elevation of volcano is: {str(el)} m', icon=folium.Icon(color= 'red' if el > 2000 else 'green' )))

map.add_child(fg)
map.save('Map1.html')
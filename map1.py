import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

def color(el):
    if el < 1000:
        return 'green'
    elif 1000 <= el < 3000:
        return 'orange'
    else:
        return 'red'
# print(lat)
map= folium.Map(location=[38.58,-99.09], zoom_start=5, tiles='Stamen Terrain')

fgv= folium.FeatureGroup(name='Volcanos')

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.Marker(location=[lt, ln], popup=f'elevation of volcano is: {str(el)} m', icon=folium.Icon(color= color(el) )))


fgp= folium.FeatureGroup(name='Population')


fgp.add_child(folium.GeoJson(data=open('world.json', 'r',encoding='UTF-8-sig').read(), style_function=lambda x:{'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save('Map1.html')
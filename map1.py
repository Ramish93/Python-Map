import folium

map= folium.Map(location=[31.752, 72.917], zoom_start=5, tiles='Stamen Terrain')
map.save('Map1.html')
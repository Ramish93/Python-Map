import folium

map= folium.Map(location=[31.752, 72.917], zoom_start=5, tiles='Stamen Terrain')
fg= folium.FeatureGroup(name='My Map')
fg.add_child(folium.Marker(location=[31.652, 72.817], popup='hi there', icon=folium.Icon(color='red')))
map.add_child(fg)
map.save('Map1.html')
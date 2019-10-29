import folium
mapx = folium.Map(location=[38.58,-99.09],zoom_start = 6,tiles = "OpenStreetMap" )

fg = folium.FeatureGroup(name="My Map")

for coordinates in [[9.58,8.09],[9.18, 8.90],[10.5, 7.4],[12.1, 11.7],[9.2, 9.3]]:

    fg.add_child(folium.Marker(location=coordinates, popup = "Hi,I am a Marker", icon = folium.Icon(color='green')))
###fg.add_child(folium.Marker(location=[37.58,-96.09], popup = "Hi,I am a Marker", icon = folium.Icon(color='green')))

mapx.add_child(fg)
mapx.save("mapx.html")
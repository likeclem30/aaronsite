import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat  = list(data["LAT"])
lon  = list(data["LON"])
elv  = list(data["ELEV"])

def colorproducer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
    

mapx = folium.Map(location=[38.58,-99.09],zoom_start = 6,tiles = "OpenStreetMap" )

fg = folium.FeatureGroup(name="My Map")

for lt,ln,el in zip(lat,lon,elv):

##[[9.58,8.09],[9.18, 8.90],[10.5, 7.4],[12.1, 11.7],[9.2, 9.3]]:
    fg.add_child(folium.Marker(location=[lt,ln], popup = str(el)+'m', icon = folium.Icon(color= colorproducer(el))))

    ##fg.add_child(folium.Marker(location=coordinates, popup = "Hi,I am a Marker", icon = folium.Icon(color='green')))
###fg.add_child(folium.Marker(location=[37.58,-96.09], popup = "Hi,I am a Marker", icon = folium.Icon(color='green')))

mapx.add_child(fg)
mapx.save("mapz.html")
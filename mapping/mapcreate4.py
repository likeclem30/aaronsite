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
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius = 6, popup = str(el)+'m',
    fill_color= colorproducer(el),color = 'grey', fill_opacity=0.7))

fg.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read()))
mapx.add_child(fg)
mapx.save("mapw.html")
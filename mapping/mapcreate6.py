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

fgv = folium.FeatureGroup(name="Volcanoes")

for lt,ln,el in zip(lat,lon,elv):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius = 6, popup = str(el)+'m',
    fill_color= colorproducer(el),color = 'grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 2000000 
else 'orange' if 20000000 <= x['properties']['POP2005'] <40000000 else 'red'}))

mapx.add_child(fgv)
mapx.add_child(fgp)
mapx.add_child(folium.LayerControl())
mapx.save("mapcl.html")
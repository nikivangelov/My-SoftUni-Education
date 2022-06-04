import folium

m = folium.Map(location=[42.6897, 23.3154])
output = 'base_map.html'
m.save(output)
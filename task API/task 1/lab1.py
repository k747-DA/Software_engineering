import folium

stadiums_location = {
    "Лужники": [55.715551, 37.554191],
    "Спартак": [55.818015, 37.440262],
    "Динамо": [55.791540, 37.559809]}

map_moscow = folium.Map(location=[55.755826, 37.6173], zoom_start=11)

for stadium, location in stadiums_location.items():
    folium.Marker(location=location, popup=stadium).add_to(map_moscow)

map_moscow.save("MoscowStadiumsMap.html")
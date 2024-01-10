import folium

coordinates = [(54.738227, 55.984619),
               (55.755825, 37.617298)]  # от аэропорта Уфы до аэропорта Москвы

m = folium.Map(location=[coordinates[0][0], coordinates[0][1]], zoom_start=6)

folium.PolyLine(locations=coordinates, color='blue').add_to(m)

avg_lat = (coordinates[0][0] + coordinates[1][0]) / 2
avg_lon = (coordinates[0][1] + coordinates[1][1]) / 2
folium.Marker(location=[avg_lat, avg_lon], popup='Средняя точка').add_to(m)

m.save('path_map.html')

import math


def lonlat_distance(a, b):
    degree_to_meters_factor = 111 * 1000  # 111 километров в метрах
    a_lon, a_lat = a
    b_lon, b_lat = b
    radians_lattitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_lattitude)
    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor  # Смещение по долготе
    dy = abs(a_lat - b_lat) * degree_to_meters_factor  # Смещение по широте
    distance = math.sqrt(dx * dx + dy * dy)  # Расстояние между точками
    return distance


# Запрос координат дома
home_lon = float(input("Введите долготу вашего дома: "))
home_lat = float(input("Введите широту вашего дома: "))

# Запрос координат университета (БашГУ)
university_lon = float(input("Введите долготу университета (БашГУ): "))
university_lat = float(input("Введите широту университета (БашГУ): "))

# Рассчитываем расстояние между домом и университетом
distance = lonlat_distance((home_lon, home_lat), (university_lon, university_lat))

print(f"Приближенное расстояние от вашего дома до университета (БашГУ): {distance:.2f} метров")
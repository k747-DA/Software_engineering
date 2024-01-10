import requests
import random
from io import BytesIO
from PIL import Image

YANDEX_API_KEY = 'вставте свой ключ' # писал ранее

cities = ['Норильск', 'Уфа', 'Канск', 'Красноярск', 'Владивосток']
# Создаем словарь Город - Координаты
city_coordinates = {
    'Норильск': (69.3423, 88.2182),
    'Уфа': (54.7352, 55.9587),
    'Канск': (56.2042, 95.7067),
    'Красноярск': (56.0106, 92.8526),
    'Владивосток': (43.1155, 131.8855)
}

def get_random_coordinates(latitude, longitude, min_radius=0.1, max_radius=0.3):
    radius = random.uniform(min_radius, max_radius)
    new_latitude = random.uniform(latitude - radius, latitude + radius)
    new_longitude = random.uniform(longitude - radius, longitude + radius)
    return new_latitude, new_longitude


def get_city_map(city, initial_coordinates):
    latitude, longitude = get_random_coordinates(*initial_coordinates)
    zoom = random.randint(10, 15)
    map_type = random.choice(['map', 'sat'])
    if map_type == 'map':
        request_url = f'https://static-maps.yandex.ru/1.x/?ll={longitude},{latitude}&z={zoom}&l={map_type}&size=400,400&apikey={YANDEX_API_KEY}&pt={longitude},{latitude},pm2rdl'
    else:
        request_url = f'https://static-maps.yandex.ru/1.x/?ll={longitude},{latitude}&z={zoom}&l={map_type}&size=400,400&pt={longitude},{latitude},pm2rdl'

    response = requests.get(request_url)
    response.raise_for_status()

    img = Image.open(BytesIO(response.content))
    img.show()

def play_guess_the_city_game():
    shuffled_cities = random.sample(cities, len(cities))

    for city in shuffled_cities:
        print(f'Угадай город')
        get_city_map(city, city_coordinates[city])
        input('Нажмите Enter, чтобы продолжить...')
        print(f'Этот город: {city}')

if __name__ == '__main__':
    play_guess_the_city_game()
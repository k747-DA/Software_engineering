import sys
import requests
import json

api_key = 'поставте свой ключ' # !!! если кто-то будет ее использовать


def get_coordinates_by_address(address):
    geocoder_url = 'https://geocode-maps.yandex.ru/1.x/'

    params = {
        'apikey': api_key,
        'geocode': address,
        'format': 'json'
    }

    response = requests.get(geocoder_url, params=params)
    response.raise_for_status()

    json_data = response.json()
    coordinates = json_data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    return tuple(map(float, coordinates.split()))

def get_district_by_coordinates(coordinates):

    response = requests.get(f'https://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode={coordinates[0]},{coordinates[1]}&kind=district&format=json')
    response.raise_for_status()

    json_data = response.json()
    data = json_data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components']
    district = f'{data[-1]}'

    json_data = json.loads(district.replace("'", "\""))

    name_value = json_data.get('name')
    return name_value

if __name__ == '__main__':
    address = input('Введите адрес: ')

    try:
        coordinates = get_coordinates_by_address(address)
        district = get_district_by_coordinates(coordinates)
        print(f'Координаты адреса {address}: {coordinates}')
        print(f'Район: {district}')
    except Exception as e:
        print(f'Произошла ошибка: {e}')

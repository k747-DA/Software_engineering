import requests
from geopy.distance import geodesic


def find_nearest_address(target_coord, coords, addresses):
    nearest_coord = min(coords, key=lambda coord: geodesic((target_coord['lat'], target_coord['lon']),
                                                           (coord['lat'], coord['lon'])).kilometers)
    index = coords.index(nearest_coord)
    return addresses[index]


def get_2gis_coordinates(api_key, query, city):
    url = 'https://catalog.api.2gis.com/3.0/items/geocode'
    params = {
        'q': f"{city} {query}",
        'fields': 'items.point',
        'key': api_key,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        test = response.json()
        data = response.json().get('result', {}).get('items', [])[0].get('point', None)
        return data
    else:
        print(f"Ошибка при выполнении запроса. Код: {response.status_code}")
        return None


def find_nearest_pharmacy_2gis(api_key, user_address, city):
    try:
        user_coords = get_2gis_coordinates(api_key, user_address, city)

        if user_coords:
            pharmacies_url = "https://catalog.api.2gis.com/3.0/items"
            params = {
                "key": api_key,
                "point": f"{user_coords['lon']},{user_coords['lat']}",
                "radius": 500,
                "q": f'Аптека'
            }

            response = requests.get(pharmacies_url, params=params)

            if response.status_code == 200:
                data = response.json()
                items = data.get("result", {}).get("items", [])

                pharmacies_address = []
                for item in items:
                    tmp = f"{city} {item['address_name']}"
                    pharmacies_address.append(tmp)

                pharmacies_coords = []
                for pharmacies in pharmacies_address:
                    coord = get_2gis_coordinates(api_key, pharmacies, city)
                    pharmacies_coords.append(coord)

                if items:
                    nearest_address = find_nearest_address(user_coords, pharmacies_coords, pharmacies_address)
                    print(f"Ближайшая аптека к адресу '{user_input_city} {user_address}': {nearest_address}")
                    return

        print("Не удалось найти ближайшую аптеку.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    api_key_2gis = "свой ключ" # !!! поставте свой ключ если кто-то будет это использовать

    user_input_city = input("Введите город: ")
    user_input_address = input("Введите улицу и дом: ")

    find_nearest_pharmacy_2gis(api_key_2gis, user_input_address, user_input_city)
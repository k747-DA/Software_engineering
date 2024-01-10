import requests

def make_2gis_api_request(query, api_key):
    url = 'https://catalog.api.2gis.com/3.0/items/geocode'
    params = {
        'q': query,
        'fields': 'items.point',
        'key': api_key,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Ошибка при выполнении запроса. Код: {response.status_code}")
        return None

def main():
    api_key = 'введите свой ключ' # !!!если кто-то будет это читать то ведите свой ключ я его не хочу отдавать ;)

    cities_input = input("Введите список городов через запятую: ")
    cities_list = [city.strip() for city in cities_input.split(',')]

    southernmost_city = None
    southernmost_latitude = float('inf')

    for city_name in cities_list:
        result_2gis = make_2gis_api_request(city_name, api_key)

        point_2gis = result_2gis.get('result', {}).get('items', [])[0].get('point', None)
        if point_2gis:
            print(f"Координаты города {city_name}: {point_2gis}")
        else:
            print(f"Координаты для города {city_name} не найдены.")

        if point_2gis and point_2gis['lat'] < southernmost_latitude:
            southernmost_latitude = point_2gis['lat']
            southernmost_city = city_name

    if southernmost_city:
        print(f"\nСамый южный город: {southernmost_city}")
    else:
        print("\nНевозможно определить самый южный город.")

if __name__ == "__main__":
    main()

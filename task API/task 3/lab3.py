import time
from selenium import webdriver
import folium


def get_satellite_image(lat, lon, zoom=15, filename='satellite_image.png'):
    map_center = [lat, lon]
    map_object = folium.Map(location=map_center, zoom_start=zoom)

    map_html = f"{filename.split('.')[0]}.html"
    map_object.save(map_html)

    options = webdriver.EdgeOptions()
    options.use_chromium = True
    options.headless = True

    browser = webdriver.Edge(options=options)

    try:
        browser.get(f'file://{map_html}')
        time.sleep(5)
        browser.save_screenshot(filename)

    finally:
        browser.quit()


if __name__ == "__main__":
    latitude = float(input("Введите широту: "))
    longitude = float(input("Введите долготу: "))
    get_satellite_image(latitude, longitude)
    print("Спутниковый снимок сохранен в файл satellite_image.png")
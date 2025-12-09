import requests

url = "https://jsonplaceholder.typicode.com/users/5"

response = requests.get(url)

if response.status_code == 200:
    user = response.json()

    city = user["address"]["city"]
    lat = user["address"]["geo"]["lat"]
    lng = user["address"]["geo"]["lng"]

    print("Місто:", city)
    print("Координати:")
    print("   Широта (lat):", lat)
    print("   Довгота (lng):", lng)

else:
    print("Помилка:", response.status_code)

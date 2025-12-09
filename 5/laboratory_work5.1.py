import requests

url = "https://jsonplaceholder.typicode.com/users/5"

response = requests.get(url)

if response.status_code == 200:
    user = response.json()
    print("Інформація про користувача з id=5:")
    print(user)
else:
    print("Помилка:", response.status_code)

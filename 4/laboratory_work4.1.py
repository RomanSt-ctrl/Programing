import requests

url = "https://www.imdb.com/chart/top/"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/",
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    html = response.text

    with open("rating_page.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("Сторінка успішно збережена у файл rating_page.html!")
else:
    print("Помилка:", response.status_code)

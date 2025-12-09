import json
from bs4 import BeautifulSoup

with open("rating_page.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

script_tag = soup.find("script", type="application/ld+json")

data = json.loads(script_tag.string)

ratings = []

for item in data["itemListElement"]:
    rating = item["item"]["aggregateRating"]["ratingValue"]
    ratings.append(float(rating))

print("Знайдені рейтинги IMDb:")
print(ratings)

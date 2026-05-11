import requests
from bs4 import BeautifulSoup
import json

url = "https://www.shl.com/solutions/products/product-catalog/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

data = []

cards = soup.find_all("a")

for card in cards:
    title = card.get_text(strip=True)

    href = card.get("href")

    if title and href:
        item = {
            "name": title,
            "url": href,
            "description": "",
            "test_type": "Unknown"
        }

        data.append(item)

with open("catalog.json", "w") as f:
    json.dump(data, f, indent=2)
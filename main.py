#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import re
import sys

if len(sys.argv) > 1:
    area_number = int(sys.argv[1].lstrip('-'))
else:
    area_number = 1

areas = {
    1: "Otaniemi",
    2: "Helsinki Centrum",
    3: "Töölö",
    6: "Kallio",
    7: "Arabia & Kumpula",
    8: "Viikki"
}

url = f"https://folio.kanttiinit.fi/fi/area/{area_number}"

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

restaurants = soup.find_all('li', class_='restaurant')

menus = {}

print(f"Area selected: {areas.get(area_number)}\n")

for restaurant in restaurants:
    restaurant_name = restaurant.find('h3').text.strip()

    menu_items = restaurant.find_all('li')
    menu = [re.sub(r"\([^)]*\)", "", item.text).strip() for item in menu_items]

    if menu:
        menus[restaurant_name] = menu

if menus:
    for name, menu in menus.items():
        print(f"{name}:")
        for item in menu:
            print(f"  - {item}")
        print()
else:
    print("No menus for today in this area")


#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import re
import sys

if len(sys.argv) > 1:
    area_number = sys.argv[1].lstrip('-') 
else:
    area_number = "1"

url = f"https://folio.kanttiinit.fi/fi/area/{area_number}"

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

restaurants = soup.find_all('li', class_='restaurant')

restaurant_menus = {}

for restaurant in restaurants:
    restaurant_name = restaurant.find('h3').text.strip()

    menu_items = restaurant.find_all('li')
    menu = [re.sub(r"\([^)]*\)", "", item.text).strip() for item in menu_items]

    if menu:
        restaurant_menus[restaurant_name] = menu

if restaurant_menus:
    for name, menu in restaurant_menus.items():
        print(f"{name}:")
        for item in menu:
            print(f"  - {item}")
        print()
else:
    print("No menus for today in this area")


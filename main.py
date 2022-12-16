from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

def scrape(url):
    # Get the page
    page = requests.get(url)
    # Parse the page
    soup = BeautifulSoup(page.text, 'html.parser')
    all_recipes = soup.find_all('h2', class_='title')
    for recipe in all_recipes:
        print(recipe)

url = "https://www.food.com/recipe/?pn="
for i in range(1, 100):
    scrape(url + str(i))

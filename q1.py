from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import re

recipe_data = []

def scrapeData(recipe_tags, counter):
    url = 'https://www.food.com/recipe'
    ingredients=""
    instructions=""
    recipe_name = ""
    cuisine = ""


    for recipe in recipe_tags:
        data = requests.get(url+recipe['href'])
        soup = BeautifulSoup(data.text, 'html.parser')
        try:
            recipe_name = soup.find('h1', class_='recipe-title').text
        except:
            recipe_name = ""
        try:
            cuisine = soup.find('div', {'class': 'col-12 cuisine'}).text
        except:
            cuisine = ""

        ingredients_tags = soup.find_all('li', itemprop='ingredients')
        instructions_tags = soup.find_all('li', itemprop='recipeInstructions')
        for ingredient in ingredients_tags:
            ingredients+=ingredient.text.strip()+", "
        for instruction in instructions_tags:
            instructions+=instruction.text.strip()+'\n'

        recipe_data.append({
                'recipe_name':recipe_name, 
                'recipe_url': url+recipe['href'], 
                'ingredients':ingredients, 
                'instructions':instructions,
                'cuisine': cuisine
        })
        counter+=1
    return counter


if __name__ == '__main__':
    url = 'https://www.food.com/recipe'
    cntr = 0
    soup = BeautifulSoup(data.text, 'html.parser')
    recipe_tags = soup.find_all('h2', itemprop = 'title')
    cntr = scrapeData(recipe_tags, cntr)

keys = recipe_data[0].keys()

with open('recipes.csv', 'w', newline='', encoding='utf-8') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(recipe_data)


df = pd.read_csv('recipes.csv')

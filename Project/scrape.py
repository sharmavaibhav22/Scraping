import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
from nltk.corpus import stopwords

final_list = []
file_obj = open('final_file.csv', 'w')
def scrape_data(URL):
    stop_words = set(stopwords.words('english'))
    try:
        html = requests.get(URL).text
        soup = BeautifulSoup(html, 'html.parser')
        ingredients = soup.find_all('li', itemprop='ingredients')
        instructions = soup.find_all('li', itemprop='recipeInstructions')
        for ingredient in ingredients:
            ingrd_str1 = ingredient.text.replace('(', '')
            ingrd_str2 = ingrd_str1.replace(')', '')
            ingrd_str3 = ingrd_str2.replace('/', '')
            ingrd_str4 = ingrd_str3.replace('.', '')
            result = [ele.strip() for x in ingrd_str4.split(',') for ele in x.split()]
            for word in result:
                if len(word) >= 5 and word not in stop_words:
                    final_list.append(word)
        for instruction in instructions:
            instruction_str1 = instruction.text.replace('(', '')
            instruction_str2 = instruction_str1.replace(')', '')
            instruction_str3 = instruction_str2.replace('/', '')
            instruction_str4 = instruction_str3.replace('.', '')
            result = [ele.strip() for x in instruction_str4.split(',') for ele in x.split()]
            for word in result:
                if len(word) >= 5 and word not in stop_words:
                    final_list.append(word)
    except Exception as e:
        print(e)


def scrape_recipes_titles():
    try:
        for page_num in range(1, 200):
            URL = "https://www.archanaskitchen.com/recipes/page-"
            print(page_num)
            URL = URL + str(page_num)
            html = requests.get(URL).text
            soup = BeautifulSoup(html, 'html.parser')
            titles = soup.find_all('a', class_='recipe-title')
            for title in titles:
                link = 'https://www.archanaskitchen.com' + title['href']
                scrape_data(link)

    except Exception as e:
        print(e)

if __name__ == "__main__" :
    scrape_recipes_titles()
    print(final_list)
    # create dataframe and write to csv
    df = pd.DataFrame(final_list)
    df.to_csv('final_file.csv', index=False, header=False)    
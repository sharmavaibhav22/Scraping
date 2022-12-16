import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
from nltk.corpus import stopwords

final_list = []
file_obj = open('final_file.csv', 'a')

def scrape():
    URL = "https://www.thescramble.com/glossary-of-cooking-terms/"
    try:
        html = requests.get(URL)
        soup = BeautifulSoup(html.content, 'html.parser')
        terms = soup.find_all('div', class_='entry-content')
        print(terms.prettify())
    except Exception as e:
        print(e)
scrape()
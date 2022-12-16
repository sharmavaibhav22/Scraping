from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import re

df1 = pd.read_csv('recipe.csv')
df2 = pd.read_csv('recipes_1.csv')

df_ = pd.concat([df1, df2], axis=0)
df_ = df_.sample(frac=1).reset_index(drop=True)
df_.to_csv('recipe_data_final.csv',index=False)

dff = pd.read_csv('recipe_data_final.csv')

print(dff)
import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


url = 'https://www.divan.ru/category/divany-i-kresla?types%5B%5D=1&types%5B%5D=4&types%5B%5D=54'
response = requests.get(url)


df = pd.read_csv('country.csv')
df = df.set_index('date')
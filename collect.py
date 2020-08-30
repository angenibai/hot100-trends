from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen

YEAR_START = 2019
YEAR_CUR = 2020

for year in range(YEAR_START, YEAR_CUR):
    url = 'https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_' + str(year)

    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    for row in soup.find(id='bodyContent').find_all('tr'):
        print(row.contents)
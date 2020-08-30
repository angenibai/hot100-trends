from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
import re
import csv

YEAR_START = 2019
YEAR_CUR = 2020

for year in range(YEAR_START, YEAR_CUR):

    csv_rows = [['Title', 'Artist(s)', 'Artists Separately']]

    url = 'https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_' + str(year)

    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find('table', {'class':'wikitable sortable'}).tbody

    for row in table.find_all('tr'):
        if (len(row.find_all('td')) == 2):
            title_cell, artist_cell = row.find_all('td')

            title = title_cell.find('a').getText()

            artist = artist_cell.text.strip() # artists as a string
            artists_list = list(map(lambda x: x.getText(), artist_cell.find_all('a'))) # list of artists

            # create new row for the csv file
            row = [title, artist] + artists_list
            csv_rows.append(row)

    # append all rows to new csv file
    csv_name = 'hot100files/' + str(year) + '.csv'
    with open(csv_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(csv_rows)

    print(f'Collected {year}')
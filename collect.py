from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
import csv

# top 100 from 1959 onwards
YEAR_START = 1959
YEAR_CUR = 2020

for year in range(YEAR_START, YEAR_CUR):

    csv_rows = [['Rank', 'Title', 'Artist(s)', 'Artists Separately']]

    url = 'https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_' + str(year)

    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find('table', {'class':'wikitable sortable'}).tbody

    num = 1
    for row in table.find_all('tr'):

        # Handle different table formats
        cells_found = False
        if year >= 1982:
            if len(row.find_all('td')) == 2:
                title_cell, artist_cell = row.find_all('td')
                cells_found = True
        else:
            if len(row.find_all('td')) == 3:
                num_cell, title_cell, artist_cell = row.find_all('td')
                cells_found = True

        if not cells_found:
            continue

        # extract title and artist from their cells
        title = title_cell.text.strip()

        artist = artist_cell.text.strip() # artists as a string
        artists_list = list(map(lambda x: x.getText(), artist_cell.find_all('a'))) # list of artists

        # create new row for the csv file
        row = [num, title, artist] + artists_list
        csv_rows.append(row)

        num += 1
        # print(f'Title: {title}, Artist(s): {artist}', artists_list) # ! DEBUG

    # append all rows to new csv file
    csv_name = 'hot100files/' + str(year) + '.csv'
    with open(csv_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(csv_rows)

    print(f'Collected {year}')
import csv
import re

year_data = {}
tracks = {}

YEAR_START = 1959
YEAR_END = 2020

for year in range(YEAR_START, YEAR_END):
    path = f'hot100files/{year}.csv'
    with open(path) as f:
        reader = list(csv.reader(f))
        file_text = [','.join(arr) for arr in reader]
        file_text = '\n'.join(file_text[1:])
        #print(file_text)
        year_data[year] = file_text


with open('missing.csv') as f:
    reader = csv.reader(f)
    count = 0
    for row in reader:
        if count == 0:
            pass

        pattern = "\d+,"+','.join(row)
        found = False
        for year in range(YEAR_START, YEAR_END):
            if (re.search(pattern, year_data[year])):
                match_row = re.search(pattern, year_data[year]).group(0) 
                print(match_row, year)
                found = True
        
           
        count += 1

#with open('missing_2.csv') as f:
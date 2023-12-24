import requests
import pandas as pd
 
from bs4 import BeautifulSoup

import csv


"""

# get URL
page = requests.get("https://en.wikipedia.org/wiki/List_of_Inkigayo_Chart_winners_(2023)")
 
# scrape webpage
soup = BeautifulSoup(page.content, 'html.parser')
 
# display scraped data
print(soup.prettify())

soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find('table',{'class':"wikitable"})

"""


wikiurl="https://en.wikipedia.org/wiki/List_of_Inkigayo_Chart_winners_(2023)"
table_class="wikitable sortable jquery-tablesorter"
response=requests.get(wikiurl)
print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')


soup.find_all('table')
table_soup = soup.find_all('table')
filtered_table_soup = [table for table in table_soup if table.caption is not None]

required_table = None

for table in filtered_table_soup:
    if str(table.caption.string).strip() != 'Key':
        required_table = table
        break    


headers = ['Date', 'Artist', 'Song', 'Points']

rows = []

# Find all `tr` tags
data_rows = required_table.find_all('tr')

for row in data_rows:
    value = row.find_all('td')
    beautified_value = [ele.text.strip() for ele in value]
    print(beautified_value)
    # Remove data arrays that are empty
    if len(beautified_value) == 0:
        continue
    # list.append - adds the thing to the end of the list
    rows.append(beautified_value)

"""
note - for triple crown/consecutive wins, the song and artist name isnt listed. 
so make it so that if length of beautified_value is less than 5, and its not 
no show/winner, then add artist name into that row

also make this entire thing into a function so that it can be called

and maybe the input is the website URL of each music show?

"""


# print(rows)

with open('inkigayo_2023.csv', 'w', newline="") as output:
    writer = csv.writer(output)
    writer.writerow(headers)
    writer.writerows(rows)



"""


print(soup.title.string)
table=soup.find('table',{'class':"wikitable.sortable.plainrowheaders.jquery-tablesorter"})
print(table)




df=pd.read_html(str(table))
df=pd.DataFrame(df[0])
print(df.head())
"""
import requests
from bs4 import BeautifulSoup
import json
import datetime

#create timestamp
path = '-data.json'
date = datetime.datetime.now()
data = str(date) + path
newdata = "-".join( data.split() )

URL = 'https://bringatrailer.com'
page = requests.get(URL)

resultsArr = []

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.findAll('div', class_='bat_announcement')

for elem in results:
  rObject = {
    'title': elem.find('h2', attrs={'class': 'post-title'}).text,
    'comments': elem.find('div', attrs={'class': 'post-excerpt'}).text
  }

  #save to json file
  resultsArr.append(rObject)

with open(newdata, 'w') as outfile:
  json.dump(resultsArr, outfile)


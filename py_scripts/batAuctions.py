import requests
from bs4 import BeautifulSoup
import json

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
  print(resultsArr)

with open('data.json', 'w') as outfile:
  json.dump(resultsArr, outfile)


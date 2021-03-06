import requests
from bs4 import BeautifulSoup

#URL = 'https://bringatrailer.com/auctions'
URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')

job_elems = results.find_all('section', class_='card-content')

for elem in job_elems:
  title = elem.find('h2', class_='title')
  company = elem.find('div', class_='company')
  location = elem.find('div', class_='location')
  if None in (title, company, location):
    continue
  print(title.text.strip())
  print(company.text.strip())
  print(location.text.strip())
  print()


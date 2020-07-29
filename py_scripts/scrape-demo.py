from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("usr/lib/chromium-browser/chromedriver")

car=[] #list the car
price=[] #list the price of the car
comments=[] #ithink there's comments
driver.get("http://https://bringatrailer.com/auctions/")

content = driver.page_source
soup = BeautifuleSoup(content)
for a in soup.FindAll('a',href=True, attrs={'class':'data-listing'}):
  name=a.find('h3', attrs={'class':'auctions-item-title'})
  price=a.find('strong', attrs={'class':'auctions-item-meta-value'})
  comments=a.find('div', attrs={'class':'auctions-item-excerpt'})
  car.append(name.text)
  price.append(price.text)
  comments.append(comments.text)

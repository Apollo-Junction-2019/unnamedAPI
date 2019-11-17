import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'http://ithare.com/internet-technology-glossary-for-kids/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')
content = soup.find(class_='entry-content')

all_entries = content.findAll('li')
entry_name = all_entries.findAll('a')
print(entry_name.text())

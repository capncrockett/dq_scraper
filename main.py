import requests
from bs4 import BeautifulSoup


response = requests.get('http://dataquestio.github.io/web-scraping-pages/simple.html')
content = response.content

parser = BeautifulSoup(content, 'html.parser')


import requests
from bs4 import BeautifulSoup

response = requests.get('https://editorial.rottentomatoes.com/guide/2021-best-movies/')
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Find the number one movie
something = parser.select('#row-index-1')
print(something)

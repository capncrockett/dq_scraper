import requests
from bs4 import BeautifulSoup


response = requests.get('http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html')
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Select all of the elements that have the first-item class.
first_items = parser.select(".first-item")

# Print the text of the first paragraph (the first element with the first-item class).
print(first_items[0].text)

first_outer_text = parser.select(".outer-text")[0].text
print(first_outer_text)

second_text = parser.select("#second")[0].text
print(second_text)


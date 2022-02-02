import requests
from bs4 import BeautifulSoup


# Get the Superbowl box score data.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/2014_super_bowl.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Find the number of turnovers the Seahawks committed.
turnovers = parser.select("#turnovers")[0]
seahawks_turnovers = turnovers.select("td")[1]
seahawks_turnovers_count = seahawks_turnovers.text
print(seahawks_turnovers_count)

patriots_total_plays_count = parser.select("#total-plays")[0].select("td")[2].text
print(patriots_total_plays_count)

seahawks_total_yards_count = parser.select("#total-yards")[0].select("td")[1].text
print(seahawks_total_yards_count)

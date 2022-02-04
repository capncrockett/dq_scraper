import requests
from bs4 import BeautifulSoup

response = requests.get('https://editorial.rottentomatoes.com/guide/2021-best-movies/')
content = response.content
soup = BeautifulSoup(content, 'html.parser')


# This is it! It needs the full path of selectors. Returns ResultSet, thus needs index.
number_10 = soup.select('body #row-index-10 h2 a')[0].text
# print(number_10)


for i in range(5):
    movie_title = soup.select(f"body #row-index-{i + 1} h2 a")[0].text
    print(movie_title)


# EVERYTHIING BELOW IS FOR REFERENCE

# Find the number one movie
# movie = soup.select('#row-index-1')
# print(type(movie))

title = soup.select("title")
# print(title)
# [<title>  The Best Movies of 2021 – Best New Films of the Year &lt;&lt; Rotten Tomatoes – 
# Movie and TV News</title>]

thing_3 = soup.select("p:nth-of-type(3)")
# print(thing_3)
# [<p>Movies achieve...reviews to 
# be <a href="https://editorial.rottentomatoes.com/article/top-critics-program-just-got-an-upgrade/"><u>published 
# by Top Critics</u></a>. Once...dropping below 70%.</p>]

body_a_thing = soup.select("body a")
# print(body_a_thing)
# <a href="http://www.fandango.com/terms-and-policies/" id="footer-tos">Terms and Policies</a>, 
# <a href="http://www.aboutads.info/choices" id="footer-ad-choices">Ad Choices</a>, 
# <a class="footerLinks" href="http://www.fandango.com/terms">Terms of Service</a>, 
# <a class="footerLinks" href="http://www.fandango.com/privacy">Privacy Policy</a>]

last_link_text = soup.select("body a")[-1].text
# print(last_link_text)
# Privacy Policy

page_title = soup.select("html head title")
# print(page_title)
# [<title>  The Best Movies of 2021 – Best New Films of the Year &lt;&lt; Rotten Tomatoes – Movie and TV News</title>]

head_title = soup.select("head > title")
# print(head_title)
# [<title>  The Best Movies of 2021 – Best New Films of the Year &lt;&lt; Rotten Tomatoes – Movie and TV News</title>]

# Select first `a` tag inside first `p` tag.
first_p_first_a = soup.select("p > a")
# print(first_p_first_a)
# [<a href="https://editorial.rottentomatoes.com/article/top-critics-program-just-got-an-upgrade/"><u>published by Top Critics</u></a>]

# Select 2nd `a` tag inside first `p` tag.
first_p_second_a = soup.select("p > a:nth-of-type(2)")
# print(first_p_second_a)
# prints empty list because there is no 2nd `a` in the first `p`.
# []

# Returns id="link1" inside first `p` tag.
first_p_link_1 = soup.select("p > #link1")
# print(first_p_link_1)
# Empty because there is no `id="link1"`
# []

# Find siblings of tags ??? Not sure about this one.
sibling_tag = soup.select("#row-index-227 ~ .row countdown-item")
# print(sibling_tag)


# Find tags by CSS class:
countdown_index = soup.select(".countdown-index")[-1]
# print(countdown_index)
# <div class="countdown-index">#1</div>

# Top 5 tomato scores.
tom_score = soup.select("[class~=tMeterScore]")[:-6:-1]
# print(tom_score)
# [<span class="tMeterScore">100%</span>, 
# <span class="tMeterScore">98%</span>, 
# <span class="tMeterScore">100%</span>, 
# <span class="tMeterScore">100%</span>, 
# <span class="tMeterScore">99%</span>]

# Find tags by ID:
row_index_10 = soup.select("#row-index-10")
# print(row_index_10)

# I guess you can also specify the target tag.
number_10_row = soup.select("div#row-index-10")
# print(number_10_row)

# Find tags that match any selector from a list of selectors:
rows_10_and_20 = soup.select("#row-index-10,#row-index-20")
# print(rows_10_and_20)

title_10 = soup.select("#row-index-10 a:nth-of-type(3)")
# print(title_10)








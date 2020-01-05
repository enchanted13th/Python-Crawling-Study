import requests
from bs4 import BeautifulSoup as BS

res = requests.get('http://v.media.daum.net/v/20170615203441266')

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# print(res.content)

# soup = BS(res.content, 'html.parser')
soup = BS(html_doc, 'html.parser')

# title = soup.find('title')
# print(title.get_text())

# print(soup.prettify())
print(soup.title)
print(soup.title.string)
print(soup.title.parent.name)

print('--------------------------')
print(soup.p)
print(soup.find_all('a'))
print(soup.get_text())

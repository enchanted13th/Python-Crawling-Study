# 네이버 실시간 검색어 크롤링

import requests
from bs4 import BeautifulSoup as BS

req = requests.get('http://www.naver.com/')
source = req.text
soup = BS(source, 'html.parser')

top_list = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k')

for top in top_list :
    print(top.text)

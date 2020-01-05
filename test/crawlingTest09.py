from selenium import webdriver as webDriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup as BS
import requests
import time

# selenium 을 통한 네이버 로그인
driver = webDriver.Chrome('../chromedriver/chromedriver')
driver.get('https://nid.naver.com/nidlogin.login')

wait = WebDriverWait(driver, 30)

id = ''
pw = ''

driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
time.sleep(1)

driver.get('https://cafe.naver.com/joonggonara?iframe_url=/ArticleList.nhn%3Fsearch.clubid=10050146%26search.menuid=334%26search.boardtype=L')
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "gm-tcol-c b")))

title_group = driver.find_element_by_class_name("gm-tcol-c b")

print(title_group)

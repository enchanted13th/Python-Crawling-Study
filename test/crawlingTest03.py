from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('../chromedriver/chromedriver')
driver.get('https://nid.naver.com/nidlogin.login')

usr = ''
pwd = ''

driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
time.sleep(1)

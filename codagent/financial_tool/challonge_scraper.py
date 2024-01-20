# Scrape our challonge data

# imports 
# import requests 
# from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import requests


# MY_CHROME_LOCATION = '/usr/bin/google-chrome'
FIREFOX_LOCATION = '/usr/bin/firefox'

BASE_URL = "https://challonge.com/users/esportsagent/tournaments"


# res = requests.get(BASE_URL)
# 
# test = BeautifulSoup(res.content, 'html5lib') 
# test2 = test.find('table')
# 
# print(test)

driver_options = Options()

# driver_options.headless = True
driver_options.set_preference('permissions.default.image', 2)
driver_options.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')

print('Trying to open firefox....')
driver = webdriver.Firefox(options=driver_options)
print('Firefox is open')

# go to our tournaments page 
driver.get(BASE_URL)
print(driver.current_url)
print(driver.title)

print('Trying to close firefox....')
driver.quit()
print('Firefox is closed')

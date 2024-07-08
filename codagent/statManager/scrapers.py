# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re



# doing breakingpoint for now
class webScraper:

    def __init__(self, driver, baseLink):
        self.driver = driver
        self.baseLink = baseLink
    
    # Not sure if this gets completed matches yet.  gets some matches tho 
    def getCompletedMatchLinks(self):
        driver = self.driver
        matchesLink = self.baseLink + '/matches'
        driver.get(matchesLink)

        aTags = driver.find_elements(By.XPATH, '//a')
        matchLinks = []
        for aTagIdx, aTag in enumerate(aTags):
            linkFromTag = aTag.get_attribute('href')

            if 'match/' in linkFromTag and not('?' in linkFromTag):
                matchLinks.append(linkFromTag)
        return matchLinks
    
    # LEFT OFF HERE
    def getStatsFromMatch(self, matchLink):
        driver = self.driver
        driver.get(matchLink)

        # tdTags = driver.find_elements(By.XPATH, '//td')
        # for tdTagIdx, tdTag in enumerate(tdTags):
        #     print(tdTag)

        # THIS IS THE TAB LIST 
        tabList = driver.find_elements(By.XPATH, '//button[@role="tab"]')
        # THESE ARE THE DIVS OF THE TAB TABLES (Overview, Map 1, etc.)
        tabDivs = driver.find_elements(By.XPATH, '//div[@role="tabpanel"]')
        # THIS IS THE TABLE 
        # testDiv = driver.find_elements(By.XPATH, '//table[@class="mantine-Table-root mantine-1c7s4d6"]')
        # print(testDiv)

        testing = tabDivs[1].find_elements(By.TAG_NAME, 'td')
        print(testing)
        # for tabIdx, tab in enumerate(tabList):
        #     # driver.implicitly_wait(10)
        #     tabDiv = tabDivs[tabIdx]
        #     # print(tabDiv)
        #     print(tabDiv.text)





options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
bpScraper = webScraper(driver, 'https://www.breakingpoint.gg')

bpScraper.getStatsFromMatch('https://www.breakingpoint.gg/match/27350/Los-Angeles-Guerrillas-vs-Las-Vegas-Legion-at-CDL-Major-4-Qualifier-2024')

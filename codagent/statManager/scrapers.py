# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re



# doing breakingpoint for now
class breakingPointScraper:

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

        tdTags = driver.find_elements(By.XPATH, '//td')
        for tdTagIdx, tdTag in enumerate(tdTags):
            print(tdTag)





options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
bpScraper = breakingPointScraper(driver, 'https://www.breakingpoint.gg')

bpScraper.getStatsFromMatch('https://www.breakingpoint.gg/match/27350/Los-Angeles-Guerrillas-vs-Las-Vegas-Legion-at-CDL-Major-4-Qualifier-2024')

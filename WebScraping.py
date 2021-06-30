from selenium import webdriver
# selenium is used to interact with webpages (like automation testing)
from bs4 import BeautifulSoup
# BeautifulSoup is used for parsing text as html
import time,csv

url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome('/Users/samay/Desktop/SAMAY THE AWESOME IV ONLINE LEARNING TAKES OVER THE WORLD/Coding/Whitehat jr./PYTHON/programs/Virtual environment programs/venv/chromedriver.exe')
browser.get(url)

time.sleep(10)

def Scrape():
    headers = ['NAME','DISTANCE', 'MASS', 'RADIUS']
    starData = []
    Soup = BeautifulSoup(browser.page_source,"html.parser")
    for tag in Soup.find_all('th',attrs={'class','headerSort'}):
        litags = tag.find_all('tr')
        tempList = []
        for index,tag in enumerate(litags):
            if index==0:
                tempList.append(tag.find_all('a')[0].contents[0])
            else:
                try:
                    tempList.append(tag.contents[0])
                except:
                    tempList.append('')
        starData.append(tempList)



    with open('ScrapeData.csv','w') as f:
        cw = csv.writer(f)
        cw.writerow(headers)
        cw.writerows(starData)

Scrape()
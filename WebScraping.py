from bs4 import BeautifulSoup
# BeautifulSoup is used for parsing text as html
import time,csv,requests,pandas

url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
page = requests.get(url)

Soup = BeautifulSoup(page.text,"html.parser") 
table = Soup.find('table')
temp = []
rows = table.find_all('tr')

for tr in rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp.append(row)

names = []
d = []
m = []
r = []
l = []

for i in range(1,len(temp)):
    names.append(temp[i][1])
    d.append(temp[i][3])
    m.append(temp[i][5])
    r.append(temp[i][6])
    l.append(temp[i][7])

df = pandas.DataFrame(list(zip(names,d,m,r,l)),columns = ['starname','distance','mass','radius','luminosity'])
df.to_csv("ScrapeData.csv")
Scrape()

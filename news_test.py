import requests
from bs4 import BeautifulSoup
# Scraping the first 5 articles
url = 'https://www.nrk.no/nyheter/'
page = requests.get(url) #war r1
coverpage = page.content
soup = BeautifulSoup(page.content, "html.parser")

headlines = soup.find_all('h2', class_= 'bulletin-title')
print(len(headlines))
print(headlines[0].get_text())
news =[]
info = soup.find_all('p')
for i in range(5):
    info[i] = info[i].get_text()
    info[i] = info[i].strip()
    info[i] = info[i].replace('–','')
    if len(info[i]) <= 4:
        pass
    else:
        news.append(info[i])
    
print(news)

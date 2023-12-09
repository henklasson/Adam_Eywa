#A collection of functions that will execute some sort of command given a certain set of input. 
#Typically go to a website and retreive some info
#___________________________________________________________________________________________________________
import geocoder
from geopy.geocoders import Nominatim
from bs4 import BeautifulSoup
# Beautifulsoup A library that provides tools for web scraping HTML and XML documents.
import requests
#A library that provides HTTP request functionality, allowing the script to retrieve web pages.   

from difflib import SequenceMatcher
import itertools
import numpy as np

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()    
    
    
def weather():
    #Needs to be fixed, fake location. 
    #And only temperature works. 

    #yr_location = location[-3]
    yr_location = "Asker"

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0'
    }
    url = f"https://www.google.com/search?q=weather+{yr_location}"
    response = requests.get(url, headers=headers)
    html_text = response.text
    soup = BeautifulSoup(html_text, 'lxml')
    temp = soup.find_all('span', class_='wob_t q8U8x')
    for item in temp:
        #print(item.text)
        temp = item.text

    # sky = soup.find_all('g-img', class_='uW5pk')
    # for sikt in sky:
    #     sikt = sikt.get('alt')
    # print(type(sikt))
        
    temp = int(temp)
    if temp <= 10:
        print(f"Kle deg godt, det er {temp} grader kaldt.")
    elif temp >10 and temp <=20:
        print(f"Du bør ha med deg en genser, det er meldt {temp} grader idag.")
    elif temp > 20:
        print(f"Idag er det varmt, {temp} grader. T-skjorte kommer holde!")
    else:
        print("Noe gikk galt, kontakt NeuralMet for kundestøtte.")
    
    # if sikt.lower() == "sol":
    #     print("Blå himmel og sol idag!")
    # elif sikt.lower() == "skyet":
    #     print("Overskyet i dag.")
    # elif sikt.lower() == "delvis skyet":
    #     print("Det vil bli delvis skyet idag.")
    # elif sikt.lower() == "byger":
    #     print("Husk paraplyen din, det kan regne idag!")
    # elif sikt.lower() == "snøbyger":
    #     print("Det er meldt snøfall idag.")
    # elif sikt.lower() == "for det meste skyet":
    #     print("La solbrillene ligge hjemme!")
    # elif sikt.lower() == "regn":
    #     print("Husk paraplyen din! Det er meldt regn!")
    # elif sikt.lower() == "regn og snø":
    #     print('Det kommer til å sludde idag, så husk å bruke vanntette sko.')
    # elif sikt.lower() == "lette regnbyger":
    #     print("Husk jakke idag, det kan regne noe i løpet av dagen.")
    # else:
    #     print("Noe gikk galt, kontakt NeuralMet for kundestøtte.")
        



def news_global():
    pass

def econ_news():
    pass
    url='https://e24.no/'
    response = requests.get(url)
    list_of_headlines = []
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h3')
    for x in headlines:
        list_of_headlines.append(x.text.strip())
    return list_of_headlines

def news_norway():
    url = 'https://www.nrk.no/nyheter/'
    page = requests.get(url) #war r1
    coverpage = page.content
    soup = BeautifulSoup(page.content, "html.parser")

    headlines = soup.find_all('h2', class_= 'bulletin-title')
    
    news =[]
    headlines_list = []
    info = soup.find_all('p')
    for i in range(5):
        headlines[i] = headlines[i].get_text()
        info[i] = info[i].get_text()
        info[i] = info[i].strip()
        info[i] = info[i].replace('–','')
        if len(info[i]) <= 4:
            pass
        else:
            news.append(info[i])
            headlines_list.append(headlines[i])
    return news, headlines_list
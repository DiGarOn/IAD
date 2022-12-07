import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Freaks_and_Geeks'
response = requests.get(url)

soup = BeautifulSoup(response.text)

list_per_episode = []

for data_per_episode in soup.find_all('tr', {'class': 'vevent'}):
    number = data_per_episode.find('th').get_text().strip()
    title = data_per_episode.find('td', {'class': 'summary'}).get_text().strip()
    director = data_per_episode.find('td', {'style':'text-align:center'}).get_text().strip()
    try:
        link = data_per_episode.find('td', {'style':'text-align:center'}).find("a").get('href')
        link = "https://en.wikipedia.org" + link
    except:
        link = None
    list_per_episode.append([number, title, director, link])

titles = ["Number", "Title", "Director", "Ref"]
df = pd.DataFrame(list_per_episode, columns = titles)
df.to_csv("Freaks_and_Geeks.csv", encoding = 'utf-16', index = False)

from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movie/Titanic-120338'
response = requests.get(website)
content = response.text

soup = BeautifulSoup(content, 'lxml')

box = soup.find('article', class_='main-article')
title = box.find('h1').get_text()
element = soup.find('p', {'class': 'cue-line', 'data-cue-idx': '2081'})
transcript = soup.find('div', id='cue-app').get_text(strip=True, separator=' ')

with open(f'{title}.txt', 'w') as file:  # title + .txt
    file.write(transcript)


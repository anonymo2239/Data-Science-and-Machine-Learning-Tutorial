from bs4 import BeautifulSoup
import requests

root = 'https://subslikescript.com'
website = root + '/movies/'
response = requests.get(website)
content = response.text
soup = BeautifulSoup(content, 'lxml')

box = soup.find('article', class_='main-article')
link_list = box.find_all('a', href=True)  # get_text vs. yazamam çünkü href True yaptım.

links = []
for link in link_list:
    link['href'] = root + link['href']
    links.append(link['href'])

for link in links:
    website = link
    response = requests.get(website)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')
    box = soup.find('article', class_='main-article')
    title = box.find('h1').get_text()
    transcript = box.find('div', id='cue-app').get_text(strip=True, separator='\n')

    with open(f'{title}.txt', 'w', encoding="utf-8") as file:
        file.write(transcript)

# BeautifulSoup ile pagination yapmak istiyorsan kurstaki videoya bakabilirsin


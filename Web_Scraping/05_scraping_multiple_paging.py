from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movies/'
response = requests.get(website)
content = response.text
soup = BeautifulSoup(content, 'lxml')



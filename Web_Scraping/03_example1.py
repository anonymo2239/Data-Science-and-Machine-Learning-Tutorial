from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movie/Titanic-120338'
response = requests.get(website)
content = response.text

soup = BeautifulSoup(content, 'lxml')
# Buraya kadar HTML kodunu cekmis olduk

# print(soup.prettify())  # cikti daha guzel gozuksun diye

box = soup.find('article', class_='main-article')  # tag_name, class_name yaziyoruz.(cok onemli kullanim!!)
# box sadece o <article class="main-article"> içindeki <h1> etiketini bulmamıza yardımcı oluyor.
title = box.find('h1').get_text()
# Eğer sayfada birden fazla <h1> varsa, yalnızca ilkini döndürürdü ve diğerlerini göz ardı ederdi.
print(title)
element = soup.find('p', {'class': 'cue-line', 'data-cue-idx': '2081'})
print(element.text)
# ya sonuna get_text yaz ya da elemanın yanına.text yaz

# ONEMLI NOT: bu çıktıyı excel e aktarırken satırlar arası boşluk olduğu için excel dosyasında işler
# karmaşıklaşabiliyor. Bunun için get_text methodunun içine strip metodunu eklemeliyiz.
transcript = soup.find('div', id='cue-app').get_text(strip=True, separator=' ')
print(transcript)



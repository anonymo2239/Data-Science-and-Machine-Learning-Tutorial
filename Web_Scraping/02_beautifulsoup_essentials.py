from bs4 import BeautifulSoup  # for scraping
import requests  # web sitelerine request atmak için
# ayrıca lxml indirdik çünkü beautifulsoup un kendi parser i yok.

# Adımlar:
# 1) Fetch the Pages
result = requests.get("https://www.google.com")  # o sayfaya request attık.

# 2) Page Content
content = result.text
# print(content)  # tüm html içeriğini vermiş oldu

# 3) Create Soup
soup = BeautifulSoup(content, "lxml")
# soup nesnesi ile HTML yapısını gezebiliriz. HTML belgesindeki etiketler, nitelikler ve metinler gibi öğelere
# erişmek için ağaç yapısını gezebiliriz.
# Örnek: soup.find("title") komutu, <title> etiketinin ilkini döndürecektir.

print(soup.find(id="spch-dlg"))  # id'sini kullanarak o elementin bilgilerini çektik.
soup.find('tag', class_="class_name")  # sınıf adı ile bulma

print(soup.find_all("h1"))  # tüm h1 elemanlarını çeker


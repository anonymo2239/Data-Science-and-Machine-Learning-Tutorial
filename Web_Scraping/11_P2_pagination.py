import chromedriver_autoinstaller
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Headless mode, tarayıcıyı görsel arayüz olmadan (arka planda) çalıştıran bir moddur.
# Daha hızlı çalışır çünkü görsel öğeleri yüklemez.
# Sistem kaynaklarını daha az tüketir.
# Sunucuda çalıştırılabilir
# options = Options()
# options.add_argument("--headless")  # Burada aktif ediyoruz.
# options.add_argument('window-size=1920x1080')  # zounlu degil eklenebilir
# simdilik kullanmaya gerek yok
chromedriver_autoinstaller.install()

web = "https://www.audible.com/search"
# driver = webdriver.Chrome(options=options)  # headless mode için
driver = webdriver.Chrome()
driver.get(web)
# driver.maximize_window()  # headless mode calisirken guzel calismaz

pagination = driver.find_element(By.XPATH, '//ul[contains(@class, "pagingElements")]')
pages = pagination.find_elements(By.TAG_NAME, 'li')
last_page = int(pages[-2].text)  # son sayfanin numarasini aldik
current_page = 1

book_title = []
book_author = []
book_length = []

while current_page <= last_page:
    # implicit(örtük, görünmeyen) weight
    # time.sleep(2)

    # explicit(açık, müstehcen) waiting
    container = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]'
                                                                                         '/div[5]/div[5]/div/div[2]/'
                                                                                         'div[4]/div/div/div/span[2]/ul')))
    products = container.find_elements(By.XPATH, "./li")  # find_elements bir liste
    # döndürür ve loop ile listeyi gezeriz.

    for product in products:
        book_title.append(product.find_element(By.XPATH, './/h3[contains(@class, "bc-heading")]').text)
        book_author.append(product.find_element(By.XPATH, './/li[contains(@class, "authorLabel")]').text)
        book_length.append(product.find_element(By.XPATH, './/li[contains(@class, "runtimeLabel")]').text)

    current_page += 1
    try:
        next_page = driver.find_element(By.XPATH, '//span[contains(@class, "nextButton")]')
        next_page.click()
    except:
        pass

book_sheet = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
book_sheet.to_csv('bookList.csv', index=False)

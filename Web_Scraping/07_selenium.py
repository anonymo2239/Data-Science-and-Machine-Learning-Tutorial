# Bir web sitesini taramak için selenium gerekip gerekmediğini öğrenmek istediğinizde,
# JavaScript'i devre dışı bırakın(sağ üst ayarlar > disable javascript) ve sonra web
# sitesinin istediğiniz verileri yüklemek için JavaScript'e ihtiyacı olup olmadığına bakın.
import time

from selenium import webdriver
from selenium.webdriver.common.by import By  # tag'i daha düzenli almamızı sağlıyor.
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()  # sürüm değişikliği olursa otomatik olarak güncelliyor

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://yandex.com/")
# eleman görünene kadar maksimum 4 saniye bekle

# Google search bar ı bulmak (Full xpath yöntemi kullanılabilir)
# input_element_by_id = driver.find_element(By.ID, "APjFqb")
input_element_by_name = driver.find_element(By.NAME, "text")
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME, "text")))
# input_element_by_x_path = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
# print(input_element_by_id)
# print(input_element_by_name)
# print(input_element_by_x_path)

input_element_by_name.send_keys("adem alperen arda")

search_button = driver.find_element(By.CSS_SELECTOR, ".search3__button.mini-suggest__button")
WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".search3__button.mini-suggest__button")))
search_button.click()

time.sleep(10)



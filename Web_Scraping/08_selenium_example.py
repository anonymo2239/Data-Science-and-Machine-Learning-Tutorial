import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By  # tag'i daha düzenli almamızı sağlıyor.
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://atilsamancioglu.com")

student_page = driver.find_element(By.CSS_SELECTOR, "#menu-item-166 > a")
WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#menu-item-166 > a")))
student_page.click()

read_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/main/article[1]/div/p[2]/a")
read_button.click()

article_list = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/aside[4]")
print(len(article_list.text.splitlines()))


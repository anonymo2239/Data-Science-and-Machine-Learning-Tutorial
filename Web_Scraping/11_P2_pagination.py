from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

web = "https://www.audible.com/search"
driver = webdriver.Chrome()
driver.get(web)

driver.maximize_window()

container = driver.find_element(By.CLASS_NAME, "adbl-impression-container ")
container.find_element(By.XPATH, "")


from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import Select
import time

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.get("https://www.adamchoi.co.uk/overs/detailed")

all_matches = driver.find_element(By.XPATH, "//label[@analytics-event='All matches']")
all_matches.click()

dropdown = Select(driver.find_element(By.ID, "country"))
dropdown.select_by_visible_text('Turkey')
time.sleep(2)

matches = driver.find_elements(By.TAG_NAME, "tr")

date = []
home_team = []
score = []
away_team = []

for match in matches:
    if 'Next match' not in match.text:
        date_match = match.find_element(By.XPATH, "./td[1]").text
        date.append(date_match)
        home = match.find_element(By.XPATH, "./td[3]").text
        home_team.append(home)
        scoreboard = match.find_element(By.XPATH, "./td[4]").text
        score.append(scoreboard)
        away = match.find_element(By.XPATH, "./td[5]").text
        away_team.append(away)

matchesFrame = pd.DataFrame({'Tarih': date, 'Ev Sahibi Takım': home_team, 'Maç Sonucu': score, 'Konuk Takım': away_team})
matchesFrame.to_csv('football_data.csv', index=False)
print(matchesFrame)


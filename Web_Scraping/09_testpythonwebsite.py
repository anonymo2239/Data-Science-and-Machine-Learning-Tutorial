import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()


class TestPythonWebsite(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://pypi.org/")
        self.assertIn("PyPI", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("selenium")
        elem.send_keys(Keys.RETURN)
        assert "There were no results for" not in driver.page_source

    def tearDown(self) -> None:
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

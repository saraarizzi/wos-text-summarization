from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Scraper:
    def __init__(self):
        self.driver = self.__setup_driver()

    def __setup_driver(self):
        d = webdriver.Chrome()
        return d

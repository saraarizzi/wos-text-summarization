import time

from scraper import Scraper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


URL = "https://quillbot.com/summarize"


class QuillBot(Scraper):

    def __init__(self):
        super().__init__()
        self.delay = 30

    def summarize(self, lst):

        # get url
        self.driver.get(URL)
        self.driver.maximize_window()

        # wait for button to decline biscuits from strangers
        WebDriverWait(self.driver, self.delay).until(
            EC.presence_of_element_located((By.ID, "onetrust-group-container")))
        self.driver.find_element(By.ID, "onetrust-reject-all-handler").click()

        for idx, abstract in enumerate(lst):

            input_box = self.driver.find_element(By.ID, "inputBoxSummarizer")
            input_box.send_keys(abstract)

            time.sleep(3)

            WebDriverWait(self.driver, self.delay).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='MuiGrid-root css-rfnosa']")))
            div = self.driver.find_element(By.XPATH, "//div[@class='MuiGrid-root css-rfnosa']")

            WebDriverWait(div, self.delay).until(
                EC.presence_of_element_located((By.XPATH, "//button[@data-testid='summarize-button']")))
            div.find_element(By.XPATH, "//button[@data-testid='summarize-button']").click()

            WebDriverWait(self.driver, self.delay).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Paraphrase Summary')]")))
            summary = self.driver.find_element(By.ID, "outputBoxSummarizer").text

            with open("data/summaries5736.txt", "a") as summaries:
                summaries.write(f"[{idx}] {summary}\n")

            input_box.clear()

            time.sleep(10)


if __name__ == "__main__":

    f = open("data/WebOfScience/WOS5736/X.txt", "r")
    abstracts_str = f.read()
    abstracts_list = abstracts_str.split("\n")

    QuillBot().summarize(abstracts_list)

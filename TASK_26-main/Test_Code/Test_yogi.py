from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from Test_Data import Data
import pytest




class Test_code:
    url = "https://www.imdb.com/search/name/"

    # method for running python tests
    @pytest.fixture()
    def home_page(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.close()

    def test_box(self,home_page):
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        wait = WebDriverWait(self.driver,20,1)
        web_ele = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,Data.Webpage_Data.search_xpath))
        )
        web_ele.send_keys(Data.pass_text().Text)
        action = ActionChains(self.driver)
        action.move_to_element(web_ele).perform()
        action.click()

        self.driver.quit()

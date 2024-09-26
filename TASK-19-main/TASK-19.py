from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager import chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException
class Guvi:
   def __init__(self):
       self.url="https://www.saucedemo.com/"
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

   def click_login_button(self):
       try:
           self.driver.maximize_window()
           self.driver.get(self.url)
           sleep(10)
       except NoSuchElementException as selenium_error:
           print(selenium_error)


   def login(self):
       try:
           sleep(10)
           self.driver.find_element(by=By.ID, value="user-name").send_keys("standard_user")
           self.driver.find_element(by=By.ID, value="password").send_keys("secret_sauce")
           self.driver.find_element(by=By.ID, value="login-button").click()
       except NoSuchElementException as selenium_error:
           print(selenium_error)
       finally:
           self.driver.close()


page = Guvi()


page.click_login_button()


page.login()

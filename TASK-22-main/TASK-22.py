from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.instagram.com/guviofficial/")
sleep(5)

followers = driver.find_element(By.XPATH, '//ul/li[2]/button/span/span').text

print("Guvi Followers: ", followers)

sleep(5)

following = driver.find_element(By.XPATH, '//ul/li[3]/button/span/span').text

print("Guvi Following: ", following)

sleep(2)

driver.quit()



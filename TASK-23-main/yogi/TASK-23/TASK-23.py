from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://jqueryui.com/droppable/")

# select frame XPATH
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))
sleep(2)
# select the ID and XPATH,CSS selectors
elem1 = driver.find_element(By.ID, "draggable")
sleep(2)
elem2 = driver.find_element(By.ID, "droppable")
sleep(2)

# drag and drop off_set work

# ActionChains(driver).drag_and_drop(elem1,elem2).perform()
ActionChains(driver).drag_and_drop_by_offset(elem1, 168, 18).perform()
sleep(4)

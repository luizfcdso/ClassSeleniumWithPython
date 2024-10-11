import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()

#driver.get('https://demo.automationtesting.in/Static.html')
driver.get('https://rahulshettyacademy.com/AutomationPractice/')


action = ActionChains(driver)

# source = driver.find_element(By.XPATH, "//img[@id='node']")
# target = driver.find_element(By.XPATH, "//div[@id='droparea']")
#
# action.drag_and_drop(source, target).perform()
#
# #Just to you see it working
# time.sleep(10)

action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
#action.context_click(driver.find_element(By.LINK_TEXT, 'Top')).perform() #RightClick

action.move_to_element(driver.find_element(By.LINK_TEXT, 'Reload')).click().perform()




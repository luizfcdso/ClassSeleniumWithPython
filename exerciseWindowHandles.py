import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.XPATH, "//a[@class='blinkingText']").click()
windowOpened = driver.window_handles

driver.switch_to.window(windowOpened[1])
textGrabbed = driver.find_element(By.XPATH, "//p[@class='im-para red']").text

partOfTheText = textGrabbed.split()
emailGrabbed = partOfTheText[4]
driver.switch_to.window(windowOpened[0])
driver.find_element(By.XPATH, "//input[@id='username']").send_keys(emailGrabbed)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("123456")

driver.find_element(By.XPATH, "//input[@id='signInBtn']").click()
time.sleep(2)
print(driver.find_element(By.XPATH, "//div[@class='alert alert-danger col-md-12']").text)





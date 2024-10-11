import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/iframe")
#pode usar o nome do frame ou o ID
driver.switch_to.frame("mce_0_ifr")
time.sleep(10)

#using explicit wait to ensure the element is present and interactable
tinymce_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "tinymce"))
)


driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am able to use frame over here")

driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)


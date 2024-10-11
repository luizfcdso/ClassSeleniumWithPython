import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option1":
        checkbox.click()
        assert checkbox.is_selected()
        break

radioButtons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radioButtons[2].click()
assert radioButtons[2].is_selected()

assert driver.find_element(By.XPATH, "//input[@id='displayed-text']").is_displayed()
driver.find_element(By.XPATH, "//input[@id='hide-textbox']").click()
assert  not driver.find_element(By.XPATH, "//input[@id='displayed-text']").is_displayed()

driver.find_element(By.XPATH, "//input[@id='displayed-text']").send_keys("Luiz Fernando")

time.sleep(3)






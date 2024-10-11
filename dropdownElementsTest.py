import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

searchField = driver.find_element(By.ID, "autosuggest")
searchField.send_keys("ind")

time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

selected = searchField.get_attribute("value")
print(selected)
assert selected == "India"






import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)

driver.get("https://rahulshettyacademy.com/angularpractice/")

successMessageEx = "Success! Thank you!."

driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()

namesProducts = driver.find_elements(By.XPATH, "//div[@class='card h-100']")


for product in namesProducts:
    productName = product.find_element(By.XPATH, "div/h4/a")
    if productName.text == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, "//a[contains(text(),'Checkout ( 1 )')]").click()

driver.find_element(By.XPATH, "//button[contains(text(),'Checkout ')]").click()

driver.find_element(By.XPATH, "//input[@id='country']").send_keys("Alb")

countryChose = driver.find_element(By.LINK_TEXT, "Albania")

wait.until(expected_conditions.element_to_be_clickable(countryChose)).click()
driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
successMessage = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text.strip()
print(successMessage)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-success alert-dismissible']")))
assert "Success! Thank you!" in successMessage

time.sleep(10)

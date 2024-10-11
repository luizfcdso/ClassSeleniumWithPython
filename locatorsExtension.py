from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/client")

driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("luizxtcosta@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Test@321")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Test@321")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# another way to write last one click
# driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()






import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

MyName = "Luiz"

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(MyName)
driver.find_element(By.ID, "alertbtn").click()

alert = driver.switch_to.alert
time.sleep(5)
alertText = alert.text
print(alertText)
assert MyName in alertText

alert.accept()

#alert.dismiss() #nesse caso ele vai negar ao inves de aceitar

time.sleep(10)



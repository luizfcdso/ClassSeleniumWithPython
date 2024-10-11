import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#simplesmente escrevendo essa linha de cód o sistema
#vai esperar tudo 5 seg antes de dar falha
driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(5)
resultList = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(resultList)
time.sleep(3)
for result in resultList:
    result.find_element(By.XPATH, "div/button").click()



driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
codeApply = driver.find_element(By.XPATH, "//span[@class='promoInfo']").text
print(codeApply)
assert codeApply == "Code applied ..!"











#assert count > 0

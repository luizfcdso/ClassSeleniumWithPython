import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
#simplesmente escrevendo essa linha de cód o sistema
#vai esperar tudo 5 seg antes de dar falha
driver.implicitly_wait(2)
wait = WebDriverWait(driver,10)

expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(5)




resultList = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(resultList)
time.sleep(3)

for result in resultList:
    actualList.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()

print(actualList)

assert expectedList == actualList


driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//tr/td[5]/p")))
prices = driver.find_elements(By.XPATH, "//tr/td[5]/p")
sum = 0

for price in prices:
    sum = sum + int(price.text)

print(sum)


totalAmount = int(driver.find_element(By.XPATH, "//span[@class='totAmt']").text)
assert sum == totalAmount

print(sum)

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='promoInfo']")))
codeApply = driver.find_element(By.XPATH, "//span[@class='promoInfo']").text
print(codeApply)
time.sleep(2)
discountPrice = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
print(f"totalAmount: {totalAmount}, discountPrice: {discountPrice}")


assert totalAmount > discountPrice


assert codeApply == "Code applied ..!"











#assert count > 0

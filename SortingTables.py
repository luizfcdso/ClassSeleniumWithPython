from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
browserSortedList = []
#hitting the website
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
#click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
#collect all veggie names -> browsersortedveggieList
veggieList = driver.find_elements(By.XPATH, "//tr/td [1]")
for ele in veggieList:
    browserSortedList.append(ele.text)

#antes de embaralhar, vou salvar em uma variavel
newSortedList = browserSortedList.copy()
#Sort this BrowserSortedvaggieList => newSortedList
browserSortedList.sort()
#BrowserSortedList == NewSortedList
assert browserSortedList == newSortedList

print(newSortedList, browserSortedList)
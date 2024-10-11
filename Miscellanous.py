import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
#passo abaixo mostra como tirar um simples print
driver.get_screenshot_as_file("screen.png")
time.sleep(5)
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#abaixo mostro como rodar o teste sem abrir o browser

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument("headless")
chrome_opt.add_argument("--disable-gpu")  # Desativar GPU (necessário em alguns sistemas)
chrome_opt.add_argument("--no-sandbox")  # Necessário em ambientes Linux
chrome_opt.add_argument("--window-size=1920,1080")  # Definir o tamanho da janela no modo headless

#necessário passar esse pedaço de cod como abaixo para poder rodar o teste em headless
driver = webdriver.Chrome(options=chrome_opt)
driver.maximize_window()


driver.get('https://rahulshettyacademy.com/AutomationPractice/')

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
#passo abaixo mostra como tirar um simples print
driver.get_screenshot_as_file("screen.png")

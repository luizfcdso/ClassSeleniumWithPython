import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#Outra maneira de invocar o browser é dessa forma, vc pode simplismente invocar o browser
#baixando o arquivo do driver do chrome, necessário ser a mesma versão do seu browser
# service_obj = Service("caminho do driver")
# driver = webdriver.Chrome(service=service_obj)
driver = webdriver.Chrome()


driver.get("https://rahulshettyacademy.com/angularpractice/")


driver.find_element(By.NAME, "email").send_keys("luizxtcosta@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("test@123")
driver.find_element(By.ID, "exampleCheck1").click()

driver.find_element(By.XPATH, "//input[@type='submit']").click()

#Static Dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(0)
#dropdown.select_by_visible_text("Female")'




messageSuccess = driver.find_element(By.CLASS_NAME, "alert-success").text




print(messageSuccess)
assert "Success! The Form has been submitted successfully!." in messageSuccess
time.sleep(3)
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# Replace with the path to your ChromeDriver
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.magazineluiza.com.br/")
driver.maximize_window()

# Search for Samsung S23
search_field = driver.find_element(By.CSS_SELECTOR, "#input-search")
search_field.send_keys("Samsung S23")
search_field.send_keys(Keys.ENTER)

# Wait for search results to load
wait = WebDriverWait(driver, 50)
wait.until(EC.visibility_of_element_located(By.CSS_SELECTOR, "span[title='Resultados para ']"))

# Click on the specific product (modify xpath if needed)
product_title = driver.find_element(By.XPATH, "//h2[normalize-space()='Smartphone Samsung Galaxy S23 256GB Preto 5G']")
product_title.click()

# Wait for Add to Cart button to be visible
cart_button = driver.find_element(By.XPATH, "//label[normalize-space()='Comprar Agora']")
wait.until(EC.visibility_of(cart_button))

cart_button.click()

# Scroll down the page (optional)
actions = ActionChains(driver)
actions.scroll_by_amount(0, 1000).perform()

# Click on Checkout button (modify xpath if needed)
checkout_button = driver.find_element(By.XPATH, "(//button[@class='sc-kOPcWz diwoJl sc-idPYgo dCQwqq'])[1]")
checkout_button.click()

# Wait for cart to load (optional)
# You can add additional logic here to wait for specific elements in the cart

# Verify product name in cart (modify selector if needed)
cart_product = driver.find_element(By.CSS_SELECTOR, "div[class='BasketTable'] p:nth-child(1)")
cart_text = cart_product.text

# Assert product name contains "Samsung Galaxy S23" (modify assertion if needed)
assert "Samsung Galaxy S23" in cart_text

print(cart_text)

driver.quit()

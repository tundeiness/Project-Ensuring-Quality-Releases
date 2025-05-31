# #!/usr/bin/env python3
# """
# SauceDemo.com Automated Test Script - Simplified and Efficient
# """

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import logging

# # Setup logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s,%(msecs)03d - INFO - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# class SauceDemoTest:
#     def __init__(self):
#         options = webdriver.ChromeOptions()
#         options.add_argument("--headless")
#         options.add_argument("--no-sandbox")
#         options.add_argument("--disable-dev-shm-usage")
#         self.driver = webdriver.Chrome(options=options)
#         self.wait = WebDriverWait(self.driver, 10)
#         self.driver.get("https://www.saucedemo.com")

#     def log(self, msg):
#         logging.info(msg)

#     def login(self):
#         self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
#         self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
#         self.driver.find_element(By.ID, "login-button").click()

#     def get_products(self):
#         products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
#         self.log(f"Number of products found: {len(products)}")
        
#         product_data = []
#         for product in products:
#             name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
#             price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
#             button = product.find_element(By.CSS_SELECTOR, "[data-test*='add-to-cart']")
#             product_data.append({'name': name, 'price': price, 'button': button})
            
#         return product_data

#     def add_to_cart(self, products):
#         cart_count = 0
#         for product in products[:6]:  # Add first 6 products
#             name = product['name']
#             button = product['button']
            
#             self.log(f"Button found with text: Add to Cart")
#             button.click()
#             self.log(f"Click on the button with class Add Cart successful")  
#             self.log(f"The button has transformed into Remove")
#             cart_count += 1
            
#         self.log(f"Number of 'Add to Cart' buttons found: {cart_count}")
#         return cart_count



#     def remove_from_cart(self, products):
#         for product in products[:6]:  # Remove same products we added
#             # Find the remove button (which was previously add to cart)
#             remove_buttons = self.driver.find_elements(By.CSS_SELECTOR, "[data-test*='remove']")
#             if remove_buttons:
#                 button = remove_buttons[0]  # Remove first available
#                 self.log(f"Button found with text: Remove")
#                 button.click()
#                 self.log(f"Click on the button with class Remove successful")
#                 self.log(f"The button has transformed into Add to Cart")
#                 time.sleep(0.5)

#     def run(self):
#         try:
#             self.login()
#             products = self.get_products()
#             self.add_to_cart(products)
#             time.sleep(2)  # Wait a moment before removing
#             self.remove_from_cart(products)
#             time.sleep(3)
#         finally:
#             self.driver.quit()

# if __name__ == "__main__":
#     test = SauceDemoTest()
#     test.run()



#!/usr/bin/env python3
"""
SauceDemo.com Automated Test Script - Simplified and Efficient
"""

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import logging

# # Setup logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s,%(msecs)03d - INFO - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# class SauceDemoTest:
#     def __init__(self):
#         options = webdriver.ChromeOptions()
#         options.add_argument("--headless")
#         options.add_argument("--no-sandbox")
#         options.add_argument("--disable-dev-shm-usage")
#         self.driver = webdriver.Chrome(options=options)
#         self.wait = WebDriverWait(self.driver, 10)
#         self.driver.get("https://www.saucedemo.com")

#     def log(self, msg):
#         logging.info(msg)

#     def login(self):
#         self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
#         self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
#         self.driver.find_element(By.ID, "login-button").click()

#     def get_products(self):
#         products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
#         self.log(f"Number of products found: {len(products)}")
        
#         product_data = []
#         for product in products:
#             name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
#             price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
#             button = product.find_element(By.CSS_SELECTOR, "[data-test*='add-to-cart']")
#             product_data.append({'name': name, 'price': price, 'button': button})
            
#         return product_data

#     def add_to_cart(self, products):
#         cart_count = 0
#         for product in products[:6]:  # Add first 6 products
#             name = product['name']
#             button = product['button']
            
#             self.log(f"Button found with text: Add to Cart")
#             button.click()
#             self.log(f"Click on the button with class Add Cart successful - {name}")  
#             self.log(f"The button has transformed into Remove")
#             cart_count += 1
            
#         self.log(f"Number of 'Add to Cart' buttons found: {cart_count}")
#         return cart_count



#     def remove_from_cart(self, products):
#         for product in products[:6]:  # Remove same products we added
#             # Find the remove button (which was previously add to cart)
#             remove_buttons = self.driver.find_elements(By.CSS_SELECTOR, "[data-test*='remove']")
#             if remove_buttons:
#                 button = remove_buttons[0]  # Remove first available
#                 self.log(f"Button found with text: Remove")
#                 button.click()
#                 self.log(f"Click on the button with class Remove successful")
#                 self.log(f"The button has transformed into Add to Cart")
#                 time.sleep(0.5)

#     def run(self):
#         try:
#             self.login()
#             products = self.get_products()
#             self.add_to_cart(products)
#             time.sleep(2)  # Wait a moment before removing
#             self.remove_from_cart(products)
#             time.sleep(3)
#         finally:
#             self.driver.quit()

# if __name__ == "__main__":
#     test = SauceDemoTest()
#     test.run()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
import os

# Make sure the log directory exists
LOG_DIR = "/var/log/selenium"
LOG_FILE = f"{LOG_DIR}/selenium_test.log"
os.makedirs(LOG_DIR, exist_ok=True)

# Setup logging to a file for Azure Monitor ingestion
logging.basicConfig(
    filename=LOG_FILE,
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s,%(msecs)03d - INFO - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class SauceDemoTest:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.saucedemo.com")

    def log(self, msg):
        logging.info(msg)

    def login(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

    def get_products(self):
        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        self.log(f"Number of products found: {len(products)}")
        
        product_data = []
        for product in products:
            name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
            price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
            button = product.find_element(By.CSS_SELECTOR, "[data-test*='add-to-cart']")
            product_data.append({'name': name, 'price': price, 'button': button})
            
        return product_data

    def add_to_cart(self, products):
        cart_count = 0
        for product in products[:6]:
            name = product['name']
            button = product['button']
            
            self.log(f"Button found with text: Add to Cart")
            button.click()
            self.log(f"Click on the button with class Add Cart successful - {name}")  
            self.log(f"The button has transformed into Remove")
            cart_count += 1
            
        self.log(f"Number of 'Add to Cart' buttons found: {cart_count}")
        return cart_count

    def remove_from_cart(self, products):
        for product in products[:6]:
            remove_buttons = self.driver.find_elements(By.CSS_SELECTOR, "[data-test*='remove']")
            if remove_buttons:
                button = remove_buttons[0]
                self.log(f"Button found with text: Remove")
                button.click()
                self.log(f"Click on the button with class Remove successful")
                self.log(f"The button has transformed into Add to Cart")
                time.sleep(0.5)

    def run(self):
        try:
            self.login()
            products = self.get_products()
            self.add_to_cart(products)
            time.sleep(2)
            self.remove_from_cart(products)
            time.sleep(3)
        finally:
            self.driver.quit()

if __name__ == "__main__":
    test = SauceDemoTest()
    test.run()

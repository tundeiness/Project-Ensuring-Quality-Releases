#!/usr/bin/env python

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import logging as log
# import time

# # Configure logging
# log.basicConfig(
#     level=log.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )

# def login_to_sauce_demo():
#     """Login to the SauceDemo website and return the driver instance"""
#     log.info("Starting login process...")

#     options = Options()
#     options.add_argument('--headless')
#     options.add_argument('--no-sandbox')
#     options.add_argument('--disable-dev-shm-usage')

#     service = Service()
#     driver = webdriver.Chrome(service=service, options=options)

#     driver.get("https://www.saucedemo.com/")
#     log.info("Navigated to SauceDemo homepage.")

#     username_field = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "user-name"))
#     )
#     username_field.send_keys("visual_user")

#     password_field = driver.find_element(By.ID, "password")
#     password_field.send_keys("secret_sauce")

#     driver.find_element(By.ID, "login-button").click()

#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "inventory_container"))
#     )
#     log.info("Successfully logged in!")

#     return driver

# def add_items_to_cart(driver):
#     """Add 3 items to the cart and navigate to cart page"""
#     log.info("Adding items to cart...")

#     add_to_cart_buttons = WebDriverWait(driver, 10).until(
#         EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[data-test^='add-to-cart']"))
#     )

#     for i in range(min(6, len(add_to_cart_buttons))):
#         item_name = driver.find_element(By.XPATH, f"(//div[@class='inventory_item_name'])[{i+1}]").text
#         add_to_cart_buttons[i].click()
#         log.info(f"Added '{item_name}' to cart.")

#     cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
#     cart_link.click()

#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "cart_list"))
#     )
#     log.info("Navigated to cart page.")

#     return driver

# def remove_items_from_cart(driver):
#     """Remove 2 items from the cart"""
#     log.info("Removing items from cart...")

#     remove_buttons = WebDriverWait(driver, 10).until(
#         EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[data-test^='remove-']"))
#     )

#     for i in range(min(5, len(remove_buttons))):
#         item_container = remove_buttons[i].find_element(By.XPATH, "./ancestor::div[@class='cart_item']")
#         item_name = item_container.find_element(By.CLASS_NAME, "inventory_item_name").text
#         remove_buttons[i].click()
#         log.info(f"Removed '{item_name}' from cart.")

#     remaining_items = driver.find_elements(By.CLASS_NAME, "cart_item")
#     log.info(f"{len(remaining_items)} item(s) remaining in cart.")
#     for i, item in enumerate(remaining_items, 1):
#         item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
#         log.info(f"{i}. {item_name}")

#     return driver

# def checkout_items(driver):
#     """Complete the checkout process"""
#     log.info("Starting checkout process...")

#     driver.find_element(By.ID, "checkout").click()

#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "checkout_info_container"))
#     )
#     log.info("On checkout information page.")

#     driver.find_element(By.ID, "first-name").send_keys("John")
#     driver.find_element(By.ID, "last-name").send_keys("Doe")
#     driver.find_element(By.ID, "postal-code").send_keys("12345")

#     driver.find_element(By.ID, "continue").click()

#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "checkout_summary_container"))
#     )
#     log.info("On checkout overview page.")

#     driver.find_element(By.ID, "finish").click()

#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "checkout_complete_container"))
#     )

#     success_header = driver.find_element(By.CLASS_NAME, "complete-header").text
#     log.info(f"Checkout completed! Message: '{success_header}'")

#     time.sleep(5)

#     return driver

# def execute_full_process():
#     """Execute the full shopping process"""
#     try:
#         log.info("=== Starting full SauceDemo process ===")
#         driver = login_to_sauce_demo()
#         driver = add_items_to_cart(driver)
#         driver = remove_items_from_cart(driver)
#         driver = checkout_items(driver)
#         log.info("=== Process completed successfully ===")
#     except Exception as e:
#         log.error(f"An error occurred: {e}")
#     finally:
#         if 'driver' in locals():
#             driver.quit()
#             log.info("Browser closed.")

# if __name__ == "__main__":
#     execute_full_process()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_saucedemo_login_add_remove_items():
    # Initialize Chrome options correctly
    options = ChromeOptions()
    options.add_argument("--headless") 

    # Create the driver with the right options
    driver = webdriver.Chrome(options=options)

    try:
        # Go to the website
        driver.get("https://www.saucedemo.com")

        # Login
        driver.find_element(By.ID, "user-name").send_keys("visual_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Wait for inventory page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
        )

        # Add first 3 items to the cart
        add_buttons = driver.find_elements(By.XPATH, '//button[text()="Add to cart"]')
        for button in add_buttons[:3]:
            button.click()
            time.sleep(0.5)

        # Go to the cart
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Wait for cart page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart_item"))
        )

        # Remove the 3 items
        remove_buttons = driver.find_elements(By.XPATH, '//button[text()="Remove"]')
        for button in remove_buttons[:3]:
            button.click()
            time.sleep(0.5)

        print("✅ Test completed successfully.")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

    finally:
        time.sleep(2)
        driver.quit()


# Run it
test_saucedemo_login_add_remove_items()

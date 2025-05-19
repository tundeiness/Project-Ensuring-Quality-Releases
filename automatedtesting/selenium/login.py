#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import time


def login(driver, user, password):
    print('Starting the login process...')
    driver.get('https://www.saucedemo.com/')
    driver.find_element(By.ID, 'user-name').send_keys(user)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'login-button').click()
    print('Login submitted.')


def run_test():
    print('Starting the browser...')
    
    # Uncomment the lines below when running in headless environments like Azure DevOps
    # options = ChromeOptions()
    # options.add_argument("--headless")
    # driver = webdriver.Chrome(options=options)
    
    driver = webdriver.Chrome()
    print('Browser started successfully. Navigating to login...')
    
    try:
        login(driver, 'standard_user', 'secret_sauce')

        time.sleep(2)  # Wait for page to load

        print("Adding the first item to the cart...")

        # Define CSS selectors
        item_name_selector = ".inventory_item_name"
        cart_badge_selector = ".shopping_cart_badge"

        # Add the first item to the cart
        driver.find_element(By.CSS_SELECTOR, ".btn_inventory").click()
        time.sleep(2)  # Allow cart badge to update

        # Get item name and cart badge value
        item_name = driver.find_element(By.CSS_SELECTOR, item_name_selector).text
        cart_badge = driver.find_element(By.CSS_SELECTOR, cart_badge_selector).text

        print(f"Item added: {item_name}")
        print(f"Cart badge: {cart_badge}")

        # Assert and conditionals
        assert "Sauce Labs" in item_name, "Item name does not contain 'Sauce Labs'"

        if cart_badge == "1":
            print("✅ 1 item was added to the cart successfully.")
        else:
            print("❌ Error: The item was not added correctly to the cart.")

    finally:
        time.sleep(5)  # Optional delay to view result
        driver.quit()
        print("Browser closed.")


if __name__ == "__main__":
    run_test()

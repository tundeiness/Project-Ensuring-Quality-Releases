#!/usr/bin/env python


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
import logging as log
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Configure logging
log.basicConfig(
    level=log.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def login_to_sauce_demo():
    """Login to the SauceDemo website and return the driver instance"""
    log.info("Starting login process...")

    options = ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service()
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://www.saucedemo.com/")
    log.info("Navigate to SauceDemo homepage.")

    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "inventory_container"))
    )
    log.info("Successfully logged in!")

    return driver


def add_items_to_cart(driver):
    log.info("Adding items to cart...")

    inventory_items = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )

    for i, item in enumerate(inventory_items[:3]):
        item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        add_button = item.find_element(By.TAG_NAME, "button")
        add_button.click()
        log.info(f"Added '{item_name}' to cart.")

    cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_link.click()

    # Debugging info
    log.debug(f"Current URL after clicking cart: {driver.current_url}")
    time.sleep(1)  # TEMPORARY: helps confirm it's a timing issue

    try:
        # Try checking for unique cart title or any stable element
        WebDriverWait(driver, 10).until(
            EC.any_of(
                EC.presence_of_element_located((By.CLASS_NAME, "cart_list")),
                EC.presence_of_element_located((By.XPATH, "//span[text()='Your Cart']"))  # Saucedemo uses this header
            )
        )
        log.info("Navigated to cart page.")
    except TimeoutException:
        driver.save_screenshot("cart_error.png")
        log.error("Cart page did not load properly or expected elements not visible.")
        raise


def remove_items_from_cart(driver):
    """Remove 2 items from the cart"""
    log.info("Removing items from cart...")

    remove_buttons = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[data-test^='remove-']"))
    )

    for i in range(min(5, len(remove_buttons))):
        item_container = remove_buttons[i].find_element(By.XPATH, "./ancestor::div[@class='cart_item']")
        item_name = item_container.find_element(By.CLASS_NAME, "inventory_item_name").text
        remove_buttons[i].click()
        log.info(f"Removed '{item_name}' from cart.")

    remaining_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    log.info(f"{len(remaining_items)} item(s) remaining in cart.")
    for i, item in enumerate(remaining_items, 1):
        item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        log.info(f"{i}. {item_name}")

    return driver

def checkout_items(driver):
    """Complete the checkout process"""
    log.info("Starting checkout process...")

    driver.find_element(By.ID, "checkout").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "checkout_info_container"))
    )
    log.info("On checkout information page.")

    driver.find_element(By.ID, "first-name").send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("12345")

    driver.find_element(By.ID, "continue").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "checkout_summary_container"))
    )
    log.info("On checkout overview page.")

    driver.find_element(By.ID, "finish").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "checkout_complete_container"))
    )

    success_header = driver.find_element(By.CLASS_NAME, "complete-header").text
    log.info(f"Checkout completed! Message: '{success_header}'")

    time.sleep(5)

    return driver

def ui_process():
    """Execute the full shopping process"""
    try:
        log.info("=== Starting full SauceDemo process ===")
        driver = login_to_sauce_demo()
        driver = add_items_to_cart(driver)
        driver = remove_items_from_cart(driver)
        driver = checkout_items(driver)
        log.info("=== Process completed successfully ===")
    except Exception as e:
        log.error(f"An error occurred: {e}")
    finally:
        if 'driver' in locals():
            driver.quit()
            log.info("Browser closed.")

if __name__ == "__main__":

    ui_process()



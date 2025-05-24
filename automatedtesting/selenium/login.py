#!/usr/bin/env python
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.common.by import By
# import time
# import tempfile


# def login(driver, user, password):
#     print('Starting the login process...')
#     driver.get('https://www.saucedemo.com/')
#     driver.find_element(By.ID, 'user-name').send_keys(user)
#     driver.find_element(By.ID, 'password').send_keys(password)
#     driver.find_element(By.ID, 'login-button').click()
#     print('Login submitted.')

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import tempfile



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tempfile


def login_to_sauce_demo():
    """Login to the SauceDemo website and return the driver instance"""
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Start maximized
    
    # Set up the WebDriver
    service = Service()  # Update with your chromedriver path if needed
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Navigate to the website
    driver.get("https://www.saucedemo.com/")
    
    # Wait for the login form to be visible
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    
    # Enter login credentials
    username_field.send_keys("visual_user")
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")
    
    # Click the login button
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    
    # Wait for successful login - check for the inventory page
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "inventory_container"))
    )
    print("Successfully logged in!")
    
    return driver



def add_items_to_cart(driver):
    """Add 3 items to the cart and navigate to cart page"""
    # Add 3 items to cart
    add_to_cart_buttons = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[data-test^='add-to-cart']"))
    )
    
    # Add first 3 items to the cart
    for i in range(min(6, len(add_to_cart_buttons))):
        item_name = driver.find_element(By.XPATH, 
            f"(//div[@class='inventory_item_name'])[{i+1}]").text
        add_to_cart_buttons[i].click()
        print(f"Added {item_name} to cart")
    
    # Navigate to the cart
    cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_link.click()
    
    # Wait for the cart page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cart_list"))
    )
    print("Navigated to cart page")
    
    return driver

def remove_items_from_cart(driver):
    """Remove 2 items from the cart"""
    # Remove 2 items from the cart
    remove_buttons = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[data-test^='remove-']"))
    )
    
    # Get the names of items being removed for better logging
    for i in range(min(5, len(remove_buttons))):
        item_container = remove_buttons[i].find_element(By.XPATH, "./ancestor::div[@class='cart_item']")
        item_name = item_container.find_element(By.CLASS_NAME, "inventory_item_name").text
        remove_buttons[i].click()
        print(f"Removed {item_name} from cart")
    
    # List remaining items in cart
    remaining_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    print(f"Items remaining in cart ({len(remaining_items)}):")
    for i, item in enumerate(remaining_items, 1):
        item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        print(f"{i}. {item_name}")
    
    return driver

def checkout_items(driver):
    """Complete the checkout process"""
    # Proceed to checkout
    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()
    
    # Wait for checkout information page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "checkout_info_container"))
    )
    print("Navigated to checkout information page")
    
    # Fill in the checkout information
    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("John")
    
    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Doe")
    
    postal_code = driver.find_element(By.ID, "postal-code")
    postal_code.send_keys("12345")
    
    # Continue to the next checkout page
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()
    
    # Wait for checkout overview page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "checkout_summary_container"))
    )
    print("Navigated to checkout overview page")
    
    # Complete the order
    finish_button = driver.find_element(By.ID, "finish")
    finish_button.click()
    
    # Wait for checkout complete page
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "checkout_complete_container"))
    )
    
    # Verify success message
    success_header = driver.find_element(By.CLASS_NAME, "complete-header").text
    print(f"Checkout completed! Message: {success_header}")
    
    # Keep the browser open for a few seconds to see the result
    time.sleep(5)
    
    return driver

def execute_full_process():
    """Execute the full shopping process"""
    try:
        driver = login_to_sauce_demo()
        driver = add_items_to_cart(driver)
        driver = remove_items_from_cart(driver)
        driver = checkout_items(driver)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser
        if 'driver' in locals():
            driver.quit()

# Call the main function when the script is executed
if __name__ == "__main__":
    execute_full_process()









# def run_test():
#     print('Starting the browser...')

#     # Configure Chrome options for CI environments
#     options = ChromeOptions()
#     options.add_argument("--headless")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_argument("--disable-gpu")

#     # Set a unique temporary user data directory to avoid session conflicts
#     user_data_dir = tempfile.mkdtemp()
#     options.add_argument(f"--user-data-dir={user_data_dir}")

#     driver = webdriver.Chrome(options=options)
#     print('Browser started successfully. Navigating to login...')

#     try:
#         login(driver, 'standard_user', 'secret_sauce')

#         time.sleep(2)  # Wait for page to load

#         print("Adding the first item to the cart...")

#         # Define CSS selectors
#         item_name_selector = ".inventory_item_price"
#         cart_badge_selector = ".shopping_cart_link"

#         # Add the first item to the cart
#         driver.find_element(By.CSS_SELECTOR, ".btn_inventory").click()
#         time.sleep(2)  # Allow cart badge to update

#         # Get item name and cart badge value
#         item_name = driver.find_element(By.CSS_SELECTOR, item_name_selector).text
#         cart_badge = driver.find_element(By.CSS_SELECTOR, cart_badge_selector).text

#         print(f"Item added: {item_name}")
#         print(f"Cart badge: {cart_badge}")

#         # Assert and conditionals
#         assert "Sauce Labs" in item_name, "Item name does not contain 'Sauce Labs'"

#         if cart_badge == "1":
#             print("✅ 1 item was added to the cart successfully.")
#         else:
#             print("❌ Error: The item was not added correctly to the cart.")

#     finally:
#         time.sleep(5)  # Optional delay to view result
#         driver.quit()
#         print("Browser closed.")


# if __name__ == "__main__":
#     run_test()

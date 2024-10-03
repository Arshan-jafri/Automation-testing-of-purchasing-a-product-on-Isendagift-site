import os
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Suppress TensorFlow logging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppresses INFO and WARNING logs from TensorFlow

# Initialize Chrome WebDriver with options
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--headless")  # Uncomment this to run in headless mode

print("Starting the WebDriver...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # Step 1: Open the login page
    print("Opening the login page...")
    driver.get("https://qa.isendagift.com/my-account/?alg_wc_ev_activate_account_message=25")
    driver.maximize_window()

    # Step 2: Enter username
    print("Entering username...")
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    username_input.clear()
    username_input.send_keys("arshan@yopmail.com")

    # Step 3: Enter password
    print("Entering password...")
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password_input.clear()
    password_input.send_keys("arshan@yopmail.com")

    # Step 4: Click login button
    print("Clicking login button...")
    login_button_xpath = "//button[contains(@name, 'login')]"
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, login_button_xpath))
    )
    login_button.click()


    # Wait for 2-3 seconds after login
    WebDriverWait(driver, 3)

    # Step 5: Click on the "Cakes" menu option
    print("Navigating to Cakes category...")
    cakes_xpath = "//li[contains(@class, 'menu-item') and contains(@class, 'menu-item-object-product_cat') and contains(@class, 'menu-item-has-children')]/a[contains(text(), 'Cakes')]"
    cakes_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, cakes_xpath))
    )
    
    cakes_menu.click()  # Click the Cakes menu

    # Wait for the Cakes page to load
    WebDriverWait(driver, 10).until(EC.title_contains("Cakes"))
    print("Successfully navigated to Cakes category!")
    
    print("Clicking on Vanilla Buttercream Cake...")
    product_xpath = "//h2[contains(@class, 'woo-loop-product__title')]/a[contains(text(), 'Vanilla Buttercream Cake')]"
    product_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, product_xpath))
    )
    
    product_link.click()  # Click the Vanilla Buttercream Cake product

    # Wait for the product page to load
    WebDriverWait(driver, 10).until(EC.title_contains("Vanilla Buttercream Cake"))
    print("Successfully navigated to the Vanilla Buttercream Cake product page!")

except Exception as e:
    print("An error occurred:")
    traceback.print_exc()

finally:
    # Close the browser
    print("Closing the browser...")
    driver.quit()


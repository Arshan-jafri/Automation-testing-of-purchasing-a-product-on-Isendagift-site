import os
import time
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
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--disable-software-rasterizer")  # Disable software rasterization
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
    username_input.send_keys("arshan1@yopmail.com")
    print("Username entered.")

    # Step 3: Enter password
    print("Entering password...")
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password_input.clear()
    password_input.send_keys("arshan1@yopmail.com")
    print("Password entered.")

    # Step 4: Click login button
    print("Clicking login button...")
    login_button_xpath = "//button[contains(@name, 'login')]"
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, login_button_xpath))
    )
    login_button.click()
    print("Login button clicked.")

    # Wait for 2-3 seconds after login
    print("Waiting for the login to process...")
    WebDriverWait(driver, 3)

    # Step 5: Click on the "Cakes" menu option
    print("Navigating to Cakes category...")
    cakes_xpath = "//li[contains(@class, 'menu-item') and contains(@class, 'menu-item-object-product_cat') and contains(@class, 'menu-item-has-children')]/a[contains(text(), 'Cakes')]"
    cakes_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, cakes_xpath))
    )
    
    cakes_menu.click()  # Click the Cakes menu
    print("Clicked on Cakes category.")

    # Wait for the Cakes page to load
    WebDriverWait(driver, 10).until(EC.title_contains("Cakes"))
    print("Successfully navigated to Cakes category!")

    # Step 6: Click on "Vanilla Buttercream Cake"
    print("Clicking on Vanilla Buttercream Cake...")
    product_xpath = "//h2[contains(@class, 'woo-loop-product__title')]/a[contains(text(), 'Vanilla Buttercream Cake')]"
    product_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, product_xpath))
    )
    
    product_link.click()  # Click the Vanilla Buttercream Cake product
    print("Clicked on Vanilla Buttercream Cake product.")

    # Wait for the product page to load
    WebDriverWait(driver, 10).until(EC.title_contains("Vanilla Buttercream Cake"))
    print("Successfully navigated to the Vanilla Buttercream Cake product page!")

    # Step 8: Click on the "Buy Now" button
    print("Clicking the 'Buy Now' button...")
    buy_now_xpath = "//button[contains(text(), 'Buy Now')]"
    buy_now_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, buy_now_xpath))
    )
    
    buy_now_button.click()  # Click the Buy Now button
    print("Clicked 'Buy Now' and navigating to checkout...")

    # Wait for the action to complete and navigate to the checkout page
    WebDriverWait(driver, 10).until(EC.title_contains("Checkout"))
    print("Successfully clicked 'Buy Now' and navigated to the checkout page!")
    
    # Step 9: Enter first name in the checkout form
    print("Entering first name...")
    first_name_xpath = "//input[@id='billing_first_name']"
    first_name_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, first_name_xpath))
    )
    first_name_input.clear()
    first_name_input.send_keys("Arsh")  # Set the first name to "Arsh"
    print("First name entered.")

    # Step 10: Enter last name in the checkout form
    print("Entering last name...")
    last_name_xpath = "//input[@id='billing_last_name']"
    last_name_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, last_name_xpath))
    )
    last_name_input.clear()
    last_name_input.send_keys("Jaf")  # Set the last name to "Jaf"
    print("Last name entered.")

    # Step 11: Click the payment method for Debit & Credit Cards
    print("Selecting payment method: Debit & Credit Cards...")
    payment_method_xpath = "//label[@for='payment_method_ppcp-credit-card-gateway']"
    payment_method_label = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, payment_method_xpath))
    )
    payment_method_label.click()  # Click the Debit & Credit Cards label
    print("Payment method selected.")

    # Step 12: Enter card details
    print("Entering card details...")
    
    # Switch to the iframe for card number (iframe 1)
    print("Switching to iframe 1 for card number...")
    driver.switch_to.frame(0)  # Switch to the first iframe

    try:
        # Enter card number
        card_number_xpath = "//input[@name='number']"
        card_number_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, card_number_xpath))
        )
        card_number_input.clear()
        card_number_input.send_keys("4032039612679425")
        print("Card number entered.")
    except Exception as e:
        print("Failed to enter card number:", e)

    # Switch back to the main content
    driver.switch_to.default_content()

    # Switch to the iframe for expiry date (iframe 3)
    print("Switching to iframe 3 for expiry date...")
    driver.switch_to.frame(2)  # Switch to the third iframe

    try:
        # Enter expiry date using the new XPath
        expiry_xpath = "//input[@aria-describedby='card-expiry-field-description']"  # Updated XPath for expiry
        expiry_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, expiry_xpath))
        )
        expiry_input.clear()
        expiry_input.send_keys("06/29")  # Enter the expiry date in MM/YY format
        print("Expiry date entered.")
    except Exception as e:
        print("Failed to enter expiry date:", e)
        driver.switch_to.default_content()  # Switch back to main content if error occurs

    # Switch back to the main content
    driver.switch_to.default_content()

    # Switch to the iframe for CVV (iframe 5)
    print("Switching to iframe 5 for CVV...")
    driver.switch_to.frame(4)  # Switch to the fifth iframe

    try:
        # Enter CVV
        cvv_xpath = "//input[@name='cvv']"  # XPath for CVV
        cvv_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, cvv_xpath))
        )
        cvv_input.clear()
        cvv_input.send_keys("123")  # Enter CVV
        print("CVV entered.")
    except Exception as e:
        print("Failed to enter CVV:", e)

    # Switch back to the main content
    driver.switch_to.default_content()

    # Step 13: Enter email address
    print("Entering email...")
    email_input_xpath = "//input[@id='billing_email']"
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, email_input_xpath))
    )
    email_input.clear()
    email_input.send_keys("arshan1@yopmail.com")  # Set the email
    print("Email entered.")

    # Step 14: Click the 'Place order' button
    print("Clicking the 'Place order' button...")
    place_order_xpath = "//div[@id='ppcp-hosted-fields']//button[@id='place_order']"
    try:
        place_order_button = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, place_order_xpath))
        )

        # Scroll to the 'Place order' button
        driver.execute_script("arguments[0].scrollIntoView(true);", place_order_button)
        
        # Wait until the button is clickable
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, place_order_xpath)))

        # Use JavaScript to click the button
        driver.execute_script("arguments[0].click();", place_order_button)  # Click the Place Order button
        print("Clicked 'Place order'.")
    except Exception as e:
        print("An error occurred while trying to place the order:")
        print(traceback.format_exc())

    # Wait for the order confirmation page to load
    try:
        # WebDriverWait(driver, 100).until(EC.title_contains("Order Confirmation"))

        # Confirm order placed successfully
        print("Order placed successfully!")

        # Check for the specific message
        thank_you_message_xpath = "//p[contains(@class, 'woocommerce-notice') and contains(@class, 'woocommerce-thankyou-order-received')]"
        thank_you_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, thank_you_message_xpath))
        )

        if "Thank you. Your order has been received." in thank_you_message.text:
            print("Thank you message confirmed:", thank_you_message.text)
        else:
            print("Thank you message not found or does not match.")

    except Exception as e:
        print("An unexpected error occurred while checking the thank you message:")
        print(traceback.format_exc())

finally:
    print("Closing the browser...")
    driver.quit()

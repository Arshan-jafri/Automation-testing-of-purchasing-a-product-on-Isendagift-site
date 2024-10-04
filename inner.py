from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Maximize the browser window

# Set up the Chrome WebDriver service
service = Service("chromedriver.exe")  # Replace with the path to your chromedriver executable

# Create a new Chrome WebDriver instance
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the website
driver.get("https://cosse.com.au/")

# Wait for the page to load (adjust the delay if needed)
time.sleep(2)
WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "//div[@id='column--66ae8a0c-a395-4313-b9aa-dfcf6368c3a6']//h3[contains(text(), 'Hand & Body Lotion')]")))
# Find the "hand and body lotion" section
section = driver.find_element(By.XPATH, "//div[@id='column--66ae8a0c-a395-4313-b9aa-dfcf6368c3a6']")


# Scroll to the section


# Wait for a few seconds (adjust the delay if needed)
time.sleep(2) 

WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "//div[@id='column--66ae8a0c-a395-4313-b9aa-dfcf6368c3a6']")))

driver.execute_script("arguments[0].scrollIntoView();", section)

accept_button = driver.find_element(By.XPATH, "//button[@data-gdpr-accept]")
accept_button.click()
print("GDPR Accept button clicked.")

# Find the "Shop Now" button beneath the section
button = driver.find_element(By.XPATH, "//div[@id='column--66ae8a0c-a395-4313-b9aa-dfcf6368c3a6']//a[contains(text(), 'Shop Now')]")

# Click the "Shop Now" button
button.click() 

try:
    # Wait for the modal's close button to be visible (indicating that the modal is open)
    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='mc-closeModal' and @aria-label='Close']"))
    )

    # Click the close button
    close_button.click()
    
    print("Modal closed successfully.")
except Exception as e:
    print(f"No modal or could not close it: {e}")
try:
 # Wait for the dropdown to be visible
    dropdown = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'select[data-swatch-index="7909440579-0"]'))
    )
    
    # Click the dropdown to open the options
    dropdown.click()
    
    # Wait for the "Lemon Verbena" option to be present and select it
    lemon_verbena_option = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//option[text()='Lemon Verbena']"))
    )
    lemon_verbena_option.click()
    print("Selected 'Lemon Verbena'.")

except Exception as e:
    print(f"An error occurred: {e}")
try:
    # Wait for the 'Add to Cart' button to be clickable
    add_to_cart_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-buy-button="7909440579"]'))
    )
    add_to_cart_button.click()

    print("Product added to cart successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
    # Take a screenshot for debugging
    driver.save_screenshot('error_screenshot.png')
 

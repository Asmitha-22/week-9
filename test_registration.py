from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure Chrome (headless for Jenkins)
chrome_options = Options()
chrome_options.add_argument("--headless")  # comment this if you want to see browser locally
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")

# Start ChromeDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("http://localhost:31930")

    # Wait until the registration form is visible
    wait = WebDriverWait(driver, 15)
    full_name_field = wait.until(
        EC.presence_of_element_located((By.NAME, "full_name"))
    )

    # Fill the form
    full_name_field.send_keys("Test User")
    driver.find_element(By.NAME, "email").send_keys("test_user@gmail.com")
    driver.find_element(By.NAME, "username").send_keys("testuser123")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.NAME, "confirm_password").send_keys("password123")
    driver.find_element(By.NAME, "phone").send_keys("9876543210")
    driver.find_element(By.NAME, "dob").send_keys("2000-01-01")
    driver.find_element(By.NAME, "gender").send_keys("Male")
    driver.find_element(By.NAME, "address").send_keys("Hyderabad, India")

    # Submit
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Wait for success redirect or message
    wait.until(EC.url_changes("http://localhost:31930"))
    print("Test Completed Successfully!")

except Exception as e:
    print("Test Failed:", e)

finally:
    driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

def run_update():
    try:
        EMAIL = os.getenv("NAUKRI_EMAIL")
        PASSWORD = os.getenv("NAUKRI_PASSWORD")

        if not EMAIL or not PASSWORD:
            raise Exception("NAUKRI_EMAIL or NAUKRI_PASSWORD env vars are missing.")

        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
        )

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # Open login page
        driver.get("https://www.naukri.com/nlogin/login")
        time.sleep(5)

        # Fill login details
        email_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter your active Email ID / Username']")
        password_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']")

        email_input.clear()
        email_input.send_keys(EMAIL)
        password_input.clear()
        password_input.send_keys(PASSWORD)

        driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
        time.sleep(6)

        # Check if login is successful
        if "nlogin" in driver.current_url:
            raise Exception("Login failed. Check credentials or captcha.")

        # Navigate to profile
        driver.get("https://www.naukri.com/mnjuser/profile")
        time.sleep(6)

        # Trigger headline update (simulate an edit)
        headline = driver.find_element(By.CLASS_NAME, "resumeHeadline")
        headline.click()
        time.sleep(2)

        headline.send_keys(" ")
        headline.send_keys(Keys.BACKSPACE)
        time.sleep(1)

        save_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Save')]")
        save_button.click()
        time.sleep(3)

        print("✅ Naukri profile updated successfully.")
        driver.quit()
        return True

    except Exception as e:
        print("❌ Error occurred:", str(e))
        return False

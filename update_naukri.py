from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import traceback
def run_update():
    try:
        EMAIL = os.getenv("NAUKRI_EMAIL")
        PASSWORD = os.getenv("NAUKRI_PASSWORD")

        if not EMAIL or not PASSWORD:
            raise Exception("Email/password environment variables not set.")

        # Setup headless browser
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")

        driver = webdriver.Chrome(options=options)
        driver.get("https://www.naukri.com/nlogin/login")
        time.sleep(3)

        # Use placeholder-based selection
        email_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter Email ID / Username']")
        password_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']")

        email_input.send_keys(EMAIL)
        password_input.send_keys(PASSWORD)

        # Login button
        login_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
        login_btn.click()
        time.sleep(5)

        # Go to profile
        driver.get("https://www.naukri.com/mnjuser/profile")
        time.sleep(5)

        # Click edit headline
        edit_btn = driver.find_element(By.XPATH, "//span[text()='Resume Headline']/ancestor::div[contains(@class,'editCard')]//span[contains(text(),'edit')]")
        edit_btn.click()
        time.sleep(2)

        textarea = driver.find_element(By.XPATH, "//textarea[contains(@class,'resumeHeadline')]")
        textarea.send_keys(" ")  # add space
        textarea.send_keys(Keys.BACKSPACE)  # remove it

        save_btn = driver.find_element(By.XPATH, "//button[text()='Save']")
        save_btn.click()
        time.sleep(2)

        driver.quit()
        return True

    except Exception as e:
        print("Update failed:", str(e))
    
    driver.quit()


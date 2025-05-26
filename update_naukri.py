from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os

def run_update():
    try:
        EMAIL = os.getenv("NAUKRI_EMAIL")
        PASSWORD = os.getenv("NAUKRI_PASSWORD")

        if not EMAIL or not PASSWORD:
            raise Exception("Environment variables NAUKRI_EMAIL or NAUKRI_PASSWORD not set.")

        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=options)
        driver.get("https://www.naukri.com/nlogin/login")
        time.sleep(3)

        # ✅ Login
        driver.find_element(By.XPATH, "//input[@placeholder='Enter your active Email ID / Username']").send_keys(EMAIL)
        driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys(PASSWORD)
        driver.find_element(By.XPATH, "//button[text()='Login']").click()
        time.sleep(5)

        # ✅ Go to profile
        driver.get("https://www.naukri.com/mnjuser/profile")
        time.sleep(6)

        # ✅ Click "Resume headline" edit icon
        driver.find_element(By.XPATH, "//span[text()='Resume headline']/ancestor::section//i").click()
        time.sleep(3)

        # ✅ Modify the resume headline
        headline = driver.find_element(By.XPATH, "//textarea[contains(@class, 'resumeHeadline')]")
        headline.send_keys(" ")  # add space
        headline.send_keys(Keys.BACKSPACE)  # remove space (to trigger change)
        time.sleep(1)

        # ✅ Save
        driver.find_element(By.XPATH, "//button[text()='Save']").click()
        time.sleep(2)

        driver.quit()
        print("✅ Profile updated successfully.")
        return True

    except Exception as e:
        import traceback
        traceback.print_exc()
        print("❌ Failed to update profile:", str(e))
        return False

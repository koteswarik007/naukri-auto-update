import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

def run_update():
    try:
        EMAIL = os.getenv("NAUKRI_EMAIL")
        PASSWORD = os.getenv("NAUKRI_PASSWORD")

        if not EMAIL or not PASSWORD:
            raise Exception("Environment variables not set.")

        options = uc.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = uc.Chrome(options=options)

        driver.get("https://www.naukri.com/nlogin/login")
        time.sleep(3)

        driver.find_element(By.ID, "usernameField").send_keys(EMAIL)
        driver.find_element(By.ID, "passwordField").send_keys(PASSWORD)
        driver.find_element(By.XPATH, "//button[text()='Login']").click()
        time.sleep(5)

        driver.get("https://www.naukri.com/mnjuser/profile")
        time.sleep(5)

        # Click "Edit" on resume headline
        edit_buttons = driver.find_elements(By.CLASS_NAME, "edit")
        for btn in edit_buttons:
            try:
                btn.click()
                break
            except:
                continue
        time.sleep(3)

        # Edit resume headline
        textarea = driver.find_element(By.XPATH, "//textarea[contains(@class,'resumeHeadline')]")
        textarea.send_keys(" ")  # Simulate change
        textarea.send_keys(Keys.BACKSPACE)
        time.sleep(2)

        # Save headline
        save_btn = driver.find_element(By.XPATH, "//button[text()='Save']")
        save_btn.click()

        print("✅ Profile updated.")
        driver.quit()
        return True

    except Exception as e:
        print("❌ Error:", str(e))
        return False

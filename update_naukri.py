from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

def run_update():
    EMAIL = os.getenv("NAUKRI_EMAIL")
    PASSWORD = os.getenv("NAUKRI_PASSWORD")

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.naukri.com/nlogin/login")
    time.sleep(3)

    # Login
    driver.find_element(By.ID, "usernameField").send_keys(EMAIL)
    driver.find_element(By.ID, "passwordField").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    time.sleep(5)

    # Go to profile
    driver.get("https://www.naukri.com/mnjuser/profile")
    time.sleep(5)
   headline = driver.find_element(By.CLASS_NAME, "resumeHeadline")
        headline.send_keys(" ")
        headline.send_keys(Keys.BACKSPACE)
    # Edit and Save headline
    try:
        driver.find_element(By.CLASS_NAME, "edit icon").click()
        time.sleep(3)
       
        headline.send_keys(Keys.BACKSPACE)
        driver.find_element(By.XPATH, "//button[text()='Save']").click()
        print("Profile updated successfully.")
    except Exception as e:
        print("Update failed:", str(e))
    
    driver.quit()

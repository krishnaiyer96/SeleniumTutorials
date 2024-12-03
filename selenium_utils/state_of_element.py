from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

class Is_Enabled:
    @staticmethod
    def check_if_enabled():
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        url = "https://www.letskodeit.com/home"
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(5)
        print(f"Title of the page is {driver.title}")
        login_link = driver.find_element(By.XPATH, "//a[@href='/login']")
        login_link.click()
        email_field = driver.find_element(By.XPATH, "//input[@placeholder='Email Address']")
        email_field.send_keys("krishna.iyer17@gmail.com")
        password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        password_field.send_keys("Learning@123")
        login_button = driver.find_element(By.XPATH, "//button[@id='login']")
        login_btn_is_enabled = login_button.is_enabled()
        if login_btn_is_enabled:
            login_button.click()
        else:
            print("Login Not enabled")
        time.sleep(2)
        driver.quit()

if __name__ == "__main__":
    Is_Enabled.check_if_enabled()

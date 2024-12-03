import time
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def click_type_actions():
    url = "https://www.letskodeit.com/home"
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
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
    login_button.click()
    time.sleep(2)
    driver.quit()


if __name__ == "__main__":
    click_type_actions()
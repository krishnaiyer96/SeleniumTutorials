import time
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium_utils.handy_wrappers import  HandyWrappers


class UsingWrappers:
    @staticmethod
    def test():
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        url = "https://www.letskodeit.com/home"
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(5)
        print(f"Title of the page is {driver.title}")
        hw = HandyWrappers(driver)

        login_link = hw.getElement("//a[@href='/login']", 'xpath')
        login_link.click()
        email_field = hw.getElement("//input[@placeholder='Email Address']", 'xpath')
        email_field.send_keys("krishna.iyer17@gmail.com")
        password_field = hw.getElement("//input[@placeholder='Password']", 'xpath')
        password_field.send_keys("Learning@123")
        login_button = hw.getElement("//button[@id='login']", 'xpath')
        login_button.click()
        time.sleep(2)
        driver.quit()

if __name__ == '__main__':
    UsingWrappers.test()



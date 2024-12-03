import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Find_HiddenElement:
    def find_hiddenElement():
        url = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(5)
        print(f"Title of the page is {driver.title}")

        block_element = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
        element_state = block_element.is_displayed()

        print("The element is displayed ", str(element_state))

        hide_btn = driver.find_element(By.ID, "hide-textbox")
        hide_btn.click()
        time.sleep(2)

        block_element = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
        element_state = block_element.is_displayed()

        print("The element is displayed ", str(element_state))

        show_btn = driver.find_element(By.ID, "show-textbox")
        show_btn.click()
        time.sleep(2)

        block_element = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
        element_state = block_element.is_displayed()

        print("The element is displayed ", str(element_state))

        driver.quit()

if __name__ == '__main__':
    Find_HiddenElement.find_hiddenElement()








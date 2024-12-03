from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

class WorkingWithElementList:

    def test_list_of_elements(self, car):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        url = "https://www.letskodeit.com/practice"
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(5)
        print(f"Title of the page is {driver.title}")

        radioButton_list = driver.find_elements(By.XPATH, "//input[contains(@type,'radio') and contains(@name, 'cars')]")
        for radio_button in radioButton_list:
            if radio_button.get_attribute("value") == 'car':
                radio_button.click()
                break


        time.sleep(2)
if __name__ == '__main__':
    check = WorkingWithElementList()
    check.test_list_of_elements("benz")





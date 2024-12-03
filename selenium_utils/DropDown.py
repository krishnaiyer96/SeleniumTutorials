import time 
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium import webdriver

class DropDown:
    def select_dropdown():
        url = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(5)
        print(f"Title of the page is {driver.title}")

        dropdown_element = driver.find_element(By.XPATH, "//select[@id='carselect']")
        sel = Select(dropdown_element)

        sel.select_by_value('benz')
        print('Select Benz by Value')
        time.sleep(2)
        sel.select_by_value('honda')
        print('Select Honda by Value')

        time.sleep(2)

if __name__ == '__main__':
    DropDown.select_dropdown()
  



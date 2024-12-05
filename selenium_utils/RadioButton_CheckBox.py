import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class radio_checkbox_test:
    @staticmethod
    def select_radio_btn_checkbox():
        url = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(5)
        print(f"Title of the page is {driver.title}")


        bmw_radio_btn = driver.find_element(By.ID, 'bmwradio')
        print(bmw_radio_btn.get_attribute("value"))
        bmw_radio_btn.click()
        time.sleep(2)

        benz_radio_btn = driver.find_element(By.ID, 'benzradio')
        benz_radio_btn.click()
        time.sleep(2)

        honda_radio_btn = driver.find_element(By.ID, 'hondaradio')
        honda_radio_btn.click()
        time.sleep(2)

        bmw_check_box = driver.find_element(By.ID, 'bmwcheck')
        if bmw_check_box.is_selected():
            print("Bmw checkbox is already selected")
        else:
            bmw_check_box.click()
        time.sleep(2)

        benz_check_box = driver.find_element(By.ID, 'benzcheck')
        benz_check_box.click()
        time.sleep(2)
        if benz_check_box.is_selected():
            benz_check_box.click()
            print("Benz checkbox is unselected")
        time.sleep(2)

        honda_check_box = driver.find_element(By.ID, 'hondacheck')
        honda_check_box.click()
        time.sleep(2)
        if honda_check_box.is_selected():
            honda_check_box.click()
            print("Honda checkbox is unselected")
        time.sleep(2)






if __name__ == '__main__':
    radio_checkbox_test.select_radio_btn_checkbox()

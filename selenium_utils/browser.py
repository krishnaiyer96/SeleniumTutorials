import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

def browser_interaction():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.letskodeit.com/practice")
    title = driver.title
    print(f"The title of the webpage is {title}")
    current_url = driver.current_url
    print(f"The Current url is {current_url}")
    driver.refresh()
    time.sleep(3)
    driver.execute_script("window.open('https://www.google.com')")
    driver.switch_to.window(driver.window_handles[1])
    print(driver.title)
    print(driver.current_url)
    time.sleep(3)
    driver.execute_script("window.open('https://www.youtube.com')")
    driver.switch_to.window(driver.window_handles[2])
    print(driver.title)
    print(driver.current_url)
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()
    print(driver.current_url)
    time.sleep(5)
    driver.quit()

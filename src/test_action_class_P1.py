import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def test_action_class_p1():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")

    #Find the Xpath of First Name text field - //input[@name ="firstname"]

    first_name = driver.find_element(By.XPATH, "//input[@name ='firstname']")

    #Problem Statement - Need to enter Text in UPPER case by pressing Shift key down

    actions = ActionChains(driver=driver)
    actions.key_down(Keys.SHIFT).send_keys_to_element(first_name,"dheeraj sharma").key_up(Keys.SHIFT).perform()

    #teardown the browser

    time.sleep(5)
    driver.quit()

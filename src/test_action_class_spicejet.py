import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton


def test_action_class_spicejet():
    driver = webdriver.Chrome()
    driver.get("https://www.spicejet.com/")

    #driver.maximize_window()
    select_origin = driver.find_element(By.XPATH, "//div[text()='From']")
    time.sleep(3)

    action_class = ActionChains(driver=driver)
    action_class.move_to_element(select_origin).click().send_keys("del").perform()

    time.sleep(8)
    driver.quit()

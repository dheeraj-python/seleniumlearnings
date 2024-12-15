import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton


def test_action_class_p3():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    drag_button = driver.find_element(By.ID, "draggable")
    drop_button = driver.find_element(By.ID,"droppable")

    time.sleep(3)
    #Problem Statement - Click & Hold the element
    action_class = ActionChains(driver=driver)
    #action_class.click_and_hold(on_element=drag_button).perform()
    action_class.drag_and_drop(drag_button, drop_button).perform()

    time.sleep(8)
    driver.quit()

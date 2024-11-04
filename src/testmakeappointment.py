from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_make_appointment():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # Find 'Make an Appointment' button on the page

    make_appointment = driver.find_element(By.ID, "btn-make-appointment")

    # Click on the element
    make_appointment.click()

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(10)
    driver.quit()



from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_make_appointment_with_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # Find 'Make an Appointment' button on the page

    make_appointment = driver.find_element(By.ID, "btn-make-appointment")

    # Click on the element
    make_appointment.click()
    username = driver.find_element(By.ID,"txt-username")
    username.send_keys("John Doe")
    password = driver.find_element(By.ID,"txt-password")
    password.send_keys("ThisIsNotAPassword")

    # click on Login button

    user_login = driver.find_element(By.ID,"btn-login")
    user_login.click()


    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
    time.sleep(10)
    driver.quit()



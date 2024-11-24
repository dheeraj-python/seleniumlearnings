from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_with_registration():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

    # Find 'Make an Appointment' button on the page. Use different user details to run the code..

    first_name = driver.find_element(By.ID, "input-firstname")
    first_name.send_keys("Dheeraj")
    last_name = driver.find_element(By.ID, "input-lastname")
    last_name.send_keys("Sharma")
    user_email = driver.find_element(By.ID, "input-email")
    user_email.send_keys("dheeraj0297@gmail.com")
    user_telephone = driver.find_element(By.ID, "input-telephone")
    user_telephone.send_keys("7007183451")
    user_password = driver.find_element(By.ID, "input-password")
    user_password.send_keys("admin@12345")
    user_password_confirm = driver.find_element(By.ID, "input-confirm")
    user_password_confirm.send_keys("admin@12345")
    # here user will check the agree check box
    driver.find_element(By.XPATH, "//input[@name ='agree']").click()

    # here user will click on Continue button
    driver.find_element(By.XPATH,"//input[@class ='btn btn-primary']").click()

    time.sleep(5)
    source_page = driver.page_source
    assert "Your Account Has Been Created!" in source_page
    #awsomeqa_registration.pyprint(source_page)

    #assert driver.find_element(By.__text_signature__, "Your Account Has Been Created!")
    #assert driver.page_source == "Your Account Has Been Created!"
    #time.sleep(5)
    #driver.quit()

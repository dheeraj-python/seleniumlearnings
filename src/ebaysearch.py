from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_ebay_site():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")

    search_mini = driver.find_element(By.XPATH, "//input[@id ='gh-ac']")
    time.sleep(5)
    search_mini.send_keys("macmini")
    search_button = driver.find_element(By.XPATH,"//input[@value ='Search']")
    search_button.click()

    time.sleep(5)
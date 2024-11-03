# open a new browser
from selenium import webdriver

def test_open_browser():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    assert driver.title == "CURA Healthcare Service"

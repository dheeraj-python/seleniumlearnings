from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_chr_options():
    # Instantiate the Options class
    chrome_options = Options()  # Correctly instantiate Options
    chrome_options.add_argument("--start-maximized")  # Now this works

    # Create a Service object if needed (optional but recommended)
    service = Service()  # You can specify the path to the ChromeDriver if necessary

    # Pass the options correctly to the Chrome driver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # Don't forget to close the driver after the test
    driver.quit()
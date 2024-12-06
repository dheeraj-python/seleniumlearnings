from selenium import webdriver
from selenium.webdriver.common.by import By


def test_webtable_part01():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")
    #driver.maximize_window()
    #here we want to print all the values available in the web table

    row_elements = driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr")
    row = len(row_elements)
    print(row)

    col_elements = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr[2]/td")
    col = len(col_elements)
    print(col)

    #print the table data

    first_part = "//table[@id='customers']/tbody/tr["
    second_part = "]/td["
    third_part = "]"

    for i in range(2, row + 1):
        for j in range(1, col + 1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            new_data = driver.find_element(By.XPATH,dynamic_path)
            print(new_data, end=" ")



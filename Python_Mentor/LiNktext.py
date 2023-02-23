import time
import selenium
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdrivermanager import ChromeDriverManager

class unknown1:
    def g1(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.flipkart.com/")
        time.sleep(3)
        print(driver.title)
        driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2doB4z']").click()
        time.sleep(3)
        driver.find_element(By.LINK_TEXT,"Top Offers").click()
        time.sleep(3)
        print(driver.title)

f1= unknown1()
f1.g1()




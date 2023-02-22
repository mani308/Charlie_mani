import time
import selenium
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdrivermanager import ChromeDriverManager

class unknown:
    def g1(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.flipkart.com/")
        time.sleep(3)
        driver.find_element(By.XPATH,"//button[@class='_2KpZ6l _2doB4z']").click()
        time.sleep(3)
        driver.find_element(By.NAME,"q").send_keys("mobiles")
        time.sleep(3)
        driver.minimize_window()
        time.sleep(4)
        print("opened paytm")
        driver.close()

f1 = unknown()
f1.g1()




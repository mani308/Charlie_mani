import time
import selenium
import pytest
from selenium import webdriver
from webdrivermanager import ChromeDriverManager

class unknown:
    def g1(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://paytm.com/")
        driver.minimize_window()
        time.sleep(4)
        print("opened paytm")
        driver.close()

f1 = unknown()
f1.g1()
o1=unknown()
o1.g1()




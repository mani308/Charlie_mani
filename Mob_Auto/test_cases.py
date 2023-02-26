from appium import webdriver
from selenium.webdriver.common.by import By
import locators
import pytest
desired_cap = {
  "platformName": "Android",
  "appium:deviceName": "emulator-5554",
  "appium:automationName": "UiAutomator2",
  "appium:appPackage": "com.opsishealth.platefuldev",
  "appium:appWaitActivity": "com.opsis.primary.MainActivity",
  "appium:app": "/home/manikanta/Downloads/plateful-dev.apk"
}
def test_opsys_p1():
  driver= webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
  driver.implicitly_wait(10)
  try:
   srt=driver.find_element(By.XPATH,locators.ele1)
   print(srt.text)
  except Exception as e :
    print(e)

def test_opsys_p2():
  driver= webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
  driver.implicitly_wait(10)



def test_opsys_p2():
  driver= webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
  driver.implicitly_wait(10)



def test_opsys_p2():
  driver= webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
  driver.implicitly_wait(10)

























import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import pytest
from Mob_Auto import locators
from Mob_Auto import TestData

desired_cap = {
  "platformName": "Android",
  "appium:deviceName": "emulator-5554",
  "appium:automationName": "UiAutomator2",
  "appium:appPackage": "com.opsishealth.platefuldev",
  "appium:appWaitActivity": "com.opsis.primary.MainActivity",
  "appium:app": "/home/manikanta/Downloads/plateful-dev.apk"
}

driver= webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
driver.implicitly_wait(10)

def test_DEmo1():
    driver.find_element(By.CLASS_NAME,locators.StartForFree_btn).click()
    time.sleep(2)
    driver.find_element(By.ID,locators.Allow_always).click()
    time.sleep(2)
    driver.find_element(By.XPATH,locators.More).click()
    time.sleep(2)
    t1=TouchAction(driver)
    t1.press(x=524,y=1409).move_to(x=520,y=798).release().perform()
    driver.find_element(By.XPATH,locators.Sign_In).click()
    time.sleep(2)
    SignUP= driver.find_element(By.XPATH,locators.sign_up).text
    assert SignUP == "Sign Up"


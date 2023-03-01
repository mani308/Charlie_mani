import pytest
from appium import webdriver

desired_cap = {
  "platformName": "Android",
  "appium:deviceName": "emulator-5554",
  "appium:automationName": "UiAutomator2",
  "appium:appPackage": "com.opsishealth.platefuldev",
  "appium:appWaitActivity": "com.opsis.primary.MainActivity",
  "appium:app": "/home/manikanta/Downloads/plateful-dev.apk"
}

# @pytest.fixture(autouse='true')
# def prere1():
#   driver= webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
#   driver.implicitly_wait(10)
#   return driver
#   yield
#   pass
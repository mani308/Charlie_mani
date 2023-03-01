import time
from appium import webdriver
import pytest

@pytest.fixture(scope='class')
def setup(request):
  desired_cap = {
    "platformName": "Android",
    "appium:deviceName": "emulator-5554",
    "appium:automationName": "UiAutomator2",
    "appium:appPackage": "com.opsishealth.platefuldev",
    "appium:appWaitActivity": "com.opsis.primary.MainActivity",
    "appium:app": "/home/manikanta/Downloads/plateful-dev.apk"
                }
  driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
  driver.start_client()

  time.sleep(5)

  request.cls.driver = driver

  yield
  driver.quit()
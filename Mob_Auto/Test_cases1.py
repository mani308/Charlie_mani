from appium import webdriver
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
@pytest.mark.home1
def test_opsys_p1():
  driver= webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
  driver.implicitly_wait(10)
  try:
   srt1=driver.find_element(By.XPATH,locators.ele1)
   R_tx1= srt1.text
  except Exception as e :
    print(e)
  assert R_tx1 == TestData.text1

@pytest.mark.home1
def test_opsys_p2():
  driver= webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
  driver.implicitly_wait(10)
  try:
   srt2=driver.find_element(By.XPATH,locators.ele2)
   R_tx2= srt2.text
  except Exception as e :
    print(e)
  assert R_tx2 == TestData.text2
@pytest.mark.home1
def test_opsys_p3():
  driver= webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
  driver.implicitly_wait(10)
  try:
    srt3=driver.find_element(By.XPATH,locators.ele2)
    R_txt3 = srt3.text
  except Exception as e:
    print(e)
  assert R_txt3 == TestData.text3


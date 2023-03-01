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

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
driver.implicitly_wait(10)
@pytest.mark.home1
def test_opsys_h1():
  try:
   srt1=driver.find_element(By.XPATH,locators.ele1)
   R_tx1= srt1.text
   print(R_tx1)
  except Exception as e :
    print(e)
  assert R_tx1 == TestData.text1

@pytest.mark.home1
def test_opsys_h2():
  # driver= webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
  # driver.implicitly_wait(10)
  try:
   srt2=driver.find_element(By.XPATH,locators.ele2)
   R_tx2= srt2.text
  except Exception as e :
    print(e)
  assert R_tx2 == TestData.text2

@pytest.mark.home1
def test_opsys_h3():
  # driver= webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
  # driver.implicitly_wait(10)
  try:
    srt3=driver.find_element(By.XPATH,locators.ele3)
    R_txt3 = srt3.text
  except Exception as e:
    print(e)
  assert R_txt3 == TestData.text3

@pytest.mark.home1
def test_opsys_h4():
  # driver= webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
  # driver.implicitly_wait(10)
  try:
    srt4=driver.find_element(By.XPATH,locators.ele4)
    R_txt4 = srt4.text
  except Exception as e:
    print(e)
  assert R_txt4 == TestData.text4

def test_opsys_h5():
  # driver= webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
  # driver.implicitly_wait(10)
  try:
    srt4=driver.find_element(By.CLASS_NAME,locators.ele5)
    srt4.click()
  except Exception as e:
    print(e)
  try:
    srt5 = driver.find_element(By.ID,locators.ale1)
    srt6 = driver.find_element(By.ID,locators.ale2)
    srt7 = driver.find_element(By.ID,locators.ale3)
    srt8 = driver.find_element(By.ID,locators.ale4)
  except Exception as e:
    print(e)
  assert srt5.text == TestData.text5
  print(srt5.text)
  assert srt6.text == TestData.text6
  print(srt6.text)
  assert srt7.text == TestData.text7
  print(srt7.text)
  assert srt8.text == TestData.text8
  print(srt8.text)

def test_opsys_i1():
  # driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
  # driver.implicitly_wait(10)
  try:
    driver.find_element(By.XPATH,locators.sli2).click()
    h2_food1=driver.find_element(By.XPATH,locators.h2_ele1).text
    print(h2_food1)
    h2_food2=driver.find_element(By.XPATH,locators.h2_ele2).text
    print(h2_food2)
  except Exception as e:
    print(e)

  assert h2_food1 == TestData.h2_tx1
  assert h2_food2 == TestData.h2_tx2

def test_opsys_j1():
  # driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
  # driver.implicitly_wait(10)
  try:
    driver.find_element(By.XPATH,locators.sli3).click()
    h3_food1 = driver.find_element(By.XPATH,locators.h3_ele1).text
    print(h3_food1)
    h3_food2 = driver.find_element(By.XPATH,locators.h3_ele2).text
    print(h3_food2)

  except Exception as e:
    print(e)
    assert h3_food1 == TestData.h3_tx1
    assert h3_food2 == TestData.h3_tx2

def test_opsys_k1():
  # driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
  # driver.implicitly_wait(10)
  try:
   driver.find_element(By.XPATH,locators.sli4).click()

  except Exception as e:
    print(e)


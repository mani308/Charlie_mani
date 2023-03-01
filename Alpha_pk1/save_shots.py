from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import time
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
driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.TextView[1]")



t1=time.strftime("%h_%m_%s_%y_%m_%d")
time.sleep(3)
driver.save_screenshot("/home/manikanta/PycharmProjects/pythonProject_info/Alpha_pk1/shots/file"+t1+".png")




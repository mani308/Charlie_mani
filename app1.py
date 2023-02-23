from appium import webdriver

desired_cap = {
  "appium:deviceName": "emulator 5556",
  "platformName": "Android",
  "appium: appPackage": "com.apidemos",
  "appium: appActivity": "7b625c7 u0 com.touchboarder.android.api.demos/com.touchboarder.androidapidemos.MainActivity",
  "appium: app": "/home/manikanta/Downloads/API Demos for Android_1.9.0_Apkpure.apk"
}

driver= webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)



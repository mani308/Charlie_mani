# import time
# import selenium
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdrivermanager import ChromeDriverManager
#
# class unknown:
#     def g1(self):
#         driver = webdriver.Chrome()
#         driver.maximize_window()
#         driver.get("https://www.flipkart.com/")
#         time.sleep(3)
#         driver.find_element(By.XPATH,"//button[@class='_2KpZ6l _2doB4z']").click()
#         time.sleep(3)
#         l1 = driver.find_elements(By.XPATH,"//a[1]")
#         print(len(l1))
#         driver.find_element(By.NAME,"q").send_keys("mobiles")
#         time.sleep(3)
#         driver.minimize_window()
#         time.sleep(4)
#         print("opened paytm")
#         driver.close()
#         driver.quit()
#     def mul_ele(self):
#      print("inside multiple elements")
#
# f1 = unknown()
# f1.g1()
# f1.mul_ele()
#
# def oust(self):
#     print("outside class")
#
# # oust()
#
#

s1="apple"
s2="ApPlE"

if s1.__eq__(s2):
    print("good to go")
else:
    print("quit")







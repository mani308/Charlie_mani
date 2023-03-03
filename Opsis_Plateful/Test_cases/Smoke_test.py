import time

from selenium.webdriver.common.by import By
from Opsis_Plateful.Ops_Info import Plateful_Testdata
from Opsis_Plateful.Ops_Elements import Locators

class Smoky:
    def __init__(self , driver):
        self.driver = driver

    def verify_launch_page(self):
#1
        try:
            if self.driver.find_element(By.XPATH,Locators.welcome_intropage1).is_displayed():
                print("welcome note is displayed on the introscreen1")
                try:
                    ops_welcome= self.driver.find_element(By.XPATH,Locators.welcome_intropage1).text
                    print(ops_welcome)
                    assert Plateful_Testdata.welcome_note == ops_welcome
                except:
                    print("Welcome to is not matching in intro_screen1")
            else:
                print("Welcome element not displayed on the intro_screen1")
                return False

#2

            if self.driver.find_element(By.XPATH, Locators.plateful_img).is_displayed():
                print("Plateful IMAGE is displayed on the intro_screen1")
            else:
                print("Plateful image is not displayed on the intro_screen1")
                return False

#3
            if  self.driver.find_element(By.XPATH,Locators.health_intropage1).is_displayed():
                print("Health note is displayed on the intro_screen1")
                try:
                    ops_health= self.driver.find_element(By.XPATH,Locators.health_intropage1).text
                    print(ops_health)
                    assert ops_health == Plateful_Testdata.Healthy
                except:
                    print("Healthy eating made easy. Text not matching")
            else:
                print("Healthy eating made easy element not displayed on the intro_screen1")
                return False

#4

            if self.driver.find_element(By.XPATH, Locators.join_the_nutrition).is_displayed():
                print("Health note is displayed on the intro_screen1")
                try:
                    ops_nutrition = self.driver.find_element(By.XPATH, Locators.join_the_nutrition).text
                    print(ops_nutrition)
                    assert ops_nutrition == Plateful_Testdata.join_nutrition
                except:
                    print("Join the nutrition revolution, starting with FoodWise. Text not matching")
            else:
                print("Join the nutrition revolution, starting with FoodWise. element not displayed on the intro_screen1")
                return False

#5

            if self.driver.find_element(By.XPATH, Locators.veggies_img).is_displayed():
                print("Image with all the veggies and fruits are displayed on the intro_screen1")
            else:
                print(" Image with all the vegies and fruits are not displayed on the intro_screen1")
                return False

#6

            if ((self.driver.find_element(By.XPATH, Locators.slide_view2).is_displayed()) & (self.driver.find_element(By.XPATH, Locators.slide_view2).is_enabled())):
                print("slider_button2 is displayed and is enabled on the intro_screen")
                try:
                    self.driver.find_element(By.XPATH, Locators.slide_view2).click()
                    time.sleep(1)
                except:
                    print("slider_button2 is not clickable")


                if((self.driver.find_element(By.XPATH, Locators.slide_view3).is_displayed()) & (self.driver.find_element(By.XPATH, Locators.slide_view3).is_enabled())):
                    print("slider_button3 is displayed and is enabled on the intro_screen")
                    try:
                        self.driver.find_element(By.XPATH, Locators.slide_view3).click()
                        time.sleep(1)
                    except:
                        print("slider_button3 is not clickable")
                else:
                    print("slider_button3 is not displayed and enabled in introscreen")
                    return False


                if ((self.driver.find_element(By.XPATH, Locators.slide_view4).is_displayed()) & (self.driver.find_element(By.XPATH, Locators.slide_view4).is_enabled())):
                    print("slider button4 is displayed and is enabled on the intro_screen")
                    try:
                        self.driver.find_element(By.XPATH, Locators.slide_view4).click()
                        time.sleep(1)
                    except:
                        print("slider_button4 is not clickable")
                else:
                    print("slider_button4 is not displayed and enabled in introscreen")
                    return False


                if ((self.driver.find_element(By.XPATH, Locators.slide_view1).is_displayed()) & (self.driver.find_element(By.XPATH, Locators.slide_view1).is_enabled())):
                    print("slider button1 is displayed and is enabled on the intro_screen")
                    try:
                        self.driver.find_element(By.XPATH, Locators.slide_view1).click()
                        time.sleep(2)
                    except:
                        print("slider_button1 is not clickable")
                else:
                    print("slider_button1 is not displayed and enabled in introscreen")
                    return False

            else:
                print( "slider_button2 is not displayed and enabled in introscreen")
                return False

#7

            if ((self.driver.find_element(By.XPATH, Locators.slide_view2).is_displayed()) & (self.driver.find_element(By.XPATH, Locators.slide_view2).is_enabled())):
                try:
                    self.driver.find_element(By.XPATH, Locators.slide_view2).click()
                    time.sleep(1)
                    if self.driver.find_element(By.XPATH, Locators.foodwise_img).is_displayed():
                        print("FoodWise image is displayed on the intro_screen2")
                    else:
                        print("FoodWise images is not displayed on the intro_screen2")
                        return False
                except:
                    print("slider button 2 is not clickable")
                    return False
            else:
                print("slider button2 is neither displayed nor enabled")
                return False

#8

            if self.driver.find_element(By.XPATH, Locators.Person_scanning).is_displayed():
                print("person scanning a coke tin IMAGE is displayed on the intro_screen2")
            else:
                print("Person scanning a coke tin Image is not displayed on the intro_screen1")
                return False

#9

            if  self.driver.find_element(By.XPATH,Locators.fill_Fridge).is_displayed():
                print("Fill your fridge with goodness is displayed on the intro_screen2")
                try:
                    ops_fridge= self.driver.find_element(By.XPATH,Locators.fill_Fridge).text
                    print(ops_fridge)
                    assert ops_fridge == Plateful_Testdata.fill_fridge
                except:
                    print("Fill your fridge with goodness Text not matching")
            else:
                print("Fill your fridge with goodness element not displayed on the intro_screen2")
                return False

#10

            if  self.driver.find_element(By.XPATH,Locators.scan_healthy).is_displayed():
                print("scan to know how healthy and sustainable your food is Text is displayed on the intro_screen1")
                try:
                    ops_scanHealthy= self.driver.find_element(By.XPATH,Locators.scan_healthy).text
                    print(ops_scanHealthy)
                    assert ops_scanHealthy == Plateful_Testdata.scan_Healthy
                except:
                    print("Scan to know how healthy and sustainable your food is Text not matching")
            else:
                print("scan to know how healthy and sustainable your food is element not displayed on the intro_screen2")
                return False

#11

            if ((self.driver.find_element(By.XPATH, Locators.slide_view3).is_displayed()) & (self.driver.find_element(By.XPATH, Locators.slide_view3).is_enabled())):
                try:
                    self.driver.find_element(By.XPATH, Locators.slide_view3).click()
                    time.sleep(1)
                    if self.driver.find_element(By.XPATH, Locators.smarter).is_displayed():
                        print("Make smarter, science-backed choices text is displayed on the intro_screen2")
                        try :
                            ops_smarter = self.driver.find_element(By.XPATH, Locators.scan_healthy).text
                            print(ops_smarter)
                            assert ops_smarter == Plateful_Testdata.smarter_choice
                            return True
                        except:
                            print("Make smarter, science-backed choices is Text not matching")
                    else:
                        print("Make smarter, science-backed choices is not displayed on the intro_screen2")
                        return False
                except:
                    print("slider button 3 is not clickable")
                    return False
            else:
                print("slider button 3 is neither displayed nor enabled")
                return False




















































        except:
            print("exception occured in Intro pages")






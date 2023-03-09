import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from Opsis_Plateful.Ops_Info import Plateful_Testdata
from Opsis_Plateful.Ops_Elements import Locators

class Smoky:
    def __init__(self , driver):
        self.driver = driver

    def Scroller(self):
        scroll=TouchAction(self.driver)
        return scroll
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
                print("Health eating note is displayed on the intro_screen1")
                try:
                    ops_health= self.driver.find_element(By.XPATH,Locators.health_intropage1).text
                    print(ops_health)
                    assert ops_health == Plateful_Testdata.Healthy
                except:
                    print("Healthy eating made easy. Text not matching")
            else:
                print("Healthy eating made easy element not displayed on the intro_screen1")
                return False




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
                except:
                    print("slider_button2 is not clickable")


                if((self.driver.find_element(By.XPATH, Locators.slide_view3).is_displayed()) & (self.driver.find_element(By.XPATH, Locators.slide_view3).is_enabled())):
                    print("slider_button3 is displayed and is enabled on the intro_screen")
                    try:
                        self.driver.find_element(By.XPATH, Locators.slide_view3).click()
                    except:
                        print("slider_button3 is not clickable")
                else:
                    print("slider_button3 is not displayed and enabled in introscreen")
                    return False


                if ((self.driver.find_element(By.XPATH, Locators.slide_view4).is_displayed()) & (self.driver.find_element(By.XPATH, Locators.slide_view4).is_enabled())):
                    print("slider button4 is displayed and is enabled on the intro_screen")
                    try:
                        self.driver.find_element(By.XPATH, Locators.slide_view4).click()
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
                print("Scan over two million foods to know how healthy and sustainable your food is Text is displayed on the intro_screen1")
                try:
                    ops_scanHealthy= self.driver.find_element(By.XPATH,Locators.scan_healthy).text
                    print(ops_scanHealthy)
                    assert ops_scanHealthy == Plateful_Testdata.scan_Healthy
                except:
                    print("Scan over two million foods to know Text not matching")
            else:
                print("Scan over two million foods to know element not displayed on the intro_screen2")
                return False

#11

            if ((self.driver.find_element(By.XPATH, Locators.slide_view3).is_displayed()) & (self.driver.find_element(By.XPATH, Locators.slide_view3).is_enabled())):
                try:
                    self.driver.find_element(By.XPATH, Locators.slide_view3).click()
                    if self.driver.find_element(By.XPATH, Locators.smarter).is_displayed():
                        print("Make smarter, science-backed choices text is displayed on the intro_screen3")
                        try :
                            ops_smarter = self.driver.find_element(By.XPATH, Locators.smarter).text
                            print(ops_smarter)
                            assert ops_smarter == Plateful_Testdata.smarter_choice
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

#12

            if  self.driver.find_element(By.XPATH,Locators.healthy_planet).is_displayed():
                print("Eat for your health and the health of the planet. is displayed on the intro_screen1")
                try:
                    ops_Eatforyourplanet= self.driver.find_element(By.XPATH,Locators.healthy_planet).text
                    print(ops_Eatforyourplanet)
                    assert ops_Eatforyourplanet == Plateful_Testdata.healthy_Planet
                except:
                    print("Eat for your health and the health of the planet. Text not matching")
            else:
                print("Eat for your health and the health of the planet. not displayed on the intro_screen2")
                return False

#13

            if self.driver.find_element(By.XPATH, Locators.fetch_nutritionimg).is_displayed():
                print("Fetching Nutrition values IMAGE is displayed on the intro_screen1")
            else:
                print("Fetching Nutrition values IMAGE is not displayed on the intro_screen1")
                return False


#14

            if ((self.driver.find_element(By.XPATH, Locators.slide_view4).is_displayed()) & (self.driver.find_element(By.XPATH, Locators.slide_view4).is_enabled())):
                try:
                    self.driver.find_element(By.XPATH, Locators.slide_view4).click()
                    if self.driver.find_element(By.XPATH, Locators.plateful_img1).is_displayed():
                        print("Plateful IMAGE is displayed on the intro_screen4")
                    else:
                        print("Plateful IMAGE is not displayed on the intro_screen4")
                        return False
                except:
                    print("slider button 4 is not clickable")
                    return False
            else:
                print("slider button 4 is neither displayed nor enabled")
                return False



#15 Start for free

            if ((self.driver.find_element(By.CLASS_NAME,Locators.StartForFree_btn).is_displayed()) & (self.driver.find_element(By.CLASS_NAME,Locators.StartForFree_btn).is_enabled())):
                print("start for free button is enabled and displayed in the intro page")
            else:
                print("slider button2 is neither displayed nor enabled")
                return False

#16

            if  self.driver.find_element(By.XPATH,Locators.startforfree_txt).is_displayed():
                print("Start For Free is displayed on the intro_screen")
                try:
                    ops_start= self.driver.find_element(By.XPATH,Locators.startforfree_txt).text
                    print(ops_start)
                    assert ops_start == Plateful_Testdata.start
                    return True
                except:
                    print("Start for free Text not matching")
            else:
                print("Start for free text not displayed on the intro_screen")
                return False

        except:
            print("exception occured in Intro pages")

    def verify_cameraaccess(self):

        try:
            if (self.driver.find_element(By.CLASS_NAME, Locators.StartForFree_btn).is_displayed()):
                try:
                    self.driver.find_element(By.CLASS_NAME, Locators.StartForFree_btn).click()
                    time.sleep(2)
                    if self.driver.find_element(By.ID, Locators.Camcorder_logo).is_displayed():
                        print("Camcorder_logo is displayed ")
                    else:
                        print("Camcorder_logo logo is not displayed")
                        return False
                except:
                    print("element not clickable exception occurred")
            else:
                print("camcorder logo is not displayed after clicking on start for free button")



            if  self.driver.find_element(By.XPATH,Locators.allow_camera).is_displayed():
                print("Allow PlatefulDev to take pictures and record video? is displayed in the camera_access screen")
                try:
                    ops_AllowCamera= self.driver.find_element(By.XPATH,Locators.allow_camera).text
                    (ops_AllowCamera.lower())
                    assert ops_AllowCamera == Plateful_Testdata.Allow_platefulDev
                except:
                    print("Allow PlatefulDev to take pictures and record video? text not matching")
            else:
                print("Allow PlatefulDev to take pictures and record video? is not displayed in the page")
                return False

#while

            if  self.driver.find_element(By.ID,Locators.Allow_always).is_displayed():
                print("While using the app is displayed in the camera_access screen")
                try:
                    ops_AllowCameraalways= self.driver.find_element(By.ID,Locators.Allow_always).text
                    print(ops_AllowCameraalways)
                    assert ops_AllowCameraalways.lower() == Plateful_Testdata.Allow_while.lower()
                except:
                    print("While using the app text not matching")
            else:
                print("While using the app is not displayed in the page")
                return False

#once

            if  self.driver.find_element(By.ID,Locators.Allow_only).is_displayed():
                print("Only this time is displayed in the camera_access screen")
                try:
                    ops_AllowCameraonly= self.driver.find_element(By.ID,Locators.Allow_only).text
                    print(ops_AllowCameraonly)
                    assert ops_AllowCameraonly.lower() == Plateful_Testdata.Allow_once.lower()
                except:
                    print("Only this time text not matching")
            else:
                print("Only this time is not displayed in the page")
                return False

#deny

            if  self.driver.find_element(By.ID,Locators.restrict_camera).is_displayed():
                print("Dont allow is displayed in the camera_access screen")
                try:
                    ops_Denycamera= self.driver.find_element(By.ID,Locators.restrict_camera).text
                    print(ops_Denycamera)
                    assert ops_Denycamera.lower() == Plateful_Testdata.Dont_allow.lower()
                    return True
                except:
                    print("dont allow text not matching")
            else:
                print("dont allow is not displayed in the page")
                return False

        except:
            print("exception occured in giving permissions")



    def verify_homepage(self):

        try:
            try:
                self.driver.find_element(By.ID,Locators.Allow_always).click()
                if self.driver.find_element(By.XPATH,Locators.Barcode).is_displayed():
                        print("you are in landing page")
                else:
                        print("you are not in landing page")
                        return False
            except:
                    print("While using the app click not working")



            if  self.driver.find_element(By.XPATH,Locators.Plate).is_displayed():
                print("Plate text is present in the scanning page")
                try:
                    ops_plate= self.driver.find_element(By.XPATH,Locators.Plate).text
                    ops_barcode= self.driver.find_element(By.XPATH,Locators.Barcode).text
                    print(ops_plate)
                    print(ops_barcode)
                    assert ops_plate == Plateful_Testdata.PLate
                    assert ops_barcode == Plateful_Testdata.BArcode
                except:
                    print("Plate and barcode text not present in landing page")
            else:
                print("Plate and barcode are not displayed in the page")
                return False



            if self.driver.find_element(By.XPATH, Locators.Flash_OnOff).is_displayed():
                print("Flash light button is displayed in the Scan page")
            else:
                print("Flash light button is not displayed in the Scan page")
                return False


            if (self.driver.find_element(By.XPATH, Locators.History).is_displayed() & self.driver.find_element(By.XPATH, Locators.More).is_displayed()) :
                print("History and more txt is displayed in the scanning page")
                try:
                    ops_history = self.driver.find_element(By.XPATH, Locators.History).text
                    ops_more = self.driver.find_element(By.XPATH, Locators.More).text
                    print(ops_history)
                    print(ops_more)
                    assert ops_history == Plateful_Testdata.HIstory
                    assert ops_more == Plateful_Testdata.MOre
                    return True
                except:
                    print("History and more text not present in Scanning page")
            else:
                print("History and more text are not displayed in the scanning page")
                return False
        except:
            print("exception occured")



    def Verify_HistoryPage(self):
        try:
            if (self.driver.find_element(By.XPATH,Locators.History).is_displayed()):
                try:
                    self.driver.find_element(By.XPATH,Locators.History).click()
                    time.sleep(2)
                    if self.driver.find_element(By.XPATH, Locators.Food).is_displayed():
                        print("you are in History Page")
                    else:
                        print("You are not in history page")
                        return False
                except:
                    print("Clicking on history not working")
            else:
                print("History button is not displayed in the home screen")


            if  self.driver.find_element(By.XPATH,Locators.Food).is_displayed():
                print("Food is displayed on the history page")
                try:
                    ops_Food= self.driver.find_element(By.XPATH,Locators.Food).text
                    print(ops_Food)
                    assert ops_Food == Plateful_Testdata.FOod
                except:
                    print("Food Text not matching")
            else:
                print("Food is not displayed on the history page")
                return False



            if  self.driver.find_element(By.XPATH,Locators.Nutrition_value).is_displayed():
                print("NUTRITION VALUE is displayed in the history page")
                try:
                    ops_nutrition= self.driver.find_element(By.XPATH,Locators.Nutrition_value).text
                    print(ops_nutrition)
                    assert ops_nutrition == Plateful_Testdata.NUtrition_VAlue
                except:
                    print("NUTRITION VALUE Text not matching")
            else:
                print("NUTRITION VALUE is not displayed in the history page")
                return False



            if  self.driver.find_element(By.XPATH,Locators.Eco_value).is_displayed():
                print("ECO VALUE is displayed in the history page")
                try:
                    ops_eco= self.driver.find_element(By.XPATH,Locators.Eco_value).text
                    print(ops_eco)
                    assert ops_eco == Plateful_Testdata.ECo_Value
                    return True
                except:
                    print("ECO VALUE Text not matching")
            else:
                print("ECO VALUE is not displayed in the history page")
                return False

        except:
            print("exception occured")

    def Verify_MorePage(self):
        try:
            if (self.driver.find_element(By.XPATH,Locators.More).is_displayed()):
                try:
                    self.driver.find_element(By.XPATH,Locators.More).click()
                    if self.driver.find_element(By.XPATH,Locators.More_Logo).is_displayed():
                        More_text = self.driver.find_element(By.XPATH,Locators.More_Logo).text
                        print(More_text)
                        assert More_text == Plateful_Testdata.MoRe
                    else:
                        print("You are not in More page")
                        return False
                except:
                    print("More button is not clickable")
            else:
                print("More button is not displayed in the home screen")

#Help

            if  self.driver.find_element(By.XPATH,Locators.Help).is_displayed():
                print("Help text is displayed in the more screen")
                try:
                    ops_Help= self.driver.find_element(By.XPATH,Locators.Help).text
                    print(ops_Help)
                    assert ops_Help == Plateful_Testdata.HeLp
                except:
                    print("Help Text not matching")

                try:
                    ops_welcomE = self.driver.find_element(By.XPATH,Locators.Welcome_to_plateful).text
                    print(ops_welcomE)
                    assert ops_welcomE == Plateful_Testdata.Welcome_To_Plateful
                except:
                    print("Welcome to Plateful Text not matching")

                try:
                    ops_howit= self.driver.find_element(By.XPATH,Locators.How_it).text
                    print(ops_howit)
                    assert ops_howit == Plateful_Testdata.How_It
                except:
                    print("How It Works Text not matching")

                try:
                    ops_frequent = self.driver.find_element(By.XPATH, Locators.Frequent).text
                    print(ops_frequent)
                    assert ops_frequent == Plateful_Testdata.FrequenT
                except:
                    print("Frequently Asked Questions Text not matching")

                try:
                    ops_contactus= self.driver.find_element(By.XPATH,Locators.Contact_us).text
                    print(ops_contactus)
                    assert ops_contactus == Plateful_Testdata.Contact_Us
                except:
                    print("Contact Us Text not matching")

                try:
                    ops_support= self.driver.find_element(By.XPATH,Locators.Support).text
                    print(ops_support)
                    assert ops_support == Plateful_Testdata.SupporT
                except:
                    print("Support Text not matching")

            else:
                print("Help is not displayed in the more page")
                return False

#DataPrivacy

            if  self.driver.find_element(By.XPATH,Locators.Data_privacy).is_displayed():
                print("Data Privacy is displayed in the more page")
                try:
                    ops_dataprivacy= self.driver.find_element(By.XPATH,Locators.Data_privacy).text
                    print(ops_dataprivacy)
                    assert ops_dataprivacy == Plateful_Testdata.Data_Privacy
                except:
                    print("Data Privacy Text not matching")

                try:
                    ops_termscondtions= self.driver.find_element(By.XPATH,Locators.terms_conditions).text
                    print(ops_termscondtions)
                    assert ops_termscondtions == Plateful_Testdata.Terms_Conditions
                except:
                    print("Data Privacy Text not matching")

                try:
                    ops_privacypolicy = self.driver.find_element(By.XPATH,Locators.Privacy_policy).text
                    print(ops_privacypolicy)
                    assert ops_privacypolicy == Plateful_Testdata.Privacy_Policy
                except:
                    print("Privacy Policy Text not matching")

            else:
                print("Privacy Policy is not displayed on the history page")
                return False

#Account

            if  self.driver.find_element(By.XPATH,Locators.Account).is_displayed():
                print("Account text displayed on the More page")
                try:
                    ops_Account= self.driver.find_element(By.XPATH,Locators.Account).text
                    print(ops_Account)
                    self.Scroller().press(x=520,y=1409).move_to(x=520,y=789).release().perform()
                    assert ops_Account == Plateful_Testdata.Account
                except:
                    print("Account Text not matching in more page")
            else:
                print("SignIn Text is not displayed on the More page")
                return False


            if self.driver.find_element(By.XPATH, Locators.Sign_In).is_displayed():
                    print("SignIn is displayed on the intro_screen")
                    try:
                        ops_SIGNin = self.driver.find_element(By.XPATH, Locators.Sign_In).text
                        print(ops_SIGNin)
                        assert ops_SIGNin == Plateful_Testdata.sign_IN
                    except:
                        print("SignIn Text not matching")
            else:
                    print("SignIn is not displayed on the intro_screen")
                    return False

#Welome to plateful Page navigation
            #
            if ((self.driver.find_element(By.XPATH, Locators.Welcome_to_plateful).is_displayed()) & (self.driver.find_element(By.XPATH, Locators.Welcome_to_plateful).is_enabled())):
                try:
                    self.driver.find_element(By.XPATH, Locators.Welcome_to_plateful).click()
                    time.sleep(1)

                    if self.driver.find_element(By.XPATH, Locators.join_the_nutrition).is_displayed():
                        print("we landed in welcome to Plateful page ")
                        time.sleep(2)
                    else:
                        print("We are not in welcome to plateful page")
                        return False

                    if self.driver.find_element(By.XPATH, Locators.Welome_cancel).is_displayed():
                        try :
                            self.driver.find_element(By.XPATH, Locators.Welome_cancel).click()
                        except:
                            print("Cancel button is not clickable in welcome to page")
                    else:
                        print("cancel button is not displayed in the welcome page")
                except:
                    print("Welcome to plateful page is not clickable")
                    return False


            if ((self.driver.find_element(By.XPATH, Locators.How_it).is_displayed()) & self.driver.find_element(By.XPATH, Locators.How_it).is_enabled()):
                try:
                    self.driver.find_element(By.XPATH, Locators.How_it).click()
                    time.sleep(1)

                    if self.driver.find_element(By.XPATH, Locators.plateful_swaps_fuzzy).is_displayed():
                        print("we landed in How it works page ")
                        time.sleep(2)
                    else:
                        print("we are not landed in how it works page ")
                        return False

                    if self.driver.find_element(By.XPATH, Locators.How_it_cancel).is_displayed():
                        try:
                            self.driver.find_element(By.XPATH, Locators.How_it_cancel).click()
                        except:
                            print("Cancel button is not clickable and not present in how it works page")
                    else:
                        print("cancel button is not displayed in the how it works page")

                except:
                    print("how it works page is not clickable")
                    return False



            if ((self.driver.find_element(By.XPATH, Locators.Frequent).is_displayed()) & self.driver.find_element(By.XPATH, Locators.Frequent).is_enabled()):
                try:
                    self.driver.find_element(By.XPATH, Locators.Frequent).click()
                    time.sleep(1)

                    if self.driver.find_element(By.XPATH, Locators.you_have_questions).is_displayed():
                        print("we landed in Frequently asked questions page")
                        time.sleep(2)
                    else:
                        print("we are not landed in frequently asked questions page")
                        return False

                    if self.driver.find_element(By.XPATH, Locators.Faq_done).is_displayed():
                        try:
                            self.driver.find_element(By.XPATH, Locators.Faq_done).click()
                        except:
                            print("Done button is not clickable and not present in Frequently asked questions page")
                    else:
                        print("Done button is not displayed in Frequently asked questions page")

                except:
                    print("Welcome to page is not clickable")
                    return False



            if ((self.driver.find_element(By.XPATH, Locators.Contact_us).is_displayed()) & self.driver.find_element(By.XPATH, Locators.Contact_us).is_enabled()):
                try:
                    self.driver.find_element(By.XPATH, Locators.Contact_us).click()
                    time.sleep(1)
                    if self.driver.find_element(By.XPATH, Locators.contact_fn).is_displayed():
                        print("we landed in contact us page ")
                        time.sleep(2)
                    else:
                        print("we are not landed in contact us page")
                        return False

                    if self.driver.find_element(By.XPATH, Locators.contact_cancel).is_displayed():
                        try:
                            self.driver.find_element(By.XPATH, Locators.contact_cancel).click()
                        except:
                            print("Cancel button is not clickable and not present in ContactUs page")
                    else:
                        print("cancel button is not displayed in the ContactUS page")

                except:
                    print("Contact us page is not clickable")
                    return False



            if ((self.driver.find_element(By.XPATH, Locators.Support).is_displayed()) & self.driver.find_element(By.XPATH, Locators.Support).is_enabled()):
                try:
                    self.driver.find_element(By.XPATH, Locators.Support).click()
                    time.sleep(1)

                    if self.driver.find_element(By.XPATH, Locators.support_page).is_displayed():
                        print("we landed in Support Page")
                        time.sleep(2)
                    else:
                        print("we are not landed in Support Page")
                        return False

                    if self.driver.find_element(By.XPATH, Locators.support_cancel).is_displayed():
                        try:
                            self.driver.find_element(By.XPATH, Locators.support_cancel).click()
                        except:
                            print("Cancel button is not clickable and not present in Support page")
                    else:
                        print("cancel button is not displayed in the Support page")

                except:
                    print("Support page is not clickable")
                    return False


            if ((self.driver.find_element(By.XPATH, Locators.terms_conditions).is_displayed()) & self.driver.find_element(By.XPATH, Locators.terms_conditions).is_enabled()):
                try:
                    self.driver.find_element(By.XPATH, Locators.terms_conditions).click()
                    time.sleep(1)

                    if self.driver.find_element(By.XPATH, Locators.TC_page).is_displayed():
                        print("we landed in Terms And Conditions Page")
                        time.sleep(2)
                    else:
                        print("we are not landed in Terms And Conditions Page")
                        return False

                    if self.driver.find_element(By.XPATH, Locators.TC_cancel).is_displayed():
                        try:
                            self.driver.find_element(By.XPATH, Locators.TC_cancel).click()
                        except:
                            print("Cancel button is not clickable and not present in Terms And Conditions page")
                    else:
                        print("cancel button is not displayed in the Terms And Conditions page")

                except:
                    print("Terms And Conditions page is not clickable")
                    return False


            if ((self.driver.find_element(By.XPATH, Locators.Privacy_policy).is_displayed()) & self.driver.find_element(By.XPATH, Locators.Privacy_policy).is_enabled()):
                try:
                    self.driver.find_element(By.XPATH, Locators.Privacy_policy).click()
                    time.sleep(1)

                    if self.driver.find_element(By.XPATH, Locators.privacypolicy_page).is_displayed():
                        print("we landed in Privacy Policy page")
                        time.sleep(2)
                    else:
                        print("We are not landed in Privacy Policy Page")
                        return False

                    if self.driver.find_element(By.XPATH, Locators.privacypolicy_cancel).is_displayed():
                        try:
                            self.driver.find_element(By.XPATH, Locators.privacypolicy_cancel).click()
                            print("cancel button is working ")
                            time.sleep(3)
                            self.Scroller().press(x=524, y=1409).move_to(x=524, y=788).release().perform()
                            time.sleep(3)
                            return True
                        except:
                            print("Cancel button is not clickable and not present in Privacy Policy page")
                    else:
                        print("cancel button is not displayed in the Privacy Policy page")

                except:
                    print("Privacy Policy page is not clickable")
                    return False
        except:
            print("exception occured")



    def Verify_SigningPage(self):

        try:
            if (self.driver.find_element(By.XPATH,Locators.Sign_In).is_displayed()):
                print("SignIn is Displayed in the more page")
                try:
                    self.driver.find_element(By.XPATH,Locators.Sign_In).click()
                    if self.driver.find_element(By.XPATH,Locators.PlateFul_Logo).is_displayed():
                        print("We are in Plateful Signing Page")
                        return True
                    else:
                        print("We are Not in Plateful Signing Page")
                        return False
                except:
                    print("Exception occured while clicking on Signin buttom")
            else:
                print("Sign in not displayed in the home screen")
        except:
            print("Exception occured")
















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
                    print("Welcome to is not matching in introscreen1")
            else:
                print("Welcome element not displayed on the introscreen1")
                return False

#2

            if self.driver.find_element(By.XPATH, Locators.plateful_img).is_displayed():
                print("Plateful IMAGE is displayed on the introscreen1")
            else:
                print("Plateful image is not displayed on the introscreen1")
                return False

#3
            if  self.driver.find_element(By.XPATH,Locators.health_intropage1).is_displayed():
                print("Health note is displayed on the introscreen1")
                try:
                    ops_health= self.driver.find_element(By.XPATH,Locators.health_intropage1).text
                    print(ops_health)
                    assert ops_health == Plateful_Testdata.Healthy
                except:
                    print("Healthy eating made easy. Text not matching")
            else:
                print("Healthy eating made easy element not displayed on the intro screen1")
                return False

#4

            if self.driver.find_element(By.XPATH, Locators.join_the_nutrition).is_displayed():
                print("Health note is displayed on the screen")
                try:
                    ops_nutrition = self.driver.find_element(By.XPATH, Locators.join_the_nutrition).text
                    print(ops_nutrition)
                    assert ops_nutrition == Plateful_Testdata.join_nutrition
                    return True
                except:
                    print("Join the nutrition revolution, starting with FoodWise. Text not matching")
            else:
                print("Join the nutrition revolution, starting with FoodWise. element not displayed on the introscreen1")
                return False

#5

            if self.driver.find_element(By.XPATH, Locators.join_the_nutrition).is_displayed():
                print("Health note is displayed on the screen")
                try:
                    ops_nutrition = self.driver.find_element(By.XPATH, Locators.join_the_nutrition).text
                    print(ops_nutrition)
                    assert ops_nutrition == Plateful_Testdata.join_nutrition
                    return True
                except:
                    print("Join the nutrition revolution, starting with FoodWise. Text not matching")
            else:
                print(
                    "Join the nutrition revolution, starting with FoodWise. element not displayed on the introscreen1")
                return False



            if self.driver.find_element(By.XPATH, Locators.join_the_nutrition).is_displayed():
                print("Health note is displayed on the screen")
                try:
                    ops_nutrition = self.driver.find_element(By.XPATH, Locators.join_the_nutrition).text
                    print(ops_nutrition)
                    assert ops_nutrition == Plateful_Testdata.join_nutrition
                    return True
                except:
                    print("Join the nutrition revolution, starting with FoodWise. Text not matching")
            else:
                print(
                    "Join the nutrition revolution, starting with FoodWise. element not displayed on the introscreen1")
                return False



            if self.driver.find_element(By.XPATH, Locators.join_the_nutrition).is_displayed():
                print("Health note is displayed on the screen")
                try:
                    ops_nutrition = self.driver.find_element(By.XPATH, Locators.join_the_nutrition).text
                    print(ops_nutrition)
                    assert ops_nutrition == Plateful_Testdata.join_nutrition
                    return True
                except:
                    print("Join the nutrition revolution, starting with FoodWise. Text not matching")
            else:
                print(
                    "Join the nutrition revolution, starting with FoodWise. element not displayed on the introscreen1")
                return False



            if self.driver.find_element(By.XPATH, Locators.join_the_nutrition).is_displayed():
                print("Health note is displayed on the screen")
                try:
                    ops_nutrition = self.driver.find_element(By.XPATH, Locators.join_the_nutrition).text
                    print(ops_nutrition)
                    assert ops_nutrition == Plateful_Testdata.join_nutrition
                    return True
                except:
                    print("Join the nutrition revolution, starting with FoodWise. Text not matching")
            else:
                print(
                    "Join the nutrition revolution, starting with FoodWise. element not displayed on the introscreen1")
                return False



            if self.driver.find_element(By.XPATH, Locators.join_the_nutrition).is_displayed():
                print("Health note is displayed on the screen")
                try:
                    ops_nutrition = self.driver.find_element(By.XPATH, Locators.join_the_nutrition).text
                    print(ops_nutrition)
                    assert ops_nutrition == Plateful_Testdata.join_nutrition
                    return True
                except:
                    print("Join the nutrition revolution, starting with FoodWise. Text not matching")
            else:
                print(
                    "Join the nutrition revolution, starting with FoodWise. element not displayed on the introscreen1")
                return False



            if self.driver.find_element(By.XPATH, Locators.join_the_nutrition).is_displayed():
                print("Health note is displayed on the screen")
                try:
                    ops_nutrition = self.driver.find_element(By.XPATH, Locators.join_the_nutrition).text
                    print(ops_nutrition)
                    assert ops_nutrition == Plateful_Testdata.join_nutrition
                    return True
                except:
                    print("Join the nutrition revolution, starting with FoodWise. Text not matching")
            else:
                print(
                    "Join the nutrition revolution, starting with FoodWise. element not displayed on the introscreen1")
                return False



            if self.driver.find_element(By.XPATH, Locators.join_the_nutrition).is_displayed():
                print("Health note is displayed on the screen")
                try:
                    ops_nutrition = self.driver.find_element(By.XPATH, Locators.join_the_nutrition).text
                    print(ops_nutrition)
                    assert ops_nutrition == Plateful_Testdata.join_nutrition
                    return True
                except:
                    print("Join the nutrition revolution, starting with FoodWise. Text not matching")
            else:
                print(
                    "Join the nutrition revolution, starting with FoodWise. element not displayed on the introscreen1")
                return False






























































        except:
            print("exception occured in Intro pages")






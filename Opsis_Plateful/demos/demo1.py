# def verify_launch_page(self):
#     try:
#         if self.driver.find_element(By.XPATH, Locators.welcome_intropage1).is_displayed():
#             print("welcome note is displayed on the screen")
#             try:
#                 ops_welcome = self.driver.find_element(By.XPATH, Locators.welcome_intropage1).text
#                 print(ops_welcome)
#                 assert Plateful_Testdata.welcome_note == ops_welcome
#                 return True
#             except:
#                 print("Welcome to is not matching")
#         else:
#             print("Welcome element not displayed")
#
#             try:
#                 if self.driver.find_element(By.XPATH, Locators.health_intropage1).is_displayed():
#                     print("Health note is displayed on the screen")
#                     try:
#                         ops_health = self.driver.find_element(By.XPATH, Locators.health_intropage1).text
#                         print(ops_health)
#                         assert ops_health == Plateful_Testdata.Healthy
#                         return True
#                     except:
#                         print("Text not matching")
#                         return False
#                 else:
#                     print("Healthy eating made easy element not displayed")
#                     return False
#             except:
#                 print("mismatch in healthy eating made easy")

import pytest
from Opsis_Plateful.Test_cases.Smoke_test import Smoky
import allure
@pytest.mark.usefixtures("setup")
class Test_block:
    @pytest.fixture(autouse = True)
    def Pre_setup(self):
        """
        Creating the object and passing appium webdriver instance into it, var_name = driver
        :return: none
        """
        self.smoketest = Smoky(self.driver)

    def test_verify_launch_page(self):
        """This test will verify the elements and functionality present on the launch page"""
        assert self.smoketest.verify_launch_page()


    def test_verify_cameraacesspage(self):
        """this test will verify all the camera access elements and functionalities"""
        assert self.smoketest.verify_cameraaccess()



    def test_verify_homepage(self):
        """this test will verify all whether we are in the landing page or not """
        assert self.smoketest.verify_homepage()


    def test_verify_historypage(self):
        """this test will verify all the elements present in the history page """
        assert self.smoketest.Verify_HistoryPage()

    def test_verify_morepage(self):
        """this test will verify all the elements in the More Page"""
        assert self.smoketest.Verify_MorePage()










import pytest
from Opsis_Plateful.Test_cases.Smoke_test import Smoky
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
        """this test will verify whether we are in the scan page or not and check all the functionalities in homepage"""
        assert self.smoketest.verify_homepage()


    def test_verify_historypage(self):
        """this test will verify whether we are in the history page or not and check all the functionalities in history page"""
        assert self.smoketest.Verify_HistoryPage()


    def test_verify_morepage(self):
        """this test will verify whether we are in the More page or not and check all the functionalities in More page"""
        assert self.smoketest.Verify_MorePage()


    def test_verify_signingpage(self):
        """
        this test will verify login and signup users and verify all the elements and functionalities in signup and login page
        """
        assert self.smoketest.Verify_SigningPage()






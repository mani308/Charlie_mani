import pytest
from Opsis_Plateful.page.Smoke_test import Smoky

@pytest.mark.usefixtures("setup")
class Test_block:
    @pytest.fixture(autouse = True)
    def Pre_setup(self):
        self.smoketest = Smoky(self.driver)

    def test_verify_launch_page(self):
        assert self.smoketest.verify_launch_page()

    # def test_verify_barcode_page(self):
    #     pass








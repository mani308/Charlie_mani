import pytest
import webdrivermanager
from pytest_html_reporter import attach

from selenium import webdriver
from webdrivermanager import chrome

driver =webdrivermanager.chrome
@pytest.mark.sanity
def test_jhonny():
    print("jhonny is playing volleyball")
def test_rani():
    print("rani is playing khokho")
    assert 2+1 ==5

@pytest.fixture()
def test_label1():
    print("inside labelling")

@pytest.mark.shark
def test_label2(test_label1):
    print("inside labellingshark")

def test_label3():
    print("inside labelling")


def test_Tiger(self):
    print("tiger in pune")
    attach(data=self.driver.get_screenshot_as_png())

def test_lion():
    print("lion hunts")
    assert "gingle"=="gingle"

def test_rabbit(self):
    print("rabbit matrix")
    assert "jennath234"== "koun123"
    attach(data=self.driver.get_screenshot_as_png())










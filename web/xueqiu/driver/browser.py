from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.android.webdriver import WebDriver


class Browser(object):
    browser:WebDriver
    @classmethod
    def _chrome(cls):
        cls.browser=webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
        return cls.browser

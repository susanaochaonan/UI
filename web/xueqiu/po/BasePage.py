from selenium.webdriver import DesiredCapabilities


from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver

from web.xueqiu.driver.browser import Browser


class BasePage(object):

    def __init__(self):
        self.driver:WebDriver=Browser.browser




from selenium.webdriver.android import webdriver
from selenium.webdriver.android.webdriver import WebDriver

from web.xueqiu.driver.browser import Browser
from web.xueqiu.po.homePage import HomePage


class Web(object):
    @classmethod
    def tohome(self) ->webdriver:
        self.driver=Browser._chrome()
        self.driver.maximize_window()
        self.driver.get("https://xueqiu.com/")
        self.driver.implicitly_wait(10)
        return HomePage()


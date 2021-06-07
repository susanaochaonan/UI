from selenium.webdriver.android import webdriver

from web.xueqiu.po.BasePage import BasePage
from web.xueqiu.po.SearchPage import SearchPage
import time

class HomePage(BasePage):
    # def __init__(self):
    #     home=HomePage()
    #     home._open_xueqiu()
    def search(self,key):
        self.driver.find_element_by_name('q').send_keys(key)
        time.sleep(1)
        self.driver.find_element_by_css_selector('button[type="button"]').click()
        time.sleep(1)
        return SearchPage()
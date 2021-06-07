import pytest
import selenium
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver

from web.xueqiu.po.homePage import HomePage
from web.xueqiu.po.Web import Web
import time


class TestDemo(object):

    # def setup(self):
    #     self.driver=webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(10)
    #     self.driver.get("https://xueqiu.com/")
    #     self.home=HomePage(self.driver)


    def setup_method(self):
        self.driver=Web.tohome()
        print('init!!!!!')



    def test_add_stock(self):
        self.driver.search('alibaba').add_stock("BABA").login_wimdow_close()
    # def test_profile(self):
    #     self.driver.add_cookie({"name": "Hm_lpvt_1db88642e346389874251b5a1eded6e3","value":"1619766547"})
    #     self.driver.add_cookie({"name": "xq_a_token", "value": "590435a0841a58c25c4fd6714d01667db2f0299d"})
    #     self.driver.add_cookie({"name": "xq_id_token", "value": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjgzNjEwODU3OTIsImlzcyI6InVjIiwiZXhwIjoxNjIyMzU1OTEyLCJjdG0iOjE2MTk3NjM5MTI2MTQsImNpZCI6ImQ5ZDBuNEFadXAifQ.fthjrViOhQWYmf26fzZjGiaU9JOHoafsUvmSVj2CJsV6H5X-qmhgWJ1HukRtF5eg6wo2lvVgY-CuKsJe4gbnIqi0z_prAALEecTLZYyuMoUW-bvb1xcWwK0PDfvQlS8_wq2T7EuXMKB1z12RFVOHbcIl3-AZrcr2ATu1mKwjeEs0Tn08u29iUCu0TOjC7OCLcxufeyoqtw1CvyYrdFMmcgfFtTxyZbGfJ33tJmzQ9BUOdEP9MzpPH_L78l1bWUYP7XyPxupa8b_jFAYpJawFWc4o0V8fJW-XdgVddcRcA4fNCjRLKhwbcPK3d2m7PEgyny7WKjVLYMCL6B9kd2G5Rg"})
    #     self.driver.add_cookie({"name": "xqat", "value": "590435a0841a58c25c4fd6714d01667db2f0299d"})
    #     self.driver.add_cookie({"name": "xq_r_token", "value": "ea00df53a0ef7353ee5b934984ec5b0de6f23788"})
    #     self.driver.add_cookie({"name": "xq_is_login", "value": "1"})
    #     self.driver.add_cookie({"name": "device_id", "value": "24700f9f1986800ab4fcc880530dd0ed"})
    #     self.driver.add_cookie({"name": "bid", "value": "60e0da22363d4df9e698f66ccd4326db_ko3xmp4o"})
    #     self.driver.add_cookie({"name": "s", "value": "ce1626v24t"})
    #     self.driver.add_cookie({"name": "acw_tc", "value": "2760820016197638815485042eee4bec957b146a75dcd6c626d04ffb7384fa"})
    #     self.driver.add_cookie({"name": "Hm_lvt_1db88642e346389874251b5a1eded6e3", "value": "1619687788"})
    #     self.driver.add_cookie({"name": "u", "value": "8361085792"})
    #     self.driver.add_cookie({"name": "xqat", "value": "590435a0841a58c25c4fd6714d01667db2f0299d"})
    #     print(self.driver.get_cookies())
    #     self.driver.refresh()
    #     self.driver.get("https://xueqiu.com/setting/user")

    def teardown_method(self):
        self.driver


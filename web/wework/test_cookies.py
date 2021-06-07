import shelve
import time

from selenium import webdriver
class TestCookies(object):
    @classmethod
    def setup_class(cls):
        cls.driver=webdriver.Chrome()



    # def setup_method(self):
    #     chrome_option = webdriver.ChromeOptions()
    #     chrome_option.debugger_address='127.0.0.1:9999'
    #     self.driver = webdriver.Chrome(options=chrome_option)



    def test_selenium(self):
        # Cookies = [
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
        #      'value': '1688851069808035'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
        #      'value': 'VYsqPL2WUrb6vPb7S3cxKnxzVDkVq0puLB4wJI-G4W1I4gu8qtZYY8UKI7tHRDu837Q-8cQzU6WXQ6ch-KZqjLtgoXuR9N5RULdU5JMNwAhxm0dPcubeRIXAA6MX5Ztnn1UbR--Qp8CzQ0ND4rjYxrM73AXRvJukz6zLX3dlHxP3ijr2yCFR-h__wliWKCAn0F0ZA14KXE-eIH4siqYtHjfpQIVLK1x6OucZghvurfPchV8PTXvWCxwBH4_Xfh24SkTpuWgAnt8ycNx5Z3cXLA'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
        #      'value': '1688851069808035'},
        #
        # #第一步  先打开浏览器获取cookies
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#profile")
        # Cookies=self.driver.get_cookies()
        # print("-------",Cookies)
        # time.sleep(3)

        #
        #
        #
        # #第二步  直接将cookie存进数据库
        # db=shelve.open("cookies")
        # db['cookie']=Cookies
        # db.close()

        #从数据库获取cookie
        db = shelve.open("cookies")
        cookies = db['cookie']



        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#profile")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#profile")
        time.sleep(3)
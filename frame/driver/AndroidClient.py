from appium import webdriver
import time
from appium.webdriver.webdriver import WebDriver

from frame.po import load


class AndroidClient(object):
    driver=WebDriver
    @classmethod
    def install_app(cls):
        caps = {}
        # caps["platformName"] = "Android"
        # caps["platformVersion"] = "6.0.1"
        # caps["deviceName"] = "127.0.0.1:6555"
        # # caps["noReset"] = True
        # caps["unicodeKeyboard"] = True
        # caps["appPackage"] = "com.xueqiu.android"
        # caps["appActivity"] = "com.xueqiu.android.common.splash.SplashActivity"
        # caps["autoGrantPermissions"] = True
        # caps["automationName"] = "uiautomator2"
        caps=load.load_caps()
        # cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver = webdriver.Remote(caps['url'], caps)
        cls.driver.implicitly_wait(10)
        return cls.driver


    @classmethod
    def start_app(cls):
        caps = {}
        # caps = load.load_caps('AndroidClient.yaml','start_app')
        caps["platformName"] = "Android"
        caps["platformVersion"] = "6.0.1"
        caps["deviceName"] = "127.0.0.1:6555"
        caps["noReset"] = True
        caps["unicodeKeyboard"] = True
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = "com.xueqiu.android.common.splash.SplashActivity"
        caps["autoGrantPermissions"] = True
        caps["automationName"] = "uiautomator2"
        caps["unicodeKeyboard"]=True    #支持中文输入
        caps["resetKeyboard"]=True

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        return cls.driver
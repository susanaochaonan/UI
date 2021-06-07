import time

import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from frame.driver.AndroidClient import AndroidClient


#实现将driver传递给page类、元素查找封装、加载数据配置
from app.android.ut.Log import Logger

# logger=Logger().getlog()
from frame.util.exception_handle import excption_handle


class BasePage(object):
    black_list = [("xpath", "//*[@resource-id='com.xueqiu.android:id/iv_close']"),("xpath","//*[@resource-id='com.xueqiu.android:id/image_cancel']")]
    #根据条件，确定具体使用androiddriver?iosdriver?
    @classmethod
    def __init__(self):
        self.driver:WebDriver=self.get_driver()
        #init方法里不能return

    #获取client
    @classmethod
    def get_client(cls):
        return AndroidClient
    #获取driver
    @classmethod
    def get_driver(cls):
        cls.driver=AndroidClient.driver
        return cls.driver



    @excption_handle
    def find(self,by,locator:WebElement=None):
        if locator is not None:
            element=self.driver.find_element(by,value=locator)
            return element
        else:
            element = self.driver.find_elements(*by)
            return element

    def findByText(self,text) -> WebElement:
        return self.find((By.XPATH,"//*[@text='%s']" %text))

    def LoadSteps(self, filename,casename, **kwargs):
        file = open('../data/' + filename, 'r', encoding='utf-8')
        file = yaml.load(file)
        steps = file[casename]
        realvalue=''
        for step in steps:
            by = step['by']
            pattern = step['pattern']
            action = str(step['action']).lower()
            if action.__contains__("send") :
                key = step['keys']
                text = str(key)
                for k, v in kwargs.items():
                    text = text.replace("$%s" % k, v)
                # print('find elememt',by,'+',patern,'+',action,'+',text)
                time.sleep(2)
                element: WebElement = self.find(by, pattern)
                time.sleep(3)
                element.send_keys(text)
            elif action=="click":
                element: WebElement=self.find(by,pattern)
                self.driver.implicitly_wait(5)
                element.click()
            elif action=="assert":
                realvalue = self.find(by,pattern).text

                print("-----realvalue:",realvalue)
                # assert_element=element
        return realvalue


    def load_caps(self,filename, method):
        caps: dict
        file = open('../data/' + filename, 'r', encoding='utf-8')
        AndroidClient = yaml.load(file)['AndroidClient']
        caps_start: dict = AndroidClient['start_app']
        caps_install: dict = AndroidClient['install_app']
        if method == 'start_app':
            # for k,v in caps.items():
            caps = caps_start
        else:
            caps = caps_install
        return caps
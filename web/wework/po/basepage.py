import yaml
from appium.webdriver.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

black_element=[('by','locator')]
class BasePage(object):
    def __init__(self,driver=None):
        if driver==None:
            options=webdriver.ChromeOptions()
            options=options.debugger_address('127.0.0.1:9999')
            self.driver=webdriver.Chrome(options=options)
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
        else:
            self.driver:WebDriver=driver

    def find(self,by,locator=None):
        try:
            if locator==None:
                ele:WebElement=self.driver.find_element(*by)
                return ele
            else:
                ele:WebElement=self.driver.find_element(by,locator)
                return ele
        except Exception as ex:
            for element in black_element:
                e:WebElement=self.driver.find_element(*element)
                if len(e) > 0:
                    e.click()
            print(ex)
        pass

    def load_step(self,file,method):
        f=open('../data/'+file+'.yaml','rb',encoding='utf-8')
        data=yaml.safe_load(f)
        steps=data[method]
        assert_elements=[]
        for step in steps:
            if step['action']=='click':
                el:WebElement=self.driver.find_element(step['by'],step['pattern'])
                el.click()
            elif 'send' in step['action']:
                el:WebElement=self.driver.find_element(step('by'),step['pattern'])
                el.send_keys(step['keys'])
            elif step['action']=='assert':
                el:WebElement=self.driver.find_element(step('by'),step['pattern'])
                assert_elements.append(el)
        return assert_elements


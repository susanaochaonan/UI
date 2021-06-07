from selenium.webdriver.common.by import By

from app.android.driver.AndroidClient import AndroidClient
from frame.po.BasePage import BasePage
from frame.po.HangqingPage import HagqingPage
from frame.po.LoginPage import LoginPage
from frame.po.SearchPage import SearchPage


class HomePage(BasePage):

    def to_hangqing(self):
        # hangqing_E=(By.XPATH, "//*[@text='行情']")
        # text_E="行情"
        # self.findByText(text_E).click()
        self.LoadSteps('HomePage.yaml','to_hangqing')
        return HagqingPage()
    def to_search(self):
        self.LoadSteps('HomePage.yaml','to_hangqing')
        return SearchPage()

    def to_login(self):
        self.LoadSteps('HomePage.yaml', 'to_login')
        return LoginPage()
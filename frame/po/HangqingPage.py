import time

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# from app.android.driver.AndroidClient import AndroidClient
from frame.po.BasePage import BasePage


class HagqingPage(BasePage):
    def add_stock(self,name):
        # search_E=(By.ID, "com.xueqiu.android:id/action_search")
        # self.find(search_E).click()
        #
        # close_E=(MobileBy.ID, "com.xueqiu.android:id/action_close")
        # WebDriverWait(self.driver, 10).until(
        #     ec.presence_of_element_located(close_E))
        #
        # input_text_E=(By.ID, "com.xueqiu.android:id/search_input_text")
        # self.find(input_text_E).send_keys("PDD")
        # time.sleep(2)
        #
        # stock_name_E=(By.XPATH, "//*[@text='PDD']")
        # text_stockname_E="PDD"
        # self.findByText(text_stockname_E).click()

        self.LoadSteps('HangqingPage.yaml',StockName=name)
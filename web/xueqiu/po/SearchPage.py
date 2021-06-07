from web.xueqiu.po.BasePage import BasePage
import time

class SearchPage(BasePage):
    def add_stock(self,stock_name):
        self.driver.find_element_by_xpath('//*[contains(text(),"%s")]/../../../..//a[@class="follow__control followed"]' % stock_name).click()
        time.sleep(2)

        return self

    def login_wimdow_close(self):
        self.driver.find_element_by_css_selector('.modal__login .close .iconfont').click()
        time.sleep(2)
        return self


    # def login_window_log
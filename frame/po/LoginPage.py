from frame.po.BasePage import BasePage
from frame.po.HangqingPage import HagqingPage
from frame.po.SearchPage import SearchPage

class LoginPage(BasePage):
    def to_close(self):
        self.LoadSteps("Login.yaml","to_close")
        return LoginPage()

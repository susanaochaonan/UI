from app.android.driver.AndroidClient import AndroidClient
from frame.po.BasePage import BasePage
from frame.po.HomePage import HomePage


class App(BasePage):
    @classmethod
    def tohome(cls):
        # 初始化，独立首页
        cls.get_client().start_app()
        return HomePage()
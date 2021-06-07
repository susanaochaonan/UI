from time import sleep
import pytest
from frame.po.App import App
class TestLoginPage(object):
    @classmethod
    def setup_class(cls):
        # cls.searchpage=App.tohome().to_search()
        cls.HomePage=App.tohome()




    # @pytest.mark.parametrize("name,excepted", [("拼多多", "已添加"), ("阿里巴巴", "已添加")])
    def test_handle_pop(self,name,excepted):
        self.driver=self.HomePage.to_login()
        self.driver=self.HomePage.to_hangqing()





    # def teardown_method(self):
    #     self.driver.quit()

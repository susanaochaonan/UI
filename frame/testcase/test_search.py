import pytest
from app.android.ut.common import *

from frame.po.App import App
class TestSearchPage(object):
    @classmethod
    def setup_class(cls):
        cls.searchpage=App.tohome().to_search()


    # @pytest.mark.parametrize("name,excepted",[("PDD","PDD"),("alibaba","BABA")])
    # def test_search(self,name,excepted):
    #     realvalue=''
    #     self.driver=self.searchpage.stock_search(name)
    #     realvalue=self.searchpage.get_stock_name()
    #     assert realvalue in excepted
    #     self.searchpage.stock_back()

    @pytest.mark.parametrize("name,excepted", [("拼多多", "已添加"), ("阿里巴巴", "已添加")])
    def test_add_stock(self,name,excepted):
        button_text=''
        self.driver=self.searchpage.stock_search(name)
        self.driver=self.searchpage.add_stock()
        button_text=self.searchpage.get_add_button_status()
        assert button_text == excepted
        self.searchpage.cancel_stock()#取消自选



    # def teardown_method(self):
    #     self.searchpage.stock_back()

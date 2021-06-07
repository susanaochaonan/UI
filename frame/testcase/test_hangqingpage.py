
import pytest

from app.android.po.App import App
# from app.android.po.HomePage import HomePage


class TestHangqingpage(object):
    @classmethod
    def setup_class(cls):
        cls.homepage=App.tohome()

    @pytest.mark.parametrize("name",["PDD","alibaba"])
    def test_add_stock(self,name):
        self.driver=self.homepage.to_hangqing().add_stock(name)




    # def teardown_method(self):


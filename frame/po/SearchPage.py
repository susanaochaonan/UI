from frame.po.BasePage import BasePage
class SearchPage(BasePage):
    def stock_search(self,name):
        self.LoadSteps('SearchPage.yaml','stock_search',StockName=name)

    def get_stock_name(self):
        text=self.LoadSteps('SearchPage.yaml','get_stock_name')
        return text


    def stock_back(self):
        self.LoadSteps('SearchPage.yaml','search_back')

    def add_stock(self):
        self.LoadSteps('SearchPage.yaml','addcancel_stock')

    def cancel_stock(self):
        self.LoadSteps('SearchPage.yaml','cancel_stock')

    def get_add_button_status(self):
        text=self.LoadSteps('SearchPage.yaml','get_add_status')
        return text

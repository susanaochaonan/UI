from web.wework.po.basepage import BasePage
from web.wework.po.contact_page import ContactPage


class IndexPage(BasePage):
    def to_contact(self):
        self.load_step('index_page','to_contact')
        return ContactPage(self.driver)

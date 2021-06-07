from web.wework.po.basepage import BasePage


class ContactPage(BasePage):
    def add_member(self):
        #input
        self.load_step('contact_page','add_member')
        return True

    def member_search(self):
        #tosend key
        return True
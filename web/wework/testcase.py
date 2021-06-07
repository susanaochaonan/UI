import shelve
from time import sleep
import allure

from selenium import webdriver

@allure.feature("上传文件")
class TestCase(object):
    # @allure.story("初始化浏览器")
    @classmethod
    def setup_class(cls):
        cls.driver=webdriver.Chrome()
        # with allure.step("打开浏览器")
        #     print("xxx")

    # def setup_method(self):
    #     chrome_option = webdriver.ChromeOptions()
    #     chrome_option.debugger_address='127.0.0.1:9999'
    #     self.driver = webdriver.Chrome(options=chrome_option)

    @allure.story("文件")
    def test_file(self):
        # # 从数据库获取cookie
        # db = shelve.open("cookies")
        # cookies = db['cookie']
        # db.close()
        # for cookie in cookies:
        #     self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#manageTools")
        sleep(1)

        with allure.step("点击图片"):
            self.driver.find_element_by_css_selector('a[href="#material/text"]').click()
            sleep(1)
        with allure.step("点击素材入口"):
            self.driver.find_element_by_css_selector('a[href="#material/image"]').click()
            sleep(1)
        # upload_e=self.driver.find_element_by_css_selector('.js_upload_file_selector')
        # # self.driver.find_element_by_css_selector('.js_upload_file_selector').click()
        # self.driver.execute_script('arguments[0].click()',upload_e)
        # sleep(3)
        # self.driver.find_element_by_css_selector('#js_upload_input').send_keys("E:/script/UI/file/1.jpg")
        # sleep(3)
        # self.driver.find_element_by_css_selector('.js_next').click()
        # sleep(3)

        elements=self.driver.find_elements_by_css_selector('.js_pic_preview_item')
        assert len(elements)==4










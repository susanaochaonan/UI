import yaml

from app.android.po import BasePage
import sys

from app.android.po import load
from app.android.ut.Log import Logger
from app.android.ut.Log import *

logger=Logger().getlog()
class TestDemo(object):
    def setup_method(self):
        pass
    def test_load(self):
        file = open('../data/pop.yaml', "r", encoding='utf-8')
        text = yaml.load(file)
        print(text)
    # def test_load(self):
    #     load.LoadSteps('HomePage.yaml')
        # caps = {}
        # caps=load.load_caps('AndroidClient.yaml','start_app')
        # print(caps)
        # print(caps['url'])
        # action='sendkys'
        # if action.__contains__("send"):
        #     print(True)


    # def test_log(self):
    #     logger.warn('oooo')

    # def test_decorator(self):
    #     add(1,1)
    def teardown_method(self):
        pass

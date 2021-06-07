import os
import sys

import json

import yaml


def get_filename():
    # filepath=os.path.split(os.path.realpath(__file__))[0]
    # dirname=os.path.dirname(__file__)
    realpath=os.path.realpath(__file__)
    file_name=os.path.split(realpath)[1]
    return file_name

def LoadSteps(filename, **kwargs):
    file = open('../data/' + filename, 'r', encoding='utf-8')
    print(file)
    file = yaml.load(file,Loader=yaml.FullLoader)
    print("------",file)
    pagename=str(filename).split('.')[0]
    print('pagename:',pagename)
    steps = file[pagename]
    for step in steps:
        by = step['by']
        print('bybyyyyyyy:',by)
        pattern = step['pattern']
        action = str(step['action']).lower()
        if action.__contains__("send") :
            key = step['keys']
            text = str(key)
            for k, v in kwargs.items():
                text = text.replace("$%s" % k, v)
            # print('find elememt',by,'+',pattern,'+',action,'+',text)
            print(by, pattern)
            print(text)
        else:
            print(by,pattern)










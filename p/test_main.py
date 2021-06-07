import importlib
import pytest
# from p.hello import Hello

def test_tmp():
    c=importlib.import_module("p.hello")
    h=getattr(c, 'Hello')()
    f=getattr(h, 'add')()
    print('----------',f)
    print(eval("1+1"))



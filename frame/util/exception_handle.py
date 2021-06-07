import allure


def excption_handle(func):
    def wrapper(*args,**kwargs):
        from frame.po.BasePage import BasePage
        instance:BasePage =args[0]
        try:
            result=func(*args,**kwargs)
            return result
        except Exception as e:
            instance.driver.save_screenshot("tmp.png")
            with open("tmp.png","rb") as f:
                content=f.read()
            allure.attach(content,attachment_type=allure.attachment_type.PNG)
            for b in instance.black_list:
                ele=instance.driver.find_elements(*b)
                if len(ele) > 0:
                    ele[0].click()
                return wrapper(*args,**kwargs)
            print("元素未找到 %s"%args)
            raise e
    return wrapper
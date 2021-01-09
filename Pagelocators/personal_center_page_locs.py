'''
Description: 前程贷用户页面元素定位
Version: 2.0
Autor: byh
Date: 2020-11-22 10:23:46
LastEditors: byh
LastEditTime: 2020-11-22 22:21:03
'''
from selenium.webdriver.common.by import By


class PersonalcenterLocators():
    '''个人中心页面的元素定位'''
    # 用户的可用余额
    use_amount_ele = (By.XPATH,'//li[@class="color_sub"]')
    
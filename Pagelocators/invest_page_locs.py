'''
Description: 前程贷投资页面元素定位
Version: 2.0
Autor: byh
Date: 2020-11-22 11:05:02
LastEditors: byh
LastEditTime: 2020-11-28 17:27:11
'''
from selenium.webdriver.common.by import By

class InvestLocators():
    '''投资页面的元素定位'''
    # 输入投资金额的【输入框】
    Input_box_ele = (By.XPATH,'//div[@class="clearfix left"]//input')
    # 【投标】按钮元素
    tender_button_ele=(By.XPATH,"//button[text()='投标']")
    # 【查看并激活】按钮
    view_and_activate_ele = (By.XPATH,'//div[@class="layui-layer-content"]//button[contains(text(),"查看")]')
    # 用户的可用金额元素
    user_amount_ele = (By.XPATH,'//div[@class="clearfix left"]//input')
    # 标的可投资金额
    subject_amount_ele = (By.XPATH,'//span[@class="mo_span4"]')
    # 【蜂群/社区】按钮
    bee_button = (By.XPATH,'//a[text()="蜂群/公社"]')
    # 首页按钮
    home_button = (By.XPATH,'//div[@class="header "]//a[text()="投标"]')



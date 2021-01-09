'''
Description: 前程贷主页元素定位
Version: 2.0
Autor: byh
Date: 2020-11-19 20:57:30
LastEditors: byh
LastEditTime: 2020-11-28 15:25:39
'''
from selenium.webdriver.common.by import By


class HomeLocators():
    '''主页元素定位'''
    # 获取退出按钮
    exit_ele=(By.XPATH,'//a[text()="退出"]')
    # 获取【个人中心】按钮
    personal_center_ele=(By.XPATH,'//img[@class="mr-5"]')
    # 获取首页的第一个标的【抢投标】按钮
    first_subject_ele = (By.XPATH,'//div[@class="b-unit-list clearfix"]//div[@class="b-unit"][1]//a[text()="抢投标"]')
    # 首页蜂群/公社 元素定位
    bee_button_ele = (By.XPATH,'//a[text()="蜂群/公社"]')

    

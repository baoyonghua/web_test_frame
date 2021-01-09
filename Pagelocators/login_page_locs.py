'''
Description: 前程贷登陆页面元素定位
Version: 2.0
Autor: byh
Date: 2020-11-19 20:57:44
LastEditors: byh
LastEditTime: 2020-11-22 22:20:48
'''
from selenium.webdriver.common.by import By


class LoginLocators():
    '''登录页面元素定位'''
    # 账号框
    user_input = (By.XPATH,'//input[@name="phone"]')
    # 密码框
    pwd_input = (By.XPATH,'//input[@name="password"]')
    # 登录按钮
    login_button = (By.TAG_NAME,"button")
    # 登录报错时的元素（错误的账号，空的账号/密码）
    msg_form = (By.XPATH,'//div[@class="form-error-info"]')
    # 登录报错时的元素（错误的密码，账号没有注册）
    msg_layui = (By.XPATH,'//div[@class="layui-layer-content"]')

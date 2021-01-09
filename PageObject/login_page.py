'''
Description: 登陆页面操作
Version: 2.0
Autor: byh
Date: 2020-11-18 19:16:52
LastEditors: byh
LastEditTime: 2020-11-24 16:14:13
'''
import os,sys
base_path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)



from selenium import webdriver
from Pagelocators.login_page_locs import LoginLocators as locs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from common.basepage import BasePage

class LoginPage(BasePage):
    '''登录页面操作'''
    # 登录
    def login(self,username,pwd):
        self.input_keys(locs.user_input,username,"登陆页面_账号框")
        self.input_keys(locs.pwd_input,pwd,"登陆页面_密码框")
        self.click_ele(locs.login_button,"登陆页面_登录按钮")


    def get_msg_from_login_form(self):
        '''捕获登录失败时的错误信息的元素文本'''     
        # 获取单个元素
        ele_text = self.get_ele_text(locs.msg_form,"登陆页面_失败文本1")
        # 返回元素的文本
        return ele_text


    def get_msg_from_login_layui(self):
        '''获取登录失败时的元素的文本'''
        ele_text = self.get_ele_text(locs.msg_layui,"登陆页面_失败文本2")
        return ele_text





    



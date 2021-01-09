'''
Description: 投资测试用例
Version: 2.0
Autor: byh
Date: 2020-11-22 12:25:47
LastEditors: byh
LastEditTime: 2020-11-25 14:57:24
'''

import os,sys
base_path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)


import unittest
from decimal import Decimal
from selenium import webdriver
from TestData.Common_Data import CommonData
from TestData.invest_data import account_num
from TestData.invest_data import amount
from PageObject.login_page import LoginPage
from PageObject.home_page import HomePage
from PageObject.invest_page import InvestPage
from PageObject.personal_center_page import PersonalcenterPage
from middleware.logger_handler import logger


class TestInvert(unittest.TestCase):
    '''投资测试用例'''
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(CommonData.login_url)
        self.driver.maximize_window()
        # 1.用户登录
        LoginPage(self.driver).login(*account_num)
        # 2.有可投资的标的
        # 3.用户可用金额足够
        # 4.可投资标的金额大于2000

    def tearDown(self):
        # 退出浏览器
        self.driver.close()

    def test_invest_success(self):
        # 1.前程贷首页 -- 
        home = HomePage(self.driver)
        # 投资前，在个人页面/投资页面，获取用户投资前的金额       
        # 进入个人页面
        home.click_personal_center()
        # 获取投资前的用户金额
        Pc = PersonalcenterPage(self.driver)
        before_user_amount=Pc.get_user_amount_from_PersonalCenter()
        # 回到上一次浏览的页面
        Pc.back_to_previous_page()        
        # 点击首页的第一个标的，进入投资页面
        home.click_first_mark_ele()
         # 初始化投资页面操作
        investpage = InvestPage(self.driver)
        # 在投资页面获取用户余额
        # before_user_amount = investpage.get_user_amount_from_InvestPage()
        # 投资前，在投资页面获取标的投资前的剩余投资金额
        before_subject_amount = investpage.get_subject_amount_from_InvestPage()
        # 2.投资界面 --- 输入2000元金额，进行投标处理
        investpage.Input_amount(amount)
        # 点击投资按钮
        investpage.click_tender_button()
         # 3.投资页面 -- 点击弹框中的“查看并激活按钮”进入个人中心页面
        investpage.click_view_and_activate()
        # 投资完成后，在个人页面获取用户投资后的金额
        after_user_amount = Pc.get_user_amount_from_PersonalCenter()
        # 用户投资后，从个人中心返回到投资页面，刷新，
        Pc.back_to_previous_page()
        # 获取标的投资后剩余投资金额
        after_subject_amount=investpage.get_subject_amount_from_InvestPage()
        
        # 断言
        try:
            # 1.用户投资前的金额 - 投资后的金额=2000
            user_expect = Decimal(before_user_amount) - Decimal(after_user_amount)
            self.assertEqual(int(user_expect),2000)
            # 2.（标的投资前的金额 - 投资后的金额）*10000 = 2000
            subject_expect = (Decimal(before_subject_amount) - Decimal(after_subject_amount))*10000
            self.assertEqual(int(subject_expect),2000)
            logger.info("pass")
        except AssertionError as e:
            logger.exception("断言失败")
            raise e


if __name__ == "__main__":    
    unittest.main()
'''
Description: 登录测试用例
Version: 2.0
Autor: byh
Date: 2020-11-18 19:14:39
LastEditors: byh
LastEditTime: 2020-12-29 15:14:40
'''

import os,sys
base_path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)

    

import unittest
from PageObject.login_page import LoginPage
from PageObject.home_page import HomePage
from selenium import webdriver
import ddt
from TestData.Common_Data import CommonData
from TestData.login_data import LoginData
from middleware.logger_handler import logger


@ddt.ddt
class TestLogin(unittest.TestCase):
    '''登录测试用例'''
    # 测试数据
    data_form = LoginData.fail_form_data
    data_layui = LoginData.fail_layui_data

    def setUp(self):
        logger.info("********登录测试用例前置条件***************")
        # 初始化操作，保证每次测试都是相互独立的！
        self.driver = webdriver.Chrome()
        self.driver.get(CommonData.login_url)
        self.driver.maximize_window()


    def tearDown(self):
        # 关闭浏览器
        self.driver.close()

    def test_login_success(self):
        logger.info("************登录成功用例****************")
        lp = LoginPage(self.driver)
        lp.login(*LoginData.success_data)
        # 进行断言
        try:
            self.assertTrue(HomePage(self.driver).get_quit_ele_exists())
            logger.info("断言成功")
        except AssertionError as e:
            logger.exception("断言失败")
            raise e
    

    @ddt.data(*data_form)
    def test_login_failed_form(self,data_info):
        logger.info("*************登录失败场景1用例*************")
        # 进行登录操作
        lp = LoginPage(self.driver)
        # 输入空的账号/密码/错误的手机号
        lp.login(data_info["phone"],data_info["pwd"])
        # 进行断言
        try:
            self.assertEqual(lp.get_msg_from_login_form(),data_info["check"])
            logger.info("断言成功")
        except AssertionError as e:
            logger.exception("断言失败")
            raise e
    

    @ddt.data(*data_layui)
    def test_login_failed_layui(self,data_info):
        logger.info("*************登录失败场景2用例***************")
        lp=LoginPage(self.driver)
        lp.login(data_info["phone"],data_info["pwd"])
        msg_text=lp.get_msg_from_login_layui()
        # 进行断言
        try:
            self.assertEquals(msg_text,data_info["check"])
            logger.info("断言成功")
        except AssertionError as e:
            logger.exception("断言失败")
            raise e



    

if __name__ == "__main__":
    unittest.main()

# testloader = unittest.TestLoader()
# testloader.loadTestsFromModule()
# testloader.loadTestsFromTestCase()


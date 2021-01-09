"""
Description: 加入蜂群/公社的测试用例
Version: 2.0
Autor: byh
Date: 2020-11-28 16:03:15
LastEditors: byh
LastEditTime: 2020-12-11 17:14:00
"""

# import os,sys
# base_path=os.path.dirname(os.path.dirname(__file__))
# sys.path.append(base_path)

import time
# import unittest
import pytest
from selenium import webdriver
from PageObject.bee.bee_page import BeePage
from PageObject.bee.beehome_page import BeehomePage
from PageObject.home_page import HomePage
from PageObject.login_page import LoginPage
from PageObject.invest_page import InvestPage
from TestData.login_data import LoginData
from common.basepage import BasePage
from TestData import bee_data
from decimal import Decimal
from middleware.logger_handler import logger


@pytest.mark.bee
class TestBee:
    """
    description : 加入【蜂群/公社】测试类
    """

    # 用户登录信息
    # user_info = LoginData.success_data

    # def setUp(self):
    #     logger.info("**********测试用例开始执行***********")
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('http://120.78.128.25:8765/Index/login.html')
    #     self.driver.maximize_window()
    #     # 1.用户已登录
    #     lp = LoginPage(self.driver) 
    #     lp.login(*self.user_info)
    #     # 2.有可加入的蜂群
    #     # 3.用户的金额大于5

    # def tearDown(self):
    #     logger.info("**********测试用例结束***********")
    #     self.driver.close()

    @pytest.mark.usefixtures("init_login")
    def test_join_bee(self, init_login):
        # 1.前程贷首页——点击 第一个标的，进入项目详情页面(投资页面)
        HomePage(init_login).click_first_mark_ele()
        # 发红包前在投资页面获取用户可用余额
        investpage = InvestPage(init_login)
        before_user_amount = investpage.get_user_amount_from_InvestPage()
        # 2.投标页面——点击 蜂群/公社，进入蜂群页面
        investpage.click_bee()
        # 3.蜂群页面——鼠标移动到第一个蜂群点击【查看蜂群】
        bp = BeePage(init_login)
        bp.move_to_first_bee()
        bp.view_bee()
        # 4.蜂群详情页（为新窗口）
        bp.switch_new_win()
        bh = BeehomePage(init_login)
        # 发红包后在投资页面获取蜂群的公产规模
        before_pub_amount = bh.get_public_money()
        # 点击敲门红包，并选中“5元”，进行点击
        bh.click_red_envelope()
        bh.click_five_dollor()
        bh.click_determine()
        time.sleep(0.5)
        # 获取发送红包后的提示
        reward_success_msg = bh.get_reward_success_msg()
        # 5.蜂群详情页——进行刷新
        bh.refresh_page()
        # 发红包后在投资页面获取蜂群的公产规模
        after_pub_amount = bh.get_public_money()
        # 6.蜂群详情页——点击【申请加入】按钮
        bh.click_join_button()
        # 点击确定按钮
        bh.click_join_determine()
        time.sleep(0.5)
        # 获取加入蜂群的提示'
        join_msg = bh.get_join_msg()
        # 7.蜂群详情页——点击首页中的第一个标的，进入投资页面
        bh.click_home()
        HomePage(init_login).click_first_mark_ele()
        # 发红包后在投资页面获取用户可用余额
        after_user_amount = investpage.get_user_amount_from_InvestPage()

        # 断言
        try:
            # 1.申请的蜂群提示
            assert join_msg == bee_data.expected_join_msg
            # 2.发红包后提示
            assert reward_success_msg == bee_data.expected_reward_success_msg
            # 3.蜂群的公产规模+5
            expected_pub_amount = Decimal(after_pub_amount) - Decimal(before_pub_amount)
            assert int(expected_pub_amount) == bee_data.amount
            # 用户可用金额减少5元
            expected_user_amount = Decimal(before_user_amount) - Decimal(after_user_amount)
            assert int(expected_user_amount) == bee_data.amount
        except Exception as e:
            logger.exception("执行测试用例失败，msg:{}".format(e))
            raise e
        else:
            logger.info("执行测试用例成功")


if __name__ == "__main__":
    pytest.main(['-s', '-v', '-m', "bee"])

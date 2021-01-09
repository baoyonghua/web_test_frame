'''
Description: 前程贷pytest的前置后置模块
Version: 2.0
Autor: byh
Date: 2020-12-11 16:42:07
LastEditors: byh
LastEditTime: 2020-12-30 13:41:06
'''
import pytest

from selenium import webdriver
from middleware.logger_handler import logger
from PageObject.login_page import LoginPage
from TestData.login_data import LoginData


@pytest.fixture()
def init_driver():
    logger.info("*********测试用例开始执行***********")
    driver=webdriver.Chrome()
    driver.get('http://120.78.128.25:8765/Index/login.html')
    driver.maximize_window()
    yield driver
    driver.close()
    logger.info("*********测试用例执行结束***********")


@pytest.fixture()
def init_login(init_driver):
    try:
        LoginPage(init_driver).login(*LoginData.success_data)
    except Exception as e:
        logger.info("登录前程贷失败")
        raise e
    yield init_driver
    
    

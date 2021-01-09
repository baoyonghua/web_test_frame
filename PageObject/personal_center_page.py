'''
Description: 
Version: 2.0
Autor: byh
Date: 2020-11-22 10:19:51
LastEditors: byh
LastEditTime: 2020-11-24 17:19:12
'''
import os,sys
base_path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)

from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pagelocators.personal_center_page_locs import PersonalcenterLocators as locs
from common.basepage import BasePage



class PersonalcenterPage(BasePage):
    '''个人中心页面'''

    def get_user_amount_from_PersonalCenter(self):
        '''获取个人中心的用户剩余金额'''
        # WebDriverWait(self.driver,60).until(EC.visibility_of_element_located(locs.use_amount_ele))
        # 获得元素的文本值
        user_amount = self.get_ele_text(locs.use_amount_ele,"个人中心_获取用户余额",timeout=60)
        user_amount=float(user_amount.split("元")[0])
        return user_amount
        

    def back_to_previous_page(self):
        '''从个人中心页面返回到上一次的页面，并进行刷新'''
        self.driver.back()
        self.driver.refresh()


    
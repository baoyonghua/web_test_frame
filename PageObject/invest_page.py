'''
Description: 
Version: 2.0
Autor: byh
Date: 2020-11-22 10:30:18
LastEditors: byh
LastEditTime: 2020-11-28 17:29:18
'''
import os,sys
base_path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pagelocators.invest_page_locs import InvestLocators as locs
from common.basepage import BasePage



class InvestPage(BasePage):
    '''投资页面'''
    
    def get_user_amount_from_InvestPage(self):
        '''获取投资页面的用户金额'''
        user_amount=self.get_ele_attr(locs.user_amount_ele,'data-amount',"投资页面_获取用户余额")
        return user_amount

    def get_subject_amount_from_InvestPage(self):
        '''获取投资页面的标的剩余投资金额'''
        subject_amount=self.get_ele_text(locs.subject_amount_ele,"投资页面_获取标的剩余投资金额")
        return subject_amount
   
    def Input_amount(self,amount):
        '''输入投资金额'''
        self.input_keys(locs.Input_box_ele,amount,"投资页面_输入投资金额")

    def click_tender_button(self):
        '''点击投标按钮'''
        self.click_ele(locs.tender_button_ele,"投资页面_点击投标按钮")
        
    def click_view_and_activate(self):
        '''点击【查看并激活】按钮'''
        self.click_ele(locs.view_and_activate_ele,"投资页面_点击【查看并激活】按钮")
    def click_bee(self):
        '''点击蜂群按钮'''
        self.click_ele(locs.bee_button,"投资页面_点击【蜂群/公社】")
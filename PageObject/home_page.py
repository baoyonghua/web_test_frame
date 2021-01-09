'''
Description: 
Version: 2.0
Autor: byh
Date: 2020-11-18 19:17:01
LastEditors: byh
LastEditTime: 2020-12-30 13:40:31
'''
import os,sys
base_path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)


from selenium import webdriver
from Pagelocators.home_page_locs import HomeLocators as locs
from common.basepage import BasePage


class HomePage(BasePage):
    '''项目主页操作'''

    def get_quit_ele_exists(self):
        '''主页面是否存在【退出】按钮的元素'''
        try:
            self.wait_ele_visible(locs.exit_ele,"前程贷主页_是否存在退出按钮")
        except :
            return False
        else:
            return True

    def click_first_mark_ele(self):
        '''对首页的第一个标的进行点击'''
        self.click_ele(locs.first_subject_ele,"前程贷主页_对第一个标进行点击")
        
        
    def click_personal_center(self):
        '''点击【个人中心】按钮'''
        self.click_ele(locs.personal_center_ele,"前程贷主页_点击【个人中心】按钮")


    def click_bee(self):
        self.click_ele(locs.bee_button_ele,'前程贷首页_点击【蜂群/公社】')
    
    

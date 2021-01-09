'''
Description: 蜂群/公社 次页面的页面操作
Version: 2.0
Autor: byh
Date: 2020-11-28 15:34:41
LastEditors: byh
LastEditTime: 2020-11-28 17:35:09
'''
import os,sys
base_path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)

from Pagelocators.bee.bee_page_locs import BeeLocators as locs
from common.basepage import BasePage

class BeePage(BasePage):
    '''
    description : 蜂群/公社_页面操作
    '''
    
    def view_bee(self):
        '''点击【查看蜂群】按钮'''
        self.click_ele(locs.view_bee_button_eles,'蜂群次页面_点击【查看蜂群】按钮')
    
    def switch_new_win(self):
        '''切换到新的窗口'''
        self.switch_to_window(-1,'蜂群次页面_切换窗口')
    
    def move_to_first_bee(self):
        '''将鼠标移动到第一个蜂群上'''
        self.move_to_ele(locs.first_bee,'蜂群次页面_将鼠标移动到第一个蜂群上')
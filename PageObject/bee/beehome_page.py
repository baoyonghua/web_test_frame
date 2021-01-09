'''
Description: 蜂群/公社  主页面
Version: 2.0
Autor: byh
Date: 2020-11-28 15:41:34
LastEditors: byh
LastEditTime: 2020-11-28 17:56:26
'''

import os,sys
base_path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)


from Pagelocators.bee.beehome_page_locs import BeehomeLocators as locs
from common.basepage import BasePage


class BeehomePage(BasePage):
    '''
    description : 蜂群/公社 主页面  操作
    '''
    def get_public_money(self):
        '''获取公产规模'''
        pub_amount = self.get_ele_text(locs.public_money,'蜂群主页面_获取公产规模')
        pub_amount = pub_amount.split('元')[0]
        return pub_amount

    def click_join_button(self):
        '''点击【申请加入】'''
        self.click_ele(locs.join_button,'蜂群主页面_点击【申请加入】')
    
    def click_join_determine(self):
        '''点击【确定】申请加入蜂群'''
        self.click_ele(locs.join_determine_button,'蜂群主页面_点击【确定】申请加入蜂群')
    
    def get_join_msg(self):
        '''获取申请加入后的提示'''
        msg = self.get_ele_text(locs.join_bee_msg,'蜂群主页面_获取申请加入后的提示')
        return msg
    
    def click_red_envelope(self):
        '''点击【敲门红包】'''
        self.click_ele(locs.red_envelope_button,'蜂群主页面_点击【敲门红包】')
        
    def click_five_dollor(self):
        '''选择五元红包'''
        self.click_ele(locs.five_dollor,'蜂群主页面_选择五元红包')
    
    def click_determine(self):
        '''点击【确定】按钮发送红包'''
        self.click_ele(locs.red_envelope_determine_button,'蜂群主页面_点击【确定】按钮发送红包')
    
    def get_reward_success_msg(self):
        '''获取发送红包后的提示'''
        msg = self.get_ele_text(locs.reward_success_msg,'蜂群主页面_获取发送红包后的提示')
        return msg

    def refresh_page(self):
        '''刷新页面'''
        self.driver.refresh()
    
    def click_home(self):
        '''点击首页'''
        self.click_ele(locs.home_button,'蜂群主页面_点击首页按钮')
    

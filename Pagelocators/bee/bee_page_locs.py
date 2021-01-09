'''
Description: 蜂群/公社，蜂群理财页面
Version: 2.0
Autor: byh
Date: 2020-11-27 17:32:41
LastEditors: byh
LastEditTime: 2020-11-28 17:34:19
'''
from selenium.webdriver.common.by import By
class BeeLocators():
    # 第一个蜂群
    first_bee = (By.XPATH,'//div[@class="cap_box"]//div[@class="top_single mg_left5"]')
    # 查看蜂群按钮
    view_bee_button_eles = (By.XPATH,'//div[@class="capital_tit"]/parent::*//div[@class="top_single mg_left5"]//a')
    
    
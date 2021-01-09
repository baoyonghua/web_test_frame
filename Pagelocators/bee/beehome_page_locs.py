'''
Description: 蜂群首页
Version: 2.0
Autor: byh
Date: 2020-11-27 17:42:39
LastEditors: byh
LastEditTime: 2020-11-28 17:54:35
'''
from selenium.webdriver.common.by import By
class BeehomeLocators():
    #获取公产规模的字段
    public_money = (By.XPATH,'//div[@class="examine_info_right examine_info_border width_div150"]//div')
    # 申请加入按钮
    join_button = (By.XPATH,'//button[@class="apply_join"]')
    # 申请加入__确定按钮
    join_determine_button = (By.XPATH,'//a[@class="layui-layer-btn0"]')
    # 加入蜂群后的提示
    join_bee_msg=(By.XPATH,'//div[@class="layui-layer-content"]')
    # 敲门红包按钮
    red_envelope_button = (By.XPATH,'//button[@class="red_packet"]')
    # 5元红包选项
    five_dollor = (By.XPATH,'//div[@id="layui-layer1"]//div[@data-value="5"]')
    # 发送红包确定按钮
    red_envelope_determine_button = (By.XPATH,'//div[@id="layui-layer1"]//button[@class="reward_ok btn btn-special"]')
    # 【打赏成功】提示
    reward_success_msg = (By.XPATH,'//div[@class="layui-layer-content"]')
    # 首页  按钮
    home_button = (By.XPATH,'//div[@class="navlist clearfix fs-18"]//a[text()="首页"]')

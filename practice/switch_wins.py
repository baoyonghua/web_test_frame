"""
Description: 百度切换窗口练习
Version: 2.0
Autor: byh
Date: 2020-11-25 21:24:44
LastEditors: byh
LastEditTime: 2020-11-26 17:44:23
"""

# import os,sys
# base_path=os.path.dirname(os.path.dirname(__file__))
# sys.path.append(base_path)
import time
from common.basepage import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class BdPage(BasePage):
    baidu_input = (By.ID, "kw")
    baidu_button = (By.ID, 'su')
    selenium_link = (By.XPATH, '//a[text()="官方"]/preceding-sibling::*')
    download_button = (By.XPATH, '//h3[text()="Selenium IDE"]/parent::*//a')

    def search_for_content(self, keys):
        self.input_keys(self.baidu_input, keys, "百度首页_输入内容")
        self.click_ele(self.baidu_button, "百度首页_点击搜索")

    def click_selenium(self):
        self.click_ele(self.selenium_link, "搜索页面_点击selenium")

    def click_download(self):
        self.switch_to_window(-1, "百度搜索页面")
        self.click_ele(self.download_button, "selenium_点击download按钮")


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    driver.maximize_window()
    bd = BdPage(driver)
    bd.search_for_content("selenium")
    bd.click_selenium()
    bd.click_download()
    time.sleep(5)
    driver.quit()

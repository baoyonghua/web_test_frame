'''
Description: 腾讯课堂登录操作
Version: 2.0
Autor: byh
Date: 2020-11-25 20:43:46
LastEditors: byh
LastEditTime: 2020-11-25 21:20:26
'''
import os,sys
base_path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)

from common.basepage import BasePage
from selenium.webdriver.common.by import By


login_button = (By.XPATH,'//a[@id="js_login"]')
qq_login = (By.XPATH,'//i[@class="icon-font i-qq"]')
# iframe_loc = (By.XPATH,'//iframe[@name="login_frame_qq"]')
iframe_loc = 'login_frame_qq'
pwd_login_loc = (By.XPATH,'//a[@id="switcher_plogin"]')
user_input = (By.ID,'u')
pwd_input = (By.ID,'p')
login_loc = (By.ID,"login_button")

class TxPage(BasePage):


    def click_login_button(self):
        self.click_ele(login_button,"腾讯课堂主页_点击登录按钮")
    
    def click_pwd_login(self):
        self.click_ele(qq_login,"腾讯课堂主页_点击qq登录按钮")
        self.switch_to_iframe(iframe_loc,"登陆页面_切换到iframe")
        self.click_ele(pwd_login_loc,"iframe框架_点击账号密码登录")
    def input_user_pwd(self,user,pwd):
        self.input_keys(user_input,user,"iframe框架_输入账号")
        self.input_keys(pwd_input,pwd,"iframe框架_输入密码")
        self.click_ele(login_loc,"iframe框架_点击登录按钮")



if __name__ == "__main__":
    import time
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("https://ke.qq.com/")
    driver.maximize_window()
    tx = TxPage(driver)
    tx.click_login_button()  
    tx.click_pwd_login()
    tx.input_user_pwd("1157449003","byhhy6873573") 
    time.sleep(20)
    driver.close()
    
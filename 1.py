"""
Description:
Version: 2.0
Autor: byh
Date: 2020-11-18 21:15:24
LastEditors: byh
LastEditTime: 2020-11-25 12:56:55
"""

#
# import os,sys
# base_path=os.path.dirname(os.path.dirname(__file__))
# sys.path.append(base_path)
# driver = webdriver.Chrome()
# driver.get(CommonData.login_url)
# driver.maximize_window()
# LoginPage(driver).login(*account_num)
# HomePage(driver).click_first_mark_ele()
# a= InvestPage(driver).get_subject_amount_from_InvestPage()
# b= a
# c=Decimal(b)+Decimal("0.01")
# print(c)
# print(type(c))

# driver.close()
import unittest
import time

s = '4926001336.65元'
s1 = s.split('元')
s2 = float(s1[0])
print(type(s2))


now1 = time.time()
time.sleep(1)
now2 = time.time()
t = now2 - now1

# print(str(t))
# TestLoader = unittest.TestLoader()
# TestLoader.discover()

# logger.exception("hello")

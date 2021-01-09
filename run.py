"""
Description: 运行测试用例模块
Version: 2.0
Autor: byh
Date: 2020-11-26 19:16:49
LastEditors: byh
LastEditTime: 2020-12-30 12:42:10
"""
# import os
# import sys
#
# base_path = os.path.dirname(os.path.dirname(__file__))
# sys.path.append(base_path)

import os
from middleware.logger_handler import logger
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from config.config_path import Configuration

testloader = unittest.TestLoader()
suite = testloader.discover(Configuration.testcase_path)

if not os.path.exists(Configuration.report_folder_path):
    os.mkdir(Configuration.report_folder_path)

now = time.strftime("%y-%m-%d %H_%M_%S")
report_name = r"\testreport {}.html".format(now)
report_path = Configuration.report_folder_path + report_name
print(report_path)

with open(report_path, "wb") as f:
    runner = HTMLTestRunner(stream=f, verbosity=2, title="自动化测试报告", description="前程贷项目", tester="byh")
    try:
        runner.run(suite)
    except Exception as e:

        logger.exception("生成测试报告失败:{}".format(e))
        raise e

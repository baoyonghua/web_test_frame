'''
Description: 项目的logger模块
Version: 2.0
Autor: byh
Date: 2020-11-20 15:41:55
LastEditors: byh
LastEditTime: 2020-11-28 18:16:24
'''
import os,sys
base_path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)

from common.py_log import PyLogger
from config.config_path import Configuration

class LoggerHandler(PyLogger):
    pass


logger = LoggerHandler(file_path=Configuration.logfile_path)

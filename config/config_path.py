'''
Description: 项目文件路径
Version: 2.0
Autor: byh
Date: 2020-11-19 22:20:53
LastEditors: byh
LastEditTime: 2020-11-26 19:28:39
'''
import os
import time
class Configuration():
    '''项目的文件路径'''
    # 项目路径
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 配置文件夹路径
    config_path = os.path.join(base_path,"config")
    # yaml文件路径
    yaml_path = os.path.join(config_path,"yaml_config.yaml")
    # excel文件路径

    # log日志文件夹的路径
    log_path = os.path.join(base_path,'recode\logs')
    # log文件路径
    log_name = time.strftime("%y-%m-%d %H_%M_%S")

    logfile_path = os.path.join(log_path,log_name+'.log') 
    # 截图文件夹保存路径
    screenshot = os.path.join(base_path,r"recode\screenshot")

    # 测试用例存放的文件夹
    testcase_path = os.path.join(base_path,"Testcase")
    # 测试报告存放文件夹
    report_folder_path = os.path.join(base_path,"report")



if __name__ == "__main__":
    a=Configuration.testcase_path
    print(a)
    # with open(logfile_path,"w+",encoding="utf8")as f:
    #     data = f.read()
    #     print(data)
    # pass

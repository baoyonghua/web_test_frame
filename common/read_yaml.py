'''
Description: 读取yaml文件
Version: 2.0
Autor: byh
Date: 2020-11-19 22:18:45
LastEditors: byh
LastEditTime: 2020-11-22 22:19:42
'''
import os,sys
base_path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)



import yaml
from config.py_config import Configuration

class ReadYaml():
    '''读取yaml文件的数据'''
    def __init__(self,yaml_path):
        self.yaml_path = yaml_path
    def read_yaml(self):
        with open(self.yaml_path,"r",encoding="utf8") as f:
            data = yaml.load(stream=f.read(),Loader=yaml.FullLoader)
        return data



if __name__ == "__main__":
    pass
    # a=ReadYaml(Configuration.yaml_path).read_yaml()
    # print(a)

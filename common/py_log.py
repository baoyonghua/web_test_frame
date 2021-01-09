'''
Description: 记录日志
Version: 2.0
Autor: byh
Date: 2020-11-20 15:11:39
LastEditors: byh
LastEditTime: 2020-11-23 17:23:27
'''
import logging



class PyLogger(logging.Logger):
    '''日志'''
    
    def __init__(self,file_path=None,name="lemon",level="DEBUG"):
        super().__init__(name)
        self.setLevel(level)
        fmt = logging.Formatter("%(asctime)s - %(levelno)s - %(filename)s - %(lineno)d - %(name)s - %(levelname)s - %(message)s")
        if file_path:
            file_handler = logging.FileHandler(file_path,mode="a",encoding="utf-8")
            file_handler.setFormatter(fmt)
            file_handler.setLevel(level)
            self.addHandler(file_handler)
        else:
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(fmt)
            stream_handler.setLevel(level)
            self.addHandler(stream_handler)



if __name__ == "__main__":
    # import os,sys
    # base_path=os.path.dirname(os.path.dirname(__file__))
    # sys.path.append(base_path)
    # from config.py_config import Configuration
    # logger = PyLogger(file_path=Configuration.logfile_path)
    # logger.error("hello")
    pass
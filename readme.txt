导入其他文件夹的模块
import os,sys
base_path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)



解决报错方法
错误信息：ResourceWarning: Enable tracemalloc to get the object allocation traceback
import warnings ：
class Test(unittest.TestCase):
       def  setUpClass(self):
            warnings.simplefilter('ignore', ResourceWarning)






就算道路且长，只要心之所向..
'''
Description: 读取excel文件
Version: 2.0
Autor: byh
Date: 2020-11-19 21:48:24
LastEditors: byh
LastEditTime: 2020-11-28 15:24:13
需要进行改造
'''
import openpyxl

class ReadExcel():
    '''读写excel'''
    def __init__(self,excel_path,sheet_name):
        self.wb=openpyxl.load_workbook(excel_path)
        self.sheet=self.wb[sheet_name]
    
    def get_title(self):
        '''获取excel的标题行'''
        title=[]
        row = self.sheet[1]
        for cell in row:
            title.append(cell.value)
        return title

    def get_content(self):
        '''获取excel的全部内容'''
        title = self.get_title()
        rows = list(self.sheet.rows)
        excel_data=[]
        for row in rows[1:]:
            value_list=[]
            for cell in row:
                value_list.append(cell.value)
            value_dict = dict(zip(title,value_list))
            excel_data.append(value_dict)
        return excel_data
    

if __name__ == "__main__":
    # from selenium.webdriver.common.by import By
    # data=ReadExcel("E:\桌面文件\cases.xlsx","Sheet3").get_content()
    # data=data[0]["method"]
    # a=eval(data)
    # print(type(a))
    pass
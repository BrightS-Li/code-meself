import os,sys,xlrd
sys.path.append(os.path.dirname(os.path.dirname(__file__))) # 本文件加入环境变量中
from configFile import filedir

class ReadExcel():
    """
    读取测试用例excel中的sheet.

    :file_excel:   测试用例excel

    :sheet_name:   测试用例表格

    例：(filedir.TEXT_EXCEL,'Sheet1')
    """
    def __init__(self,file_excel,sheet_name):
        self.data = xlrd.open_workbook(file_excel) # 打开excel文件
        self.table = self.data.sheet_by_name(sheet_name) # 通过名字获取表
        self.nrow = self.table.nrows # 获取总行数)

    def get_excel(self):
        
        '''1.更改excel表格标题为英文标题
           2.英文标题和内容一一对应
           3.返回excel中所有的测试用例[{},{},{},……]'''

        header = {
            '测试模块':'module',
            '测试编号':'number',
            '测试标题':'title',
            '接口':'url',
            '数据':'data',
            '方法':'method',
            '预期结果':'expected_result',
            '实际结果':'actual_result',
            '测试结果':'test_result'
        }

        # Excel中文标题，换成header中的英文标题
        header_head = [] # 转换后的英文标题
        excel_head = self.table.row_values(0)
        for h in excel_head:
            d = header.get(h,h)
            header_head.append(d)

        
        # 英文标题和内容对应组成列表[{},{}]
        data_list = []
        for n in range(1,self.nrow):
            excel_body = self.table.row_values(n)
            list = dict(zip(header_head,excel_body))
            data_list.append(list)
        return data_list

if __name__ == "__main__":
    A = ReadExcel(filedir.TEXT_EXCEL,'Sheet1').get_excel()
    print(A)



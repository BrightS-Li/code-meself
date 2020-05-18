import xlrd
import xlsxwriter

# 操作Excel的工具类
class Excel():
    
    # 初始化方法，参数type：r读取，w写入，file_name文件名
    def __init__(self,type,file_name):
        # 读取excel
        if type == 'r':
            # 打开文件读取数据
            self.workbook = xlrd.open_workbook(file_name)

            # 获取到所有的sheet_name,sheet1,sheet2获取到所有，获取到的是一个list
            self.sheet_names = self.workbook.sheet_names()

            # 装载所有数据的list
            self.list_data = []
        
        # 写入excel
        elif type == 'w':
            # 获得写入excel的实例
            self.workbook = xlsxwriter.workbook(file_name)
        
    def read(self):
        # 根据sheet_name去读取用例，并获取文件的总行数获取到每行内容
        for sheet_name in self.sheet_names:

            # 通过每个sheetname获取到每个页的内容
            sheet = self.workbook.sheet_by_name(sheet_name)

            # 获取有效行数
            rosw = sheet.nrows
            
            # 根据总行数进行读取
            for i in range(0,rosw):
                rowvalues = sheet.row_values(i)

                #讲每一行的内容添加进去
                self.list_data.append(rowvalues)
                # 去掉大标题第一行进行切割处理
        # 将得到的excel数据返回进行处理
        return self.list_data

def element_tojson(element):
    elements = {}
    # 将元素和接口等信息组成key和value的形式方便进行查询
    for e in element:
        elements[e[0]] = {'type':e[1],'url':e[2]}
    return elements

if __name__ == '__main__':
    file = 'frametest\element\elements.xlsx'
    e = Excel('r',file)
    list_read = e.read()

    # 读出excel表格内容
    for i in list_read:
        print(i)
    ele = element_tojson(list_read)
    print(ele['登录接口'])
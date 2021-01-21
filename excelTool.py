import xlwt
import xlrd
import copy


def readExcel(excelPath, sheetName):
    titleItemInfo = {}
    excelInfoArr = []
    # 打开一个excel表
    workbook = xlrd.open_workbook(excelPath)
    # 获取所有sheet页的名字
    # print(workbook.sheet_names())
    # 获取一个工作表
    workbook1 = workbook.sheet_by_name(sheetName)
    num_rows = workbook1.nrows
    num_cols = workbook1.ncols
    for row in range(num_rows):
        dataItemInfo = {}
        if row > 0:
            dataItemInfo = copy.deepcopy(titleItemInfo)
        for col in range(num_cols):
            if row == 0:
                # 获取标题头
                titleItemInfo[workbook1.cell_value(row, col)] = None
            if row > 0:
                cell = workbook1.cell_value(row, col)
                dataItemInfo[workbook1.cell_value(0, col)] = cell
                if col == (num_cols-1):
                    excelInfoArr.append(dataItemInfo)
    return excelInfoArr


def writeExcel(excelSavePath, sheetName, lineIndex, listIndex, value, style=None):
    if style == None:
        style = xlwt.XFStyle()
        font = xlwt.Font()
        font.name = '宋体'
        style.font = font

    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheetName)  # 在工作簿中新建一个表格
    sheet.write(lineIndex, listIndex, value, style)  # 像表格中写入数据（对应的行和列）
    workbook.save(excelSavePath)  # 保存工作簿

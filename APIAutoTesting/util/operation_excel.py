#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/2/21 10:11
# @Author : hcm
# @File : operation_excel.py
# @desc :

import xlrd
from xlutils.copy import copy
from public import config

class OperationExcel(object):
    """这是OperationExcel"""

    def __init__(self, filename=None, sheet_idx=None):
        if filename:
            self.filename = filename
            sheet_idx = sheet_idx
        else:
            self.filename = config.src_path + "/config/interface.xls"
            self.sheet_idx = 0

        self.sheet = self.get_sheet()

    def get_sheet(self):
        """
        获取sheet内容
        """
        excel = xlrd.open_workbook(self.filename)
        sheet = excel.sheets()[self.sheet_idx]
        return sheet

    def get_line_length(self):
        """
        获取行数
        """
        return self.sheet.nrows

    def get_cell_value(self, row, col):
        """
        获取单元格数据
        """
        return self.sheet.cell_value(row, col)

    def write_cell_value(self, row, col, value):
        """
        写入单元格数据
        """
        excel = xlrd.open_workbook(self.filename)
        excel_copy = copy(excel)
        sheet = excel_copy.get_sheet(0)
        sheet.write(row, col, value)
        excel_copy.save(self.filename)


if __name__ == '__main__':
    pass
    op_excel = OperationExcel()
    sheet = op_excel.get_sheet()
    print(sheet.nrows)
    print(op_excel.get_line_length())
    print(op_excel.get_cell_value(0, 0))

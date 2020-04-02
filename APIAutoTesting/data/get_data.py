#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/2/22 11:26 
# @Author : hcm 
# @File : get_data.py
# @desc :


import global_var
from util.operation_excel import OperationExcel
from util.operation_json import OperationJson


class GetData(object):
    """这是GetData"""

    def __init__(self):
        self.op_excel = OperationExcel()
        self.op_json = OperationJson()

    def get_case_lines(self):
        return self.op_excel.get_line_length()

    def get_request_url(self, row):
        col = global_var.get_col_url()
        return self.op_excel.get_cell_value(row, col)

    def get_request_method(self, row):
        col = global_var.get_col_method()

        return self.op_excel.get_cell_value(row, col)

    def get_request_data(self, row):
        col = global_var.get_col_data()
        return self.op_excel.get_cell_value(row, col)

    def get_is_run(self, row):
        col = global_var.get_col_run()
        return self.op_excel.get_cell_value(row, col)

    # 根据关键字获取请求数据json
    def get_request_data_by_json(self, row):
        key = self.get_request_data(row)
        return self.op_json.get_data(key)

    def get_header(self, row):
        col = global_var.get_col_header()
        return self.op_excel.get_cell_value(row, col)

    def get_expect_result(self, row):
        col = global_var.get_col_expect()
        return self.op_excel.get_cell_value(row, col)

    def write_actual_result(self, row, result):
        col = global_var.get_col_actual()
        return self.op_excel.write_cell_value(row, col, result)

#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/2/22 11:34 
# @Author : hcm 
# @File : global_var.py
# @desc :


class GlobalVar(object):
    """这是GlobalVar"""
    col_id = 0
    col_name = 1
    col_url = 2
    col_method = 3
    col_data = 4
    col_header = 5
    col_run = 6
    col_expect = 7
    col_actual = 8


def get_col_id():
    return GlobalVar.col_id


def get_col_name():
    return GlobalVar.col_name


def get_col_url():
    return GlobalVar.col_url


def get_col_method():
    return GlobalVar.col_method


def get_col_data():
    return GlobalVar.col_data


def get_col_header():
    return GlobalVar.col_header


def get_col_run():
    return GlobalVar.col_run


def get_col_expect():
    return GlobalVar.col_expect

def get_col_actual():
    return GlobalVar.col_actual

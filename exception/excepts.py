#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: LaiZHiYuan
@time: 2018/3/6 9:11
@file: exception.py
@desc: 异常类定义
"""


class BlankParamExcept(Exception):
    """
    空白参数异常类
    """

    def __init__(self, msg):
        Exception.__init__(self, msg)
        self.msg = msg


class NoneExcept(Exception):
    """
    参数=None异常类
    """

    def __init__(self, msg):
        Exception.__init__(self, msg)
        self.msg = msg

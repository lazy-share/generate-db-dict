#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: LaiZHiYuan
@time: 2018/3/6 10:07
@file: basic.py
@desc: 基础类
"""


class BasicSqlStatement(object):
    """
        基础SQL语句类
    """

    def callback(self, method, *args):
        """
        调用拼接函数，如果存在的话
        :param method: 函数名称
        :param args: 函数参数
        :return: 调用函数结果
        """
        method = getattr(self, method, None)
        if callable(method):
            return method(*args)


class BasicService(object):
    """
    基础服务类
    """

    def callback(self, prefix, name, *args):
        """
        调用拼接函数，如果存在的话
        :param prefix: 函数前缀
        :param name:  函数名称
        :param args: 函数参数
        :return: 调用函数结果
        """
        method = getattr(self, prefix + name, None)
        if callable(method):
            return method(*args)

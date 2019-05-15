#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: LaiZHiYuan
@time: 2019/5/12.
@desc: 断言工具类
"""
from exception.excepts import BlankParamExcept


class AssertUtils:

    @staticmethod
    def is_blank(param_val, param_name):
        if not param_val:
            raise BlankParamExcept('param {0} is blank'.format(param_name))

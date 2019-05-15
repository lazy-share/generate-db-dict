#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: LaiZHiYuan
@time: 2019/5/14.
@desc: 表
"""


class TableDto:

    def __init__(self, name, comment='', columns=[]):
        self.name = name
        self.comment = comment
        self.columns = columns

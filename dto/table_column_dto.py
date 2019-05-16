#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: LaiZHiYuan
@time: 2019/5/14.
@desc: 
"""


class TableColumnDto:

    def __init__(self, name, comment, nullable, types, pk, length):
        self.name = name
        self.comment = comment
        self.types = types
        self.length = length
        if nullable == 'NO':
            self.nullable = '否'
        else:
            self.nullable = '是'
        self.pk = pk

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
        self.nullable = nullable
        self.types = types
        self.pk = pk
        self.length = length

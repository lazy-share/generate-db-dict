#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: LaiZHiYuan
@time: 2018/3/12 14:38
@file: uuid_utils.py
@desc: 
"""
import uuid

from helper.sys_conf_helper import SysConfHelper


class UuidUtils:
    @staticmethod
    def gen_uuid():
        return str(uuid.uuid1(int(SysConfHelper.get_item("uuid", "node")))).replace('-', '')


if __name__ == '__main__':
    print(UuidUtils.gen_uuid())

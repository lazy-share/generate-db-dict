#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: LaiZHiYuan
@time: 2018/3/6 9:23
@file: sys_conf_helper.py
@desc: sys_conf.ini文件获取助手
"""
import configparser

from app_path import AppPath


class SysConfHelper:

    config = configparser.ConfigParser()
    config.read(AppPath.get_ini_file_path())

    @staticmethod
    def get_item(option, item):
        return SysConfHelper.config.get(option, item)


if __name__ == '__main__':
    print(SysConfHelper.get_item("mysql", "uri"))
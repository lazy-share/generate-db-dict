#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: LaiZHiYuan
@time: 2018/3/6 9:10
@file: db_helper.py
@desc: 获取db
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from helper.sys_conf_helper import SysConfHelper
from tools.log_util import info


class DbHelper:
    session = None

    @staticmethod
    def get_session(hostname='127.0.0.1', port='3306', username=None, pwd=None, database=None):
        """
        初始化db session
        """

        if DbHelper.session:
            return DbHelper.session

        uri = SysConfHelper.get_item("mysql", "uri_pattern")

        uri = uri.format(username=username, pwd=pwd, hostname=hostname, port=port, database=database)

        info('DbHelper', 'begin init database {0}'.format(uri))

        # 初始化数据库连接:
        engine = create_engine(uri)
        # 创建DBSession类型:
        db_session = sessionmaker(bind=engine)
        # 创建session对象:
        DbHelper.session = db_session()

        return DbHelper.session

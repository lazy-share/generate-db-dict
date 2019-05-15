#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: LaiZHiYuan
@time: 2019/5/12.
@desc: Mysql sql 语句类
"""
from base.basic import BasicSqlStatement
from tools.log_util import info


class MysqlSqlStatement(BasicSqlStatement):
    """
    Mysql sql 语法类
    """
    single = None

    @classmethod
    def get_single(cls):
        """
        获取单例
        :return:
        """
        if not cls.single:
            info("MysqlSqlStatement", "实例化[MysqlSqlStatement]类")
            cls.single = MysqlSqlStatement()
        return cls.single

    @staticmethod
    def load_tables():
        """
        加载所有表
        :return:
        """
        return 'show table status'

    @staticmethod
    def load_columns():
        """
        加载表所有列
        :return:
        """
        return 'show full fields from `{table}`'

    @staticmethod
    def table_name():
        """
        表名称关键字
        :return:
        """
        return 'NAME'

    @staticmethod
    def table_comment():
        """
        表注释关键字
        :return:
        """
        return 'COMMENT'

    @staticmethod
    def table_pk_key():
        """
        表主键关键字
        :return:
        """
        return 'KEY'

    @staticmethod
    def table_pk_val():
        """
        表主键值关键字
        :return:
        """
        return 'PRI'

    @staticmethod
    def column_name():
        """
        列名称关键字
        :return:
        """
        return 'FIELD'

    @staticmethod
    def column_type():
        """
        列类型关键字
        :return:
        """
        return 'TYPE'

    @staticmethod
    def column_comment():
        """
        列注释关键字
        :return:
        """
        return 'COMMENT'

    @staticmethod
    def column_nullable():
        """
        列是否可为null关键字
        :return:
        """
        return 'Null'

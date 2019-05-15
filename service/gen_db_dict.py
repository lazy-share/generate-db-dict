#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: LaiZHiYuan
@time: 2019/5/12.
@desc: 生成数据库字段服务类
"""
import os
from flask import request, render_template
from jinja2 import Environment, PackageLoader, select_autoescape

from app_path import AppPath
from base.basic import BasicService
from dto.table_column_dto import TableColumnDto
from dto.table_dto import TableDto
from helper.db_helper import DbHelper
from helper.sys_conf_helper import SysConfHelper
from statement.mysql_sql_statement import MysqlSqlStatement
from tools.assert_util import AssertUtils
from tools.date_utils import DateUtils
from tools.log_util import info


class GenDbDictService(BasicService):
    single = None

    @classmethod
    def get_single(cls):
        """
        获取单例
        :return:
        """
        if not cls.single:
            info("GenDbDictService", "实例化[GenDbDictService]服务类")
            cls.single = GenDbDictService()
        return cls.single

    @staticmethod
    def gen_db_dict():
        """
        数据库字典服务核心路由
        :return: 数据/模板
        """
        method = request.method.lower()
        return GenDbDictService.get_single().callback("{0}_".format(method), "gen_db_dict")

    @staticmethod
    def get_gen_db_dict():
        """
        模板渲染生成数据字典html
        :return:
        """
        return render_template('gen_db_dict.html')

    @staticmethod
    def post_gen_db_dict():
        """
        生成数据字典html
        :return:
        """
        username = request.form.get('username')
        AssertUtils.is_blank(username, 'username')
        pwd = request.form.get('password')
        hostname = request.form.get('hostname')
        AssertUtils.is_blank(hostname, 'hostname')
        port = request.form.get('port')
        AssertUtils.is_blank(port, 'port')
        database = request.form.get('database')
        AssertUtils.is_blank(database, 'database')

        sql_statement = MysqlSqlStatement.get_single()

        # 创建session对象:
        session = DbHelper.get_session(
            hostname=hostname,
            port=port,
            username=username,
            pwd=pwd,
            database=database
        )
        tables_result_set = session.execute(
            sql_statement.load_tables()
        )

        tables = []
        for ti, table_rows in enumerate(tables_result_set):
            table = TableDto(
                name=table_rows[0],
                comment=table_rows[17]
            )
            tables_columns_result_set = session.execute(
                sql_statement.load_columns().format(table=table_rows[0])
            )
            for tci, table_columns_rows in enumerate(tables_columns_result_set):
                print(table_columns_rows)
                table.columns.append(TableColumnDto(
                    name=table_columns_rows[0],
                    comment=table_columns_rows[8],
                    nullable=table_columns_rows[3],
                    pk=table_columns_rows[4] == 'PRI',
                    length=GenDbDictService.get_table_column_len(table_columns_rows[1]),
                    types=table_columns_rows[1]
                ))
            tables.append(table)

        env = Environment(
            loader=PackageLoader('generate-db-dict', 'templates'),
            autoescape=select_autoescape(['html'])
        )
        template = env.get_template('db_dict.html')

        fname = AppPath.get_project_root_path() + "/output/" + DateUtils.get_current_time()

        try:
            f = open(AppPath.get_project_root_path() + "/output/" + fname)

            f.write(template.render(tables=tables))
        finally:
            print('finally')
            # os.remove(fname)

        return render_template('gen_db_dict.html')

    @staticmethod
    def get_table_column_len(type_len_str):
        if not type_len_str:
            return ''
        if type_len_str.find('(') == -1:
            return ''
        return type_len_str[(type_len_str.find('(') + 1)
                            :type_len_str.find(')')]

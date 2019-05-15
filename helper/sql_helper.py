#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: LaiZHiYuan
@time: 2018/3/5 16:47
@file: t_example_model.py
@desc: 
"""
from com.lzy.project.admin.constant.constant import Constants
from com.lzy.project.admin.model.t_example_model import TExample
from com.lzy.project.admin.tools.log_util import info


class SqlHelper:

    @staticmethod
    def gen_del_sql(model, value_in_list, field_name='id'):
        """
        delete from table where xxx in xxx
        :param model:
        :param value_in_list:
        :param field_name:
        :return:
        """
        ids_str = ["'" + str(idd) + "'" for idd in value_in_list]
        sql = "delete from {0} where {1} in({2})".format(model.get_table_name(), field_name, ','.join(ids_str))
        info('sqlhelper', sql)
        return sql

    @staticmethod
    def gen_condition_del_sql(table, conditions):
        """
        生成 delete from ... where ...
        :param table:
        :param conditions:
        :return:
        """
        sql = "delete from {0}".format(table)
        sql += SqlHelper.gen_where(conditions, False)
        info('sqlhelper', sql)
        return sql

    @staticmethod
    def gen_select_sql(table, conditions, is_count=False):
        """
        生成 select ... from ... where ...
        :param table:
        :param conditions:
        :param is_count:
        :return:
        """
        if is_count:
            sql = "select count(*) from {0}".format(table)
        else:
            sql = "select * from {0}".format(table)
        if not 'valid_status' in conditions.keys():
            conditions['valid_status'] = Constants.VALID_STATUS_Y
        sql += SqlHelper.gen_where(conditions, is_count)
        info("genSqlHelper", sql)
        return sql

    @staticmethod
    def gen_where(conditions, is_count):
        """
        生成 where 1=1 and ...
        :param is_count: 是否查数量
        :param conditions:
        :return:
        """
        sql = " where 1=1 "
        rules = conditions['rule'] if 'rule' in conditions.keys() else {}
        rule_utils = Rule()
        for k, v in conditions.items():
            rule = Constants.QUERY_CONDITION_RULE_EQ
            if k == 'paging' or k == 'rule' or not v:
                continue
            if k.startswith('_s_'):
                rule = Constants.QUERY_CONDITION_RULE_GE
                k = k.replace('_s_', '')
            if k.startswith('_e_'):
                rule = Constants.QUERY_CONDITION_RULE_LE
                k = k.replace('_e_', '')
            if k in rules.keys():
                rule = rules[k]
            sql += rule_utils.gen_sql_by_rule(rule, k, v)
        if not is_count and 'paging' in conditions.keys():
            paging = conditions['paging']
            sql += ' limit ' + str((paging['current_page'] - 1) * paging['page_size']) + ',' + str(paging['page_size'])
        return sql


class Rule:

    def gen_sql_by_rule(self, rule, *args):
        method = getattr(self, 'rule_' + rule)
        if callable(method):
            return method(*args)

    @staticmethod
    def rule_like(k, v):
        return " and {0} like '%{1}%' ".format(str(k), str(v))

    @staticmethod
    def rule_in(k, v):
        if len(v) == 1:
            return Rule.rule_eq(k, v[0])
        value_list = ["'" + str(idd) + "'" for idd in v]
        return " and {0} in({1}) ".format(str(k), ','.join(value_list))

    @staticmethod
    def rule_ge(k, v):
        return " and {0} >= '{1}'".format(str(k), str(v))

    @staticmethod
    def rule_le(k, v):
        return " and {0} <= '{1}'".format(str(k), str(v))

    @staticmethod
    def rule_eq(k, v):
        return " and {0} = '{1}'".format(str(k), str(v))


if __name__ == '__main__':
    # print(SqlHelper.gen_select_sql(TExample(), {"name": "lsi", "age": 23, "_s_create_time": "2017-2-28",
    #                                             "_e_create_time": '2016-6-12'}))
    print(SqlHelper.gen_del_sql(TExample(), ['a', 'b', 'c']))
    print(','.join(['a', 'b']))
    dict_test = {}
    if dict_test['a']:
        print('exists')
    print('nit exists')

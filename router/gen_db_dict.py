#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: LaiZHiYuan
@time: 2018/3/5 16:47
@file: gen_db_dict.py
@desc: 路由器
"""
from flask import Blueprint, render_template

from helper.db_helper import DbHelper
from service.gen_db_dict import GenDbDictService

gen_db_dict = Blueprint(name='gen_db_dict',
                        import_name=__name__,
                        url_prefix='/',
                        static_folder='static',
                        template_folder='templates'
                        )


@gen_db_dict.errorhandler(404)
def internal_404_error(error):
    return render_template('error.html', error=error)


@gen_db_dict.errorhandler(400)
def internal_400_error(error):
    return render_template('error.html', error=error)


@gen_db_dict.errorhandler(500)
def internal_500_error(error):
    DbHelper.get_db().session.rollback()
    return render_template('error.html', error=error)


gen_db_dict.add_url_rule(rule='/', view_func=GenDbDictService.get_gen_db_dict, methods=['GET'])
gen_db_dict.add_url_rule(rule='/gen_db_dict', view_func=GenDbDictService.gen_db_dict, methods=['GET', 'POST'])

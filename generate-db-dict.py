#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: LaiZHiYuan
@time: 2019/5/12 17:47
@file: generate-db-dict.py
@desc:  生成数据库字典
"""
from flask import Flask

from router import gen_db_dict

app = Flask(__name__)
# 工具工程，开启debug模式无妨
app.debug = True

app.register_blueprint(gen_db_dict.gen_db_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

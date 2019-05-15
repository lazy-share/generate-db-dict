#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import datetime


class DateUtils:
    """
    日期、时间工具类
    """

    @staticmethod
    def get_current_time():
        """
        获取当前时间
        :return:
        """
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    print(DateUtils.get_current_time())

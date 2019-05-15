#!/usr/bin/python3
# -*- encoding:utf-8 -*-


class StringUtil:
    """
    字符串工具类
    """

    @staticmethod
    def _contain_chinese(string):
        """
        是否包含中文
        :param string: 字符串
        :return: 布尔值
        """
        for ch in string:
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
        return False

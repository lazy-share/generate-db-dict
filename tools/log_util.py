#!/usr/bin/python3
# -*- encoding:utf-8 -*-
import logging
import logging.config

from app_path import AppPath

logging.config.fileConfig(AppPath.get_conf_path() + "/log.conf")


def debug(log_name, msg):
    if not log_name:
        log_name = "sys"
    logger = logging.getLogger(log_name)
    logger.debug(msg)


def info(log_name, msg):
    if not log_name:
        log_name = "sys"
    logger = logging.getLogger(log_name)
    logger.info(msg)


def error(log_name, msg):
    if not log_name:
        log_name = "sys"
    logger = logging.getLogger(log_name)
    logger.error(msg)


def warning(log_name, msg):
    if not log_name:
        log_name = "sys"
    logger = logging.getLogger(log_name)
    logger.warning(msg)


if __name__ == "__main__":
    info(log_name='log_util', msg="test info")
    error(log_name='log_util', msg="test error")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .key_value_manager import KeyValueManager

r_config = {
    'host': '127.0.0.1',
    'port': 6379,
    'decode_responses': True,
    'password': ''
}
sql_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '123456',
    'database': 'version_controller',
}
# 尝试导入自定义配置（这个是带密码的）
try:
    from .myconfig import redis_config, mysql_config

    r_config = redis_config
    sql_config = mysql_config
except BaseException as e:
    print('use default mysql and redis config')

# 创建实例
c = KeyValueManager(r_config, sql_config)

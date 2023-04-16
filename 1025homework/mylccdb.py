# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 07:14:00 2022

@author: User
"""

import pymysql

dbsetting = {
    "host":"127.0.0.1",
    "port":3306,
    "user":"root",
    "password":"123456789",
    "db":"jobs",
    "charset":"utf8"
    }

conn = pymysql.connect(**dbsetting)

# !/usr/bin/env python
# -*-coding:UTF-8-*-
# __author__ = pighui
# __time__ = 2019-11-14 下午2:30
import redis


class Dao():
    def __init__(self):
        self.conn = redis.Redis(db=9, decode_responses=True)

    def write(self, name, value):
        self.conn.setnx(name, value)

    def read(self):
        all_number = []
        keys = self.conn.keys()
        for key in keys:
            value = self.conn.get(key)
            number_list = value.split("#")[0].split('_')
            all_number += number_list
        return all_number

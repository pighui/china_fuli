# !/usr/bin/env python
# -*-coding:UTF-8-*-
# __author__ = pighui
# __time__ = 2019-11-14 下午3:57
import time

from analysis import Forecast
from spider.double import Chromosphere
from datetime import date, datetime


def update_data():
    # weekend = date(2019, 11, 10)
    # now = date.today()
    # week = (now - weekend).days % 7
    # hour = datetime.now().hour
    # # 每周2,4,7晚21:15开奖
    # if week in [2, 4, 0] and hour >= 22:
    #     # 更新最新的开奖数据
    chromosphere = Chromosphere()
    #     print("更新了最新一期的数据")
    print("数据已更新")
def next_number():
    forecast = Forecast()


if __name__ == '__main__':
    update_data()
    next_number()


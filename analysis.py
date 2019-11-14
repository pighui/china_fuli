# !/usr/bin/env python
# -*-coding:UTF-8-*-
# __author__ = pighui
# __time__ = 2019-11-14 下午2:44
from rdao import Dao
from collections import Counter


class Forecast():
    def __init__(self):
        self.dao = Dao()
        self.get()

    def get(self):
        number = self.dao.read()
        self.count(number)

    def count(self, number):
        first_number = number[::7]
        average = int(len(first_number) * 7 / 33)
        second_number = number[1::7]
        third_number = number[2::7]
        fourth_number = number[3::7]
        fifth_number = number[4::7]
        sixth_number = number[5::7]
        seventh_number = number[6::7]
        first_count = Counter(first_number).most_common(1).pop()
        second_count = Counter(second_number).most_common(1).pop()
        third_count = Counter(third_number).most_common(1).pop()
        fourth_count = Counter(fourth_number).most_common(1).pop()
        fifth_count = Counter(fifth_number).most_common(1).pop()
        sixth_count = Counter(sixth_number).most_common(1).pop()
        seventh_count = Counter(seventh_number).most_common(1).pop()
        result = [[first_count, second_count, third_count, fourth_count, fifth_count, sixth_count, seventh_count],
                  average]
        self.divine(result)

    def divine(self, data):
        most_number = data[0]
        average = data[1]
        numbers = ''
        all_chance = 0
        for i in range(len(most_number)):
            number, count = most_number[i]
            probability = count / average * 100
            numbers += number + ' '
            all_chance += probability
        chance = round(all_chance / 7, 2)
        print("预测号码：%s"%numbers.strip())
        print("中奖概率：%s" % chance + '%')
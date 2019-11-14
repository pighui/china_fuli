# !/usr/bin/env python
# -*-coding:UTF-8-*-
# __author__ = pighui
# __time__ = 2019-11-14 上午11:33


import requests

from rdao import Dao
from spider.util.html import to_html
from lxml import etree
from tqdm import tqdm, trange


class Chromosphere():
    def __init__(self):
        self.dao = Dao()
        self.url = 'http://datachart.500.com/ssq/history/newinc/history.php?limit=5000&sort=0'
        self.get()

    def get(self):
        response = requests.get(self.url)
        resp_bytes = response.content
        html = to_html(resp_bytes)
        self.parse(html)

    def parse(self, html):
        root = etree.HTML(html)
        phase_list = root.xpath("//tr[@class='t_tr1']/td[1]/text()")
        red_ball_list = root.xpath("//tr[@class='t_tr1']/td[@class='t_cfont2']/text()")
        blue_ball_list = root.xpath("//tr[@class='t_tr1']/td[@class='t_cfont4'][1]/text()")
        date_list = root.xpath("//tr[@class='t_tr1']/td[last()]/text()")
        for i in trange(len(phase_list)):
            # item = {
            #     'phase': phase_list[i],
            #     'number': red_ball_list[i*6:i*6+6] + [blue_ball_list[i]],
            #     'date': date_list[i],
            # }
            name = phase_list[i]
            value = '_'.join(red_ball_list[i * 6:i * 6 + 6] + [blue_ball_list[i]]) + '#' + date_list[i]
            self.dao.write(name, value)

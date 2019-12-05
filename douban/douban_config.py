#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : douban_config.py
# @Author: wu gang
# @Date  : 2019-12-05
# @Desc  : 豆瓣配置
# @Contact: 752820344@qq.com

base_url = "https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&"
year = 2019
start = 2080
start_range = 20

cookie = "douban-fav-remind=1; ll=\"108288\"; bid=ABS9ESA9NH0; __utmc=30149280; __utmz=30149280.1575370013.16.13.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; __utmc=223695111; push_noty_num=0; push_doumail_num=0; ap_v=0,6.0; __utma=30149280.1047098624.1533107994.1575459020.1575529613.18; __utmv=30149280.14211; __utma=223695111.1753693179.1557830749.1575459020.1575531179.6; __utmb=223695111.0.10.1575531179; __utmz=223695111.1575531179.6.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmb=30149280.31.10.1575529613"

movie_file = "../data/douban/movie_" + str(year) + ".csv"
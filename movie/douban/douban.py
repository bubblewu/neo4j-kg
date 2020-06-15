#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : douban.py
# @Author: wu gang
# @Date  : 2019-12-05
# @Desc  : 
# @Contact: 752820344@qq.com

import json
import time

from movie import douban as config
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

from base.spider_util import download_requests


def parse(html):
    soup = BeautifulSoup(html)
    movie_item_soup = soup.find("div", {"class": "list-wp"}).findAll("div", {"class": "item"})
    if movie_item_soup is None:
        print("ERROR: 请检查spider")
    else:
        for movie_item in movie_item_soup:
            poster_div = movie_item.find("div", {"class": "poster"})
            # 封面
            img_url = poster_div.find("img").get("src")
            info_div = movie_item.find("div", {"class": "info"})
            title = info_div.find("a", {"class": "title"})
            rating = info_div.find("span", {"class": "rating"})
            cast = info_div.find("p", {"class": "cast"}).getText().split("\xa0")

            print(title)


def parse_json(data):
    movie_list = list()
    try:
        data_json = json.loads(data)
        data_list = data_json["data"]

        for d in data_list:
            directors = d['directors']
            src = d['url']
            movie_name = d['title']
            actors = d['casts']
            cover = d['cover']
            rate = d['rate']
            star = d['star']
            id = d['id']

            movie_info = {
                'id': id,
                'movie_name': movie_name,
                'year': config.year,
                'directors': "/".join(directors),
                'actors': "/".join(actors),
                'rate': rate,
                'star': star,
                'src': src,
                'cover': cover
            }
            movie_list.append(movie_info)
    except:
        print("ERROR：接口返回信息错误。%s" % data)
    print("this page get movie count: %d" % len(movie_list))
    return movie_list


def save(movie_list):
    data = pd.DataFrame({
        'id': [index for index in range(len(movie_list))],
        'movie_name': [movie['movie_name'] for movie in movie_list],
        'year': [movie['year'] for movie in movie_list],
        'directors': [movie['directors'] for movie in movie_list],
        'actors': [movie['actors'] for movie in movie_list],
        'rate': [movie['rate'] for movie in movie_list],
        'star': [movie['star'] for movie in movie_list],
        'src': [movie['src'] for movie in movie_list],
        'cover': [movie['cover'] for movie in movie_list],
        'douban_id': [movie['id'] for movie in movie_list]
    })
    data.to_csv(config.movie_file, index=False, encoding="UTF-8")
    print("save movie info successfully: %s" % config.movie_file)


def start():
    begin = time.time()
    year_range = str(config.year) + "," + str(config.year)
    start_index = config.start
    data_list = list()
    while 1:
        url = config.base_url + "start=" + str(start_index) + "&year_range=" + year_range
        html = download_requests(url)
        movie_list = parse_json(html)
        if len(movie_list) < 1:
            save(data_list)
            print("总共获取电影: [%d]条，耗时: %s" % (len(data_list), time.time() - begin))
            break
        data_list.extend(movie_list)
        start_index += config.start_range
        time.sleep(np.random.rand() * 10)
    save(data_list)
    print("总共获取电影: [%d]条，耗时: %s" % (len(data_list), time.time() - begin))


if __name__ == '__main__':
    start()

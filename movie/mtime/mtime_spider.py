#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : mtime_spider.py
# @Author: wu gang
# @Date  : 2019-12-04
# @Desc  : 时光网电影Top100数据抓取
# @Contact: 752820344@qq.com

import requests
from bs4 import BeautifulSoup

import movie.mtime.mtime_config as config
from movie.mtime.mtime_config import IndexRange


def download(url):
    """
    下载URL的HTML文件
    :param url: url地址
    :return: html
    """
    print("start download: %s" % url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        'Cookie': config.cookie,
        'Cache-Control': "no-cache",
        'Postman-Token': "aa12e090-e228-4fe8-be1c-313f8597cf0a,30af4ed1-996a-4b7e-a002-5f32d833476a",
        'Host': "www.mtime.com",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    return response.text


def parse(html):
    """
    对下载的网页进行解析
    :param html: Url的html内容
    :return: 全部电影信息的list，也就是movie_list
    """
    print("start parse html data...")
    soup = BeautifulSoup(html, features="lxml")
    movie_list = list()
    # 获取电影列表信息
    movie_list_soup = soup.find("ul", attrs={'id': 'asyncRatingRegion'})
    if movie_list_soup is None:
        print("ERROR: 请检查spider的Cookies")
    else:
        for movie_li in movie_list_soup.find_all('li'):
            # 排名
            rank = movie_li.find('div', attrs={'class': 'number'}).getText()
            # movie主要信息
            movie_info = movie_li.find('div', attrs={'class': 'mov_con'})
            movie_temp = movie_info.find('a').getText().split("\xa0")
            # 电影名
            movie_name = movie_temp[0]
            # 年份
            year = movie_temp[1].split(" ")[-1].replace('(', '').replace(')', '')
            # 电影英文名
            movie_en_name = movie_temp[1][:-7]
            # print(movie_en_name)
            # 电影封面图
            pic = movie_li.find('div', attrs={'class': 'mov_pic'}).find("img", attrs={'class': 'img_box'})['src']
            src = movie_info.find('a')['href']
            person_info = movie_info.select('p')
            # 导演
            director = person_info[0].find('a').string
            # 主演
            movie_actor = []
            for act in person_info[1].find_all('a'):
                movie_actor.append(act.string)

            movie_info_all = {'rank': rank,
                              'src': src,
                              'movie_name': movie_name,
                              'movie_en_name': movie_en_name,
                              'year': year,
                              'director': director,
                              'actor': movie_actor,
                              'image': pic
                              }
            movie_list.append(movie_info_all)
    print("get movie count: %d" % len(movie_list))
    return movie_list


def get_movie_list(url):
    # /index-2.html
    movie_data = list()
    for i in range(config.total_page_count):
        index = i + 1
        if index == 1:
            new_url = url.replace("index-{PAGE}.html", "")
        else:
            new_url = url.replace("{PAGE}", str(index))
        movie_data.extend(parse(download(new_url)))
    return movie_data


def handle_person(movie_list):
    """
    处理导演和主演数据，建立唯一词典
    :param movie_list: 电影数据
    :return: 导演和主演词典
    """
    director_list, actor_list = list(), list()
    dir_dic, actor_dic, movie_dic = dict(), dict(), dict()
    for movie in movie_list:
        director_list.append(movie['director'])
        actor_list.extend(movie['actor'])
    director_set = set(director_list)
    actor_set = set(actor_list)
    # movie_set = set(movies)

    for index, value in enumerate(director_set):
        dir_dic[index] = value
    for index, value in enumerate(actor_set):
        actor_dic[index] = value
    for index, value in enumerate(movie_list):
        movie_dic[index + IndexRange.MOVIE_START_INDEX.value] = value['movie_name']

    return dir_dic, actor_dic, movie_dic

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : gen_entity.py
# @Author: wu gang
# @Date  : 2019-12-04
# @Desc  : 生成相关实体信息：电影、导演、主演
# @Contact: 752820344@qq.com

import pandas as pd

import mtime.mtime_config as config
from mtime.mtime_config import IndexRange


def save_movie_entity(movie_list):
    """
    生成节点csv文件：电影信息
    :param movie_list:
    :return:
    """
    data = pd.DataFrame({
        "index:ID": [index + IndexRange.MOVIE_START_INDEX.value for index in range(len(movie_list))],
        'rank': [movie['rank'] for movie in movie_list],
        'src': [movie['src'] for movie in movie_list],
        'name': [movie['movie_name'] for movie in movie_list],
        'movie_en': [movie['movie_en_name'] for movie in movie_list],
        'year': [movie['year'] for movie in movie_list],
        'image': [movie['image'] for movie in movie_list],
        ':LABEL': '电影表'
    })
    data.to_csv(config.movie_entity_file, index=False, encoding="UTF-8")
    print("save movie entity info successfully: %s" % config.movie_entity_file)


def save_director_entity(director_dict):
    """
    生成节点csv文件：导演信息
    :param director_dict: 所有导演词典
    :return:
    """
    data = pd.DataFrame({
        'index:ID': [item + IndexRange.DIRECTOR_START_INDEX.value for item in director_dict.keys()],
        'director': [val for val in director_dict.values()],
        ':LABEL': '导演表'
    })
    data.to_csv(config.director_entity_file, index=False, encoding="UTF-8")
    print("save director entity info successfully: %s" % config.director_entity_file)


def save_actor_entity(actor_dict):
    """
    生成节点csv文件：主演信息
    :param actor_dict: 所有演员词典
    :return:
    """
    data = pd.DataFrame({
        'index:ID': [item + IndexRange.ACTOR_START_INDEX.value for item in actor_dict.keys()],
        'actor': [val for val in actor_dict.values()],
        ':LABEL': '演员表'
    })
    data.to_csv(config.actor_entity_file, index=False, encoding="UTF-8")
    print("save actor entity info successfully: %s" % config.actor_entity_file)


def save_all_entity(movie_list, director_dict, actor_dict):
    save_movie_entity(movie_list)
    save_director_entity(director_dict)
    save_actor_entity(actor_dict)

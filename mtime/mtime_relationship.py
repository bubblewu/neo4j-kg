#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : mtime_relationship.py
# @Author: wu gang
# @Date  : 2019-12-04
# @Desc  : 关系：电影、导演、演员
# @Contact: 752820344@qq.com

import pandas as pd

import mtime.mtime_config as config
from mtime.mtime_config import IndexRange


def save_movie_director_relationship(movie_list, movie_dict, director_dict):
    data = pd.DataFrame({
        ':START_ID': [list(director_dict.keys())
                      [list(director_dict.values()).index(movie['director'])] + IndexRange.DIRECTOR_START_INDEX.value
                      for movie in movie_list],
        ':END_ID': [list(movie_dict.keys())[list(movie_dict.values()).index(movie['movie_name'])]
                    for movie in movie_list],
        'relation': '导演',
        ':TYPE': '导演'
    })
    data.to_csv(config.movie_director_relationship_file, index=False, encoding="UTF-8")
    print("save movie director relationship successfully: %s" % config.movie_director_relationship_file)


def save_movie_actor_relationship(movie_list, movie_dict, actor_dict):
    relation_list = []
    for movie in movie_list:
        for actor_info in movie['actor']:
            actor_index = list(actor_dict.keys())[list(actor_dict.values()).index(actor_info)]
            movie_index = list(movie_dict.keys())[list(movie_dict.values()).index(movie['movie_name'])]
            info = {
                'actor_index': actor_index,
                'movie_index': movie_index
            }
            relation_list.append(info)

    data = pd.DataFrame({
        ':START_ID': [relation['actor_index'] + IndexRange.ACTOR_START_INDEX.value for relation in relation_list],
        ':END_ID': [relation['movie_index'] for relation in relation_list],
        'relation': '主演',
        ':TYPE': '主演'
    })
    data.to_csv(config.movie_actor_relationship_file, index=False, encoding="UTF-8")
    print("save movie actor relationship successfully: %s" % config.movie_actor_relationship_file)


def save_director_actor_relationship(movie_list, director_dict, actor_dict):
    relation_list = []
    for movie in movie_list:
        for actor_info in movie['actor']:
            actor_index = list(actor_dict.keys())[list(actor_dict.values()).index(actor_info)]
            dir_index = list(director_dict.keys())[list(director_dict.values()).index(movie['director'])]
            info = {
                'actor_index': actor_index,
                'dir_index': dir_index
            }
            relation_list.append(info)

    data = pd.DataFrame({
        ':START_ID': [relation['dir_index'] + IndexRange.DIRECTOR_START_INDEX.value for relation in relation_list],
        ':END_ID': [relation['actor_index'] + IndexRange.ACTOR_START_INDEX.value for relation in relation_list],
        'relation': '相关',
        ':TYPE': '相关'
    })
    data.to_csv(config.director_actor_relationship_file, index=False, encoding="UTF-8")
    print("save director actor relationship successfully: %s" % config.director_actor_relationship_file)


def save_all_relationship(movie_list, director_dict, actor_dict, movie_dict):
    save_movie_director_relationship(movie_list, movie_dict, director_dict)
    save_movie_actor_relationship(movie_list, movie_dict, actor_dict)
    save_director_actor_relationship(movie_list, director_dict, actor_dict)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : mtime_main.py
# @Author: wu gang
# @Date  : 2019-12-04
# @Desc  : 基于Neo4j的时光网电影Top100知识图谱构建
# @Contact: 752820344@qq.com

import time

import movie.mtime.gen_entity as entity
import movie.mtime.mtime_config as config
import movie.mtime.mtime_relationship as relationship
import movie.mtime.mtime_spider as spider

"""
- 生成相关的CSV文件
- 导入Neo4j：

"""

if __name__ == '__main__':
    start = time.time()
    movie_list = spider.get_movie_list(config.url_top)
    if len(movie_list) > 0:
        director_dict, actor_dict, movie_dict = spider.handle_person(movie_list)
        entity.save_all_entity(movie_list, director_dict, actor_dict)
        relationship.save_all_relationship(movie_list, director_dict, actor_dict, movie_dict)

    print("total costs %s ms" % (time.time() - start))


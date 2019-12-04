#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : mtime_config.py
# @Author: wu gang
# @Date  : 2019-12-04
# @Desc  : 时光网相关配置
# @Contact: 752820344@qq.com

from enum import Enum


class IndexRange(Enum):
    """
    区分电影、导演、主演信息的index
    """
    MOVIE_START_INDEX = 10000
    DIRECTOR_START_INDEX = 20000
    ACTOR_START_INDEX = 30000


url_top = "http://www.mtime.com/top/movie/top100/index-{PAGE}.html"
total_page_count = 10
cookie = "_userCode_=20191241022137701; _userIdentity_=20191241022133404; DefaultCity-CookieKey=290; DefaultDistrict-CookieKey=0; __utmc=196937584; __utmz=196937584.1575426135.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _tt_=898E1207454C922116723F795772FF9D; guessIndex=0; _movies_=254343; maxShowNewbie=1; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; __utma=196937584.1712474831.1575426135.1575428276.1575446260.3; _ydclearance=95ad85bbce171b9b4452475c-ff11-4b1d-afaf-1055cec16cd4-1575460886"

base_path = "../data/mtime/"
# 实体文件
movie_entity_file = base_path + "mtime_movie_entity.csv"
director_entity_file = base_path + "mtime_director_entity.csv"
actor_entity_file = base_path + "mtime_actor_entity.csv"

# 关系文件
movie_director_relationship_file = base_path + "mtime_movie_director_relationship.csv"
movie_actor_relationship_file = base_path + "mtime_movie_actor_relationship.csv"
director_actor_relationship_file = base_path + "mtime_director_actor_relationship.csv"

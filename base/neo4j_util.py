#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : neo4j_util.py
# @Author: wu gang
# @Date  : 2020-06-15
# @Desc  : 
# @Contact: 752820344@qq.com

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from py2neo import Graph
import article.hlm.hlm_config as config


class NeoDB(object):
    def __init__(self):
        self.graph = Graph(config.neo4j_uri, username=config.neo4j_user, password=config.neo4j_password)

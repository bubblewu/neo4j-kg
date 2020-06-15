#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : data_to_neo4j.py
# @Author: wu gang
# @Date  : 2020-06-15
# @Desc  : 将《红楼梦》的人物关系数据导入Neo4j数据库
# @Contact: 752820344@qq.com

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import article.hlm.hlm_config as config
from base.neo4j_util import NeoDB


class ImportNeo(object):
    def __init__(self):
        self.graph = NeoDB()
        self.categories = config.categories
        self.similar_words = config.similar_words

    def create_graph(self, relationship_file=config.relationship_file):
        """
        构造图数据，将relationships.txt文件数据写入neo4j数据库
        :param relationship_file:
        :return:
        """
        with open(relationship_file, mode="r") as read:
            for line in read.readlines():
                # name1, name2, 关系, name1_from, name2_from
                # 贾演, 贾代化, 父亲, 贾家宁国府, 贾家宁国府
                # 贾代化, 贾演, 儿子, 贾家宁国府, 贾家宁国府
                # ...
                # 贾母,贾赦,母亲,史家,贾家荣国府
                relationship_array = line.strip("\n").split(",")
                print(relationship_array)
                # 生成Person实体：[类别, 人物]。
                # 所有人物对应的类别（府邸）构造Person实体：│{"cate":"贾家宁国府","Name":"贾演"}│
                self.graph.run("MERGE(p: Person {cate: $cate, Name: $name})",
                               {"cate": relationship_array[3], "name": relationship_array[0]})
                # │{"cate":"贾家宁国府","Name":"贾代化"}│
                self.graph.run("MERGE(p: Person {cate: $cate, Name: $name})",
                               {"cate": relationship_array[4], "name": relationship_array[1]})
                # 人物关系生成：
                # │[{"cate":"贾家宁国府","Name":"贾演"},{"relation":"父亲"},{"cate":"贾家宁国府","Name":"贾代化"}]│
                # │[{"cate":"贾家宁国府","Name":"贾代化"},{"relation":"儿子"},{"cate":"贾家宁国府","Name":"贾演"}]│
                self.graph.run(
                    "MATCH (p1: Person), (p2: Person) WHERE p1.Name = $name_1 AND p2.Name = $name_2 "
                    "CREATE (p1) - [r: %s {relation: $relation}] -> (p2) RETURN r" % (relationship_array[2]),
                    {"name_1": relationship_array[0], "name_2": relationship_array[1], "relation": relationship_array[2]}
                )


if __name__ == '__main__':
    neo = ImportNeo()
    neo.create_graph()

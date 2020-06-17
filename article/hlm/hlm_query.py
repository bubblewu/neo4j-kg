#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : hlm_query.py
# @Author: wu gang
# @Date  : 2020-06-16
# @Desc  : 
# @Contact: 752820344@qq.com

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from base.neo4j_util import NeoDB
import article.hlm.hlm_config as config
import base64
from base.token_util import Token
import json

neo = NeoDB()
token = Token()


def query(name):
    data = neo.graph.run("MATCH (p)-[r]->(n:Person {Name: '%s'}) "
                         "RETURN p.Name, r.relation, n.Name, p.cate, n.cate "
                         "UNION ALL "
                         "MATCH(p:Person {Name: '%s'})-[r]->(n) "
                         "RETURN p.Name, r.relation, n.Name, p.cate, n.cate"
                         % (name, name))
    data = list(data)
    return get_json_data(data)


def get_json_data(data):
    json_data = {"data": [], "links": []}
    data_list = list()
    for record in data:
        data_list.append(record["p.Name"] + "_" + record["p.cate"])
        data_list.append(record["n.Name"] + "_" + record["n.cate"])
        data_list = list(set(data_list))
    name_dict = {}  # 姓名及其索引：<class 'dict'>: {'王熙凤': 0, '王子腾': 1, '贾琏': 2, '巧姐': 3, '王夫人': 4, '邢夫人': 5}
    count = 0
    for d in data_list:
        cur_array = d.split("_")
        data_item = {}
        name_dict[cur_array[0]] = count
        count += 1
        data_item['name'] = cur_array[0]  # 姓名
        data_item['category'] = config.categories[cur_array[1]]  # 府邸索引
        json_data['data'].append(data_item)
    for record in data:
        link_item = {}
        link_item['source'] = name_dict[record["p.Name"]]  # 相关人员
        link_item['target'] = name_dict[record['n.Name']]  # 目标人
        link_item['value'] = record['r.relation']  # 关系
        json_data['links'].append(link_item)
    return json_data


def get_target_array(question):
    """
    句子分词并标注词性，返回实体和关系
    :param question: 用户输入的问句，如"贾宝玉的爸爸的爸爸的老婆是谁？"
    :return target_array: 如 <class 'list'>: ['贾宝玉', '爸爸', '爸爸', '老婆', '的']
    """
    word_list = token.cut_words(question, enable_pos=True)
    target_pos = ['nr', 'n']
    target_array = []
    # seg_array = []
    for w in word_list:
        wp = w.split(" ")
        # seg_array.append(wp[0])
        if wp[1] in target_pos:
            target_array.append(wp[0])
    # target_array.append(seg_array[1])
    return target_array


def get_qa_answer(question):
    target_array = get_target_array(question)
    result_list = list()  # 结果集合
    for i in range(len(target_array) - 1):
        if i == 0:
            name = target_array[0]
        else:
            name = result_list[-1]['p.Name']  # 多层关系时，获取上一个关系结果的人物Name
        relationship = target_array[i + 1]
        data = neo.graph.run(
            "match(p)-[r:%s{relation: '%s'}]->(n:Person{Name:'%s'}) return  p.Name,n.Name,r.relation,p.cate,n.cate" % (
                config.similar_words[relationship], config.similar_words[relationship], name)
        )
        data = list(data)
        print(data)
        result_list.extend(data)
        print("===" * 36)

    with open(config.images_path + "%s.jpg" % (str(result_list[-1]['p.Name'])), "rb") as image:
        base64_data = base64.b64encode(image.read())
        b = str(base64_data)

    return [get_json_data(result_list), get_profile(str(result_list[-1]['p.Name'])), b.split("'")[1]]


def get_profile(name):
    """
    生成待展示人物相关信息HTML数据
    :param name: 待展示人物
    :return:
    """
    with open(config.user_info_data, encoding='utf-8')as f:
        data = json.load(f)
    s = ''
    for i in data[name]:
        st = "<dt class = \"basicInfo-item name\" >" + str(i) + " \
        <dd class = \"basicInfo-item value\" >" + str(data[name][i]) + "</dd >"
        s += st
    return s


def get_answer_profile(name):
    with open(config.images_path + "%s.jpg" % (str(name)), "rb") as image:
        base64_data = base64.b64encode(image.read())
        b = str(base64_data)
    return [get_profile(str(name)), b.split("'")[1]]

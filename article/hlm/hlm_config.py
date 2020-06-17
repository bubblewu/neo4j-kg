#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : hlm_config.py
# @Author: wu gang
# @Date  : 2020-06-15
# @Desc  : 相关配置
# @Contact: 752820344@qq.com

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

neo4j_uri = "http://localhost:7474"
neo4j_user = "neo4j"
neo4j_password = "qwe123"

relationship_file = "../../data/article/hlm/relationships.txt"
images_path = "./images/"
user_info_data = "./json/data.json"

categories = {"贾家荣国府": 0, "贾家宁国府": 1, "王家": 2, "史家": 3, "薛家": 4, "其他": 5, "林家": 6}
similar_words = {
    "爸爸": "父亲",
    "妈妈": "母亲",
    "爸": "父亲",
    "妈": "母亲",
    "父亲": "父亲",
    "母亲": "母亲",
    "儿子": "儿子",
    "女儿": "女儿",
    "丫环": "丫环",
    "兄弟": "兄弟",
    "妻": "妻",
    "老婆": "妻",
    "哥哥": "哥哥",
    "表妹": "表兄妹",
    "弟弟": "弟弟",
    "妾": "妾",
    "养父": "养父",
    "姐姐": "姐姐",
    "娘": "母亲",
    "爹": "父亲",
    "father": "父亲",
    "mother": "母亲",
    "朋友": "朋友",
    "爷爷": "爷爷",
    "奶奶": "奶奶",
    "孙子": "孙子",
    "老公": "丈夫",
    '岳母': '岳母',
    "表兄妹": "表兄妹",
    "孙女": "孙女",
    "嫂子": "嫂子",
    "暧昧": "暧昧"
}

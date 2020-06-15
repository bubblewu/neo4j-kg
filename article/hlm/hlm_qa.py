#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : hlm_qa.py
# @Author: wu gang
# @Date  : 2020-06-15
# @Desc  : 《红楼梦》简单的问答
# @Contact: 752820344@qq.com

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import logging
logging.basicConfig(level=logging.INFO)
from base.token_util import Token
from base.neo4j_util import NeoDB
import article.hlm.hlm_config as config
import re


class QA(object):
    def __init__(self):
        self.neo = NeoDB()
        self.token = Token()

    def cut_words(self, text):
        """
        句子分词并标注词性
        :param text: 用户输入的问句，如"贾宝玉的爸爸是谁"
        :return person: str 问题的主要人物，eg：贾宝玉
        :return words: 如['爸爸', '妈妈']
        """
        word_list = self.token.cut_words(text, enable_pos=True)
        person = ''
        words = list()
        for w in word_list:
            wp = w.split(" ")
            if wp[1] == 'nr':
                person = wp[0]
            if wp[1] == 'n':
                words.append(config.similar_words[wp[0]])
        logging.info(str(words))
        return person, words

    def qa(self, question):
        """
        简单用户关系QA
        :param question: 用户输入的问句，如"贾宝玉的爸爸是谁"
        :return:
        """
        try:
            question = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", question)
            question = re.sub('\W+', '', question).replace("_", '')
            person, words = self.cut_words(question)
            # 0来占位
            words_ = [0 for i in range(len(words))]
            for i in range(len(words)):
                words_[i] = '-[r' + str(i) + ':' + words[len(words) - i - 1] + ']'
                if i != len(words) - 1:
                    words_[i] += '->(n' + str(i) + ':Person)'
            query = "match(p)" + ''.join(words_) + \
                    "->(n:Person{Name:'" + person + \
                    "'}) return  p.Name,n.Name,p.cate,n.cate"
            logging.info("query: %s", query)
        except Exception as e:
            return "错误的提问！！！"

        try:
            data = self.neo.graph.run(query)
            data = list(data)[0]
            logging.info(str(data))

            result = data['n.cate'] + '的【' + data['n.Name'] + "】"
            for item in words:
                result += '的'
                result += item
            result += '是'
            result += data['p.cate'] + '的【' + data['p.Name'] + "】"
            return result
        except Exception as e:
            return "没有找到正确的答案！"


if __name__ == '__main__':
    answer = QA()
    print(answer.qa("贾宝玉的爸爸是谁？"))
    print(answer.qa("贾宝玉的爸爸的爸爸的老婆是谁？"))

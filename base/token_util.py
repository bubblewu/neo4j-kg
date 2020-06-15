#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : token_util.py
# @Author: wu gang
# @Date  : 2020-06-15
# @Desc  : 分词工具：jieba
# @Contact: 752820344@qq.com

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import jieba
import jieba.posseg as pseg


class Token(object):

    def cut_words(self, text, enable_pos=False):
        """
        分词
        :param text: 文本
        :param enable_pos: 是否显示词性POS
        :return: 词语集合
        """
        # words_arr = "|".join(jieba.cut(text))
        # return words_arr.split("|")
        # jieba.enable_paddle()
        words = list(jieba.cut(text))
        if enable_pos:
            return self.get_pos_array(text)
        return words

    def get_pos_array(self, text):
        """
        分词并获取词性
        :param text: 文本
        :return: eg：['今天 t', '是 v', '个 q', '好日子 l']
        """
        result = list()
        word_pos_list = pseg.cut(text)
        for wp in word_pos_list:
            # print(wp.word, wp.flag)
            result.append(wp.word + " " + wp.flag)
        return result


if __name__ == '__main__':
    print(Token().cut_words("今天是个好日子"))
    print(Token().cut_words("今天是个好日子", True))

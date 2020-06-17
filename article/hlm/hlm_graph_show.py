#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : hlm_graph_show.py
# @Author: wu gang
# @Date  : 2020-06-15
# @Desc  : 基于Neo4j的《红楼梦》人物关系图谱可视化及问答
# @Contact: 752820344@qq.com

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from flask import Flask, render_template, request, jsonify

import article.hlm.hlm_query as hq

# app = Flask(__name__, template_folder='./web/templates')
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index(name=None):
    return render_template('index.html', name=name)


@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html')


@app.route('/qa', methods=['GET', 'POST'])
def qa():
    return render_template('qa.html')


@app.route('/get_all_relation', methods=['GET', 'POST'])
def get_all_relation():
    return render_template('all_relation.html')


@app.route('/search_name', methods=['GET', 'POST'])
def search_name():
    name = request.args.get('name')
    json_data = hq.query(str(name))
    return jsonify(json_data)


@app.route('/qa_answer', methods=['GET', 'POST'])
def qa_answer():
    question = request.args.get('name')
    json_data = hq.get_qa_answer(str(question))
    return jsonify(json_data)


@app.route('/get_profile', methods=['GET', 'POST'])
def get_profile():
    name = request.args.get('character_name')
    json_data = hq.get_answer_profile(name)
    return jsonify(json_data)


if __name__ == '__main__':
    app.debug = True
    app.run(port=8082)

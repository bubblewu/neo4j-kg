#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : MovieGraphShow.py
# @Author: wu gang
# @Date  : 2020-06-11
# @Desc  : 基于neo4j + D3.js的时光网电影图谱展示
# @Contact: 752820344@qq.com

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json

import pandas as pd
from py2neo import Graph

from movie.web.bottle import get, run, request, response, static_file

graph = Graph("http://neo4j:qwe123@localhost:7474")


@get("/")
def get_index_page():
    return static_file("index-movie.html", root="../web")


@get("/graph")
def get_graph():
    results = graph.run("MATCH (m:`电影表`) <-[:`主演`]-(a:`演员表`) "
                        "RETURN m.name as movie, collect(a.actor) as actors "
                        "LIMIT 100;")
    nodes = []
    rels = []
    i = 0
    for movie, actors in results:
        nodes.append({"title": movie, "label": "movie"})
        target = i
        i += 1
        for name in actors:
            actor = {"title": name, "label": "actor"}
            try:
                source = nodes.index(actor)
            except ValueError:
                nodes.append(actor)
                source = i
                i += 1
            rels.append({"source": source, "target": target})
    print({"nodes": nodes, "links": rels})
    return {"nodes": nodes, "links": rels}


@get("/search")
def get_search():
    try:
        # q = request.query["q"]
        # bottle框架下前端基于encodeURIComponent参数中文乱码解决
        params = dict(request.headers)
        args = request.query.decode("utf-8")
        for i in args:
            params[i] = args[i]
        q = args["q"]
    except KeyError:
        return []
    else:
        results = graph.run("MATCH (movie:`电影表`) "
                            "WHERE movie.name =~ $name "
                            "RETURN movie", {"name": "(?i).*" + q + ".*"})
        result_df = pd.DataFrame(results)
        result_json_list = [{"movie": row[0]} for index, row in result_df.iterrows()]
        print(json.dumps(result_json_list))
        response.content_type = "application/json"
        return json.dumps(result_json_list)


@get("/movie/<name>")
def get_movie_info(name):
    results = graph.run("MATCH (movie:`电影表` {name: $name}) "
                        "OPTIONAL MATCH (movie)<-[ar]-(a:`演员表`) "
                        "OPTIONAL MATCH (movie)<-[dr]-(d:`导演表`) "
                        "RETURN movie.name as name, d.director as director, collect(a.actor) as actors, movie.image as image "
                        "LIMIT 1;", {"name": name})
    result_df = pd.DataFrame(results)
    for index, row in result_df.iterrows():
        # {'name': '霸王别姬', 'directors': '陈凯歌', 'actors': '张丰毅,张国荣'}
        # print({"name": row[0], "directors": row[1], "actors": ','.join(row[2])})
        return {"name": row[0], "directors": row[1], "actors": ','.join(row[2]), "image": row[3]}


if __name__ == '__main__':
    # 访问http://127.0.0.1:8081
    run(port=8081)

    # get_search()
    # get_movie_info("霸王别姬")
    # get_graph()

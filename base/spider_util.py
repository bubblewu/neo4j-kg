#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : spider_util.py
# @Author: wu gang
# @Date  : 2019-12-05
# @Desc  : 爬虫工具
# @Contact: 752820344@qq.com

import random
import time
from urllib import request

import numpy as np
import requests
from bs4 import BeautifulSoup

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"]

headers = {
    "User-Agent": random.choice(USER_AGENTS),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
    "Cache-Control": "no-cache",
    # "Cookie": ""
}


def get_ip_list():
    """
    获取动态代理IP（只获取了该网页的部分）
    :return: 代理IP
    """
    print("正在获取代理列表...")
    url = 'http://www.xicidaili.com/nn/'
    html = requests.get(url=url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    ips = soup.find(id='ip_list').find_all('tr')
    ip_list = list()
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    print("代理列表抓取成功, count: %d" % len(ip_list))
    return ip_list


ip_list = get_ip_list()


def get_random_ip(ip_list):
    # print("正在设置随机代理...")
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    print("代理设置成功：%s" % proxies)
    return proxies


def download(url, use_proxy=True):
    print("start download: %s" % url)
    time.sleep(np.random.rand() * 5)
    if use_proxy:
        proxy_handler = request.ProxyHandler(get_random_ip(ip_list))
        opener = request.build_opener(proxy_handler)
        req = request.Request(url, headers=headers)
        html = opener.open(req).read()
    else:
        req = request.Request(url, headers=headers)
        html = request.urlopen(req).read()
    html = str(html, encoding="utf-8")
    return html


def download_requests(url, use_proxy=True):
    print("start download: %s" % url)
    time.sleep(np.random.rand() * 5)
    if use_proxy:
        response = requests.get(url, headers=headers, proxies=get_random_ip(ip_list))
        response.encoding = 'utf-8'
        return response.text
    else:
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        return response.text

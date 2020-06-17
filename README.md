[toc]
# KG：基于Neo4j的知识图谱和问答案例

## Movie模块： 基于Neo4j的电影数据可视化
博客参考：[基于Neo4j的电影数据可视化](https://bubblewu.github.io/ckbarwdyc0000z5yd8tl0cjqn/)

本文主要内容为：
- 基于requests + BeautifulSoup抓取时光网电影数据；
- 基于电影数据构建电影和关系实体信息；
- 数据导入neo4j进行存储分析；
- 基于Bottle框架的对neo4j数据进行查询可视化展示。

效果展示：
![效果展示](https://cdn.jsdelivr.net/gh/bubblewu/cdn/images/neo4j/web-demo.png)

## Article模块：
### hlm 基于红楼梦的关系可视化和简单问答系统
主要内容：
- 基于《红楼梦》数据，构造人物实体和人物之间的关系实体；
- 利用网络爬虫从百科上抓取人物信息和图片；
- 将数据写入Neo4j图数据库；
- 前端基于Flask框架，后端封装API接口对neo4j进行查询、问答分析、和结果可视化；

效果展示：
![效果展示](https://cdn.jsdelivr.net/gh/bubblewu/cdn/images/other/hlm-search.png)

## Base模块：基础包
- spider_util：爬虫基础工具封装

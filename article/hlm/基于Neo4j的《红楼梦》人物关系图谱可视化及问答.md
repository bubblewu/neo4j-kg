
# 基于Neo4j的《红楼梦》人物关系图谱可视化及问答

本内容参考：
- [基于知识图谱的《红楼梦》人物关系可视化及问答系统](https://github.com/chizhu/KGQA_HLM)

## 主要内容：
- 基于《红楼梦》数据，构造人物实体和人物之间的关系实体；
- 利用网络爬虫从百科上抓取人物信息和图片；
- 将数据写入Neo4j图数据库；
- 前端基于Flask框架，后端封装API接口对neo4j进行查询、问答分析、和结果可视化；

## 效果展示：
- 登录界面：

![登录界面](https://cdn.jsdelivr.net/gh/bubblewu/cdn/images/other/hlm-homepage.png)

- 人物关系检索可视化：

![人物关系检索可视化](https://cdn.jsdelivr.net/gh/bubblewu/cdn/images/other/hlm-search.png)

- 人物关系全貌：

![人物关系全貌](https://cdn.jsdelivr.net/gh/bubblewu/cdn/images/other/hlm-all.png)

- 人物关系简单问答：

![人物关系简单问答](https://cdn.jsdelivr.net/gh/bubblewu/cdn/images/other/hlm-qa.png)

# 基于Neo4j的电影知识图谱构建

## mtime 时光网Top100电影
参考：
### 数据准备
主要分为两部分数据：实体数据和关系数据；

直接执行mtime_main函数，可以得到数据：
- 电影信息、导演信息、演员信息数据；
- 电影和导演关系、电影和演员关系、导演和演员关系数据。

### neo4j
#### 查看是否关闭服务
./neo4j status
#### 如果未关闭，关闭服务
./neo4j stop
#### 命令导入相关数据：
参考脚本：data/mtime/import_mtime.sh

#### 查看db
cd /Users/wugang/env/neo4j/data/databases/mtime_movie.db

#### 打开配置文件
vim conf/neo4j.conf
```
dbms.active_database=mtime_movie.db
```

#### 打开服务
./neo4j start

#### 可视化服务
执行mtime/mtime_graph_show.py。基于Bottle框架的Web服务。



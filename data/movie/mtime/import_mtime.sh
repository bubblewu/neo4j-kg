#!/bin/sh
# 脚本来执行将csv文件（节点和关系）导入neo4j
# 注意：必须停止neo4j；只能生成新的数据库，而不能在已存在的数据库中插入数据。

db_name=MovieMTime.db
neo4j_path=/Users/wugang/env/neo4j-community-4.0.4
base_path=/Users/wugang/code/python/neo4j-kg/data/mtime

import() {
  cd ${neo4j_path}
  ./bin/neo4j stop
  rm -rf /Users/wugang/env/neo4j-community-4.0.4/data/databases/${db_name}
  ./bin/neo4j-admin import --verbose \
                        --database ${db_name} \
                        --id-type STRING \
                        --input-encoding=UTF-8 \
                        --ignore-extra-columns=false \
                        --trim-strings=true \
                        --delimiter=, \
                        --array-delimiter=';' \
                        --processors=4 \
                        --nodes ${base_path}/mtime_movie_entity.csv \
                        --nodes ${base_path}/mtime_actor_entity.csv \
                        --nodes ${base_path}/mtime_director_entity.csv \
                        --relationships ${base_path}/mtime_director_actor_relationship.csv \
                        --relationships ${base_path}/mtime_movie_actor_relationship.csv  \
                        --relationships ${base_path}/mtime_movie_director_relationship.csv
  # 需要修改neo4j.conf配置文件中的默认db才能展示新建的db，否则还是默认的。（只能指定一个db）
#  ./bin/neo4j start
#  ./bin/neo4j stop
}

import


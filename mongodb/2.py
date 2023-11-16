"""
聚合函数-------------------------·-----------------------------
分组：$sum---求和  age---字段名，注意前面加$  gender---字段名，注意前面加$  count:{$sum:1}----------查询总和
db.my.aggregate({$group:{'_id':'$gender',counter:{$sum:'$age'},count:{$sum:1}}})

$project：-----------类似映射，对输出结果进行修改
db.my.aggregate({$group:{'_id':'$gender','avg_age':{$avg:'$age'},'count':{$sum:1}}},{$project:{'_id':0,'数量':'$count','平均年龄':'$avg_age'}})

$match 过滤文档----注意管道操作可以将结果传递
db.my.aggregate({$match:{'age':{$gte:30}}})

$sort排序：
db.my.aggregate({$sort:{state:1,age:-1}})

$limit分页：
db.my.aggregate({$limit:2})

索引----------------------------------------------------------

建立索引：--以id
db.my.ensureIndex({id:1})

查看索引
db.my.getIndexes()

建立唯一索引并去重：
db.my.ensureIndex({id:1},{'unique':true,'dropDups':true})
"""

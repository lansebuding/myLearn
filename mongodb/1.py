"""
启动指令
mongod -f ../conf/mongod.conf

连接：
mongo

创建数据库：
use [name]

查看所有数据库：(注意新建的数据库必须要有数据才会展示)
show dbs

查看当前使用数据库：
db

删除持久化数据库：
db.dropDatabase()
--------------------------------------------------
集合操作：

创建集合(显示)：
db.createCollection([name])

查看当前库中的集合(表):
show tables

删除指定集合
db.[name].drop()

隐式创建集合并插入文档：（注：my是集合名字，隐式创建）-----插入一条数据
db.my.insert({"id":"001","name":"YJW","age":NumberInt(25),"state":null})

查看插入的数据：
db.my.find()

查看插入的数据并格式化：
db.my.find().pretty()

并集查询：
db.my.find({$or:[{'state':1},{'age':18}]}).pretty()

自定义查询：
db.my.find({$where:function(){return !this.state}})

去重：
db.my.distinct('name')

根据条件去重：
db.my.distinct('name',{age:{$gt:20}})

插入多条数据：
db.my.insertMany([{"id":"002","name":"YJW2","age":NumberInt(26),"state":null},{"id":"003","name":"YJW3","age":NumberInt(27),"state":null}])

查询指定id数据：
db.my.find({"id":"002"})

查询指定id数据，只显示name属性：
db.my.find({"id":"002"},{"name":1})

查询指定id数据，多条只查一条：-------------查询时可以通过正则查询
db.my.findOne({"id":"002"})

可以使用try...catch...来插入：
try{db.my.insert({"id":"004","name":"YJW4","age":NumberInt(28),"state":null})}catch(e){print(e)}

更新数据：-----$set不加会覆盖
db.my.update({'name':'YJW'},{$set:{'age':NumberInt(1000)}})

批量更新数据：-----$set不加会覆盖
db.my.update({'name':'YJW'},{$set:{'age':NumberInt(1000)}},{multi:true})

数据递增：
db.my.update({'name':'YJW'},{$inc:{'age':NumberInt(1000)}})

删除数据（文档）：
db.my.remove({'name':'YJW'})

删除全部数据（文档）：
db.my.remove({})

获取文档数量：
db.my.count()

查询前两条数据：
db.my.find().limit(2)

跳过前两条数据查询第三条数据：
db.my.find().skip(2)

对数据进行排序查询：1---升序  -1------降序
db.my.find().sort({'age':1})

运算查询：---------1.$gt > 2.$lt < 3.$gte >= 4.$lte <= 5.$ne !=
包含查询：---------1.$in ['100','200'] 查询在数组内的  2.$nin ['100','200'] 查询不在数组内的
--------------------------------------------------

"""
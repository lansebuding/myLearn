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

插入多条数据：
db.my.insertMany([{"id":"002","name":"YJW2","age":NumberInt(26),"state":null},{"id":"003","name":"YJW3","age":NumberInt(27),"state":null}])

查询指定id数据：
db.my.find({"id":"002"})

查询指定id数据，只显示name属性：
db.my.find({"id":"002"},{"name":1})

查询指定id数据，多条只查一条：
db.my.findOne({"id":"002"})

可以使用try...catch...来插入：
try{db.my.insert({"id":"004","name":"YJW4","age":NumberInt(28),"state":null})}catch(e){print(e)}
--------------------------------------------------

"""
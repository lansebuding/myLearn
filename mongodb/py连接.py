import pymongo,time,datetime

client = pymongo.MongoClient(host='127.0.0.1',port=27017)
db = client['py_test']
collection = db['my']
def my_insert():
    my_dic={
        'name':'YJW3',
        'age':27,
        'likeNum':None,
        'createTime':int(time.time())
    }
    result = collection.insert_one(my_dic)
    print(result)

def my_find():
    result = collection.find()
    # result = collection.find().sort('age',1).skip(2).limit(5)
    # result = collection.find({'age':{'$lt':26}})
    # result = collection.find({'name':{'$regex':'3'}})
    for i in result:
        print(i)
        print(type(i))
    print(f'总数为：{collection.count_documents({})}')
    # print(type(result))

def my_update():
    result = collection.update_one({'name':'YJW2'},{'$inc':{'age':5}})
    # result = collection.update_one({'name':'YJW3'},{'$set':{'name':'YJW4'}})
    # result = collection.update_many({'name':'YJW2'},{'$inc':{'age':-25}})
    print(result)

def my_delete():
    result = collection.delete_many({'name':'YJW2'})
    print(result)

# my_insert()
# my_update()
# my_delete()
my_find()
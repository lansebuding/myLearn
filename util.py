import pymysql

# 获取连接对象
# db='cast'-----你连接的数据库名称
def get_connection():
    conn = pymysql.Connection(host='localhost',port=3306,user='root',db='cast',password='a1846770113')
    cursor = conn.cursor()

    return conn,cursor

# 关闭连接对象
def close_connection(conn,cursor):
    if(conn):
        conn.close()
    if(cursor):
        cursor.close()


def getValues(sql:str):
    conn,cursor = get_connection()
    cursor.execute(sql)
    res = cursor.fetchall()
    conn.commit()
    close_connection(conn,cursor)

    return res
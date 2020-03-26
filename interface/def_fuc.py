#-*- encoding:utf-8 -*-
import pymysql as mysqlc
import cx_Oracle
import pymssql

# 生成顺序ip地址
def get_ip(number, start_ip):
    starts = start_ip.split('.')
    A = int(starts[0])
    B = int(starts[1])
    C = int(starts[2])
    D = int(starts[3])
    for A in range(A, 256):
        for B in range(B, 256):
            for C in range(C,256):
                for D in range(D, 256):
                    ip = "%d.%d.%d.%d" % (A, B, C, D)
                    yield ip
                    if number > 1:
                        number -= 1
                    else:
                        return
                D=0
            C=0
        B=0


def get_db_conn(dbtype, dbinfo):  # conn = get_db_conn(dbtype, dbinfo); conn.close()

    try:
        if dbtype == "oracle":
            conn = cx_Oracle.connect('{}/{}@{}:{}/{}'.format(dbinfo["user"],dbinfo["passwd"],dbinfo["host"],
                                                             dbinfo["port"],dbinfo["db"]))
        elif dbtype == "mysql":
            conn = mysqlc.connect(host=dbinfo["host"], user=dbinfo["user"], passwd=dbinfo["passwd"],
                                  port=dbinfo["port"], charset='utf8')
        elif dbtype == "mssql":
            conn = pymssql.connect(server=dbinfo["host"], user=dbinfo["user"], password=dbinfo["passwd"],
                                  port=dbinfo["port"], charset='utf8',autocommit=True)
        else:
            conn = "nothing"
        return conn
    except Exception as e:
        print('创建数据库连接失败')
        print(e)
        return False

##执行select语句
def select_table(conn,select_sql):
    cursor=conn.cursor()
    cursor.execute(select_sql)
    data=cursor.fetchall()
    return data

def insert_table(conn, table_name, values, dbtype):
    cursor = conn.cursor()
    # _values = []
    # for v in values:
    #     _v = "'" + v + "'"
    #     _values.append(_v)
    _values=[repr(i) for i in values]
    print(_values)
    if dbtype == "mysql" or dbtype == "mssql":
        sql = 'insert into ' + table_name + ' values(' + ','.join(_values) + ')'
    elif dbtype == "oracle":
        sql = 'insert into ' + table_name + ' values(' + ','.join(_values) + ')'
    else:
        sql = '空'
        print('insert_sql语句为:{}'.format(sql))
        exit()
    print('插入的语句为:{}'.format(sql))
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        return False

def drop_database(conn, database_name, dbtype):
    cursor = conn.cursor()
    if dbtype == "mysql":
        sql = 'drop database if exists ' + database_name
    elif dbtype == "mssql":
        sql = 'ALTER DATABASE [{}] SET  SINGLE_USER WITH ROLLBACK IMMEDIATE;drop database {};'.format(database_name,database_name)
    else:
        sql = '空'
        print('drop sql语句为:{}'.format(sql))
        exit()
    print('删除数据库语句为：{}'.format(sql))
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        return False

def create_database(conn, database_name, dbtype):
    cursor = conn.cursor()
    if dbtype == "mysql":
        sql = 'create database ' + database_name
    elif dbtype == "mssql":
        sql = 'create database {};'.format(database_name)
    else:
        sql = '空'
        print('create databse sql语句为:{}'.format(sql))
        exit()
    print('create databse sql语句为:{}'.format(sql))
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        return False

def drop_table(conn, table_name, dbtype):
    cursor = conn.cursor()
    if dbtype == "mysql":
        sql = 'drop table if exists ' + table_name
    elif dbtype == "oracle" or dbtype == "mssql":
        sql = 'drop table ' + table_name
    else:
        sql = '空'
        print('drop table sql语句为:{}'.format(sql))
        exit()
    print('drop table sql语句为:{}'.format(sql))
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        return False

def create_table(conn, table_name, table_info, dbtype):
    cursor = conn.cursor()
    ziduan = ''
    for key in table_info.keys():
        if len(ziduan) > 0:
            ziduan += ','
        ziduan += key + ' ' + table_info[key]
    if dbtype == "mysql" or dbtype == "mssql":
        sql = 'create table ' + table_name + '(' + ziduan + ')'
    elif dbtype == "oracle":
        sql = 'create table ' + table_name + '(' + ziduan + ')'
    else:
        sql = '空'
        print('create table sql语句为:{}'.format(sql))
        exit()
    print('建表语句为:{}'.format(sql))
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        return False

def use_database(conn, database_name, dbtype):
    cursor = conn.cursor()
    if dbtype == "mysql":
        sql = 'use ' + database_name
    elif dbtype == "mssql":
        sql = "use {};".format(database_name)
    else:
        sql = '空'
        print('use sql语句为:{}'.format(sql))
        exit()
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        return False

def close_coo(conn):
    try:
        conn.close
    except Exception as e:
        print(e)
        return False


if __name__=="__main__":
    for ip in get_ip(10,'10.10.10.253'):
        print(ip)
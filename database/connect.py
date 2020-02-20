# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 0021 下午 14:16
# @Author  : zgh
# @Site    :
# @File    : connect.py
# @Software: PyCharm
import pymysql as mysqlc
import cx_Oracle




def get_db_conn(dbtype, dbinfo):  # conn = get_db_conn(dbtype, dbinfo); conn.close()

    try:
        if dbtype == "oracle":
            conn = cx_Oracle.connect('{}/{}@{}:{}/{}'.format(dbinfo["user"],dbinfo["passwd"],dbinfo["host"],
                                                             dbinfo["port"],dbinfo["db"]))
        elif dbtype == "mysql":
            conn = mysqlc.connect(host=dbinfo["host"], user=dbinfo["user"], passwd=dbinfo["passwd"],
                                  port=dbinfo["port"], charset='utf8')
        else:
            conn = "nothing"
        return conn
    except Exception as e:
        print('创建数据库连接失败')
        print(e)
        return False


def insert_table(conn, table_name, values, dbtype):
    cursor = conn.cursor()
    # _values = []
    # for v in values:
    #     _v = "'" + v + "'"
    #     _values.append(_v)
    _values=[repr(i) for i in values]
    print(_values)
    if dbtype == "mysql":
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
    elif dbtype == "oracle":
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
    if dbtype == "mysql":
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

import connect
import genertor_data
import os
import time
import profile

os.environ['NLS_LANG'] = 'Simplified Chinese_CHINA.ZHS16GBK'



dbinfo_oracle = {"host": "192.168.0.17",
          "port": 1521,
          "db": "orcl",
          "user": "thw",
          "passwd": "thw",
          "table_name": "test"
          }

dbinfo_mysql = {"host": "cdb-9b3dm1pm.cd.tencentcdb.com",
          "port": 10070,
          "db": "thw1",
          "user": "root",
          "passwd": "schina1234",
          "table_name": "test"
          }

table_info_mysql = {'id': 'varchar(128)',
              'name': 'varchar(128)',
              'sex': 'varchar(4)',
              'birth':'varchar(20)',
              'address': 'varchar(128)',
              'phone': 'varchar(20)',
              'cardid': 'varchar(20)'
              }
table_info_oracle = {'id': 'varchar2(128)',
              'name': 'varchar2(128)',
              'sex': 'varchar2(4)',
              'birth':'varchar2(20)',
              'address': 'varchar2(128)',
              'phone': 'varchar2(20)',
              'cardid': 'varchar2(20)'
              }



count = 1001  ##循环插入数据次数

def create_mysql_db():
    table_info = table_info_mysql
    dbtype = "mysql"
    dbinfo = dbinfo_mysql

    starttime=time.time()
    # 创建数据库连接
    conn = connect.get_db_conn(dbtype, dbinfo)
    # 删除数据库
    connect.drop_database(conn, dbinfo['db'],dbtype)
    # 创建数据库
    connect.create_database(conn, dbinfo['db'],dbtype)
    # 创建表
    connect.use_database(conn, dbinfo['db'],dbtype)
    connect.create_table(conn, dbinfo['table_name'], table_info,dbtype)
    # 创建数据
    _genertor_data = genertor_data.genertor_data(count,len(table_info))
    for c in range(count):
        table_values = next(_genertor_data)
        print('创建的数据为:{}'.format(table_values))
        connect.insert_table(conn, dbinfo['table_name'], table_values,dbtype)
    # 关闭连接
    connect.close_coo(conn)
    endtime = time.time()
    print(endtime - starttime)


def create_oracle_db():
    table_info = table_info_oracle
    dbtype = "oracle"
    dbinfo = dbinfo_oracle

    starttime=time.time()
    # 创建数据库连接
    conn = connect.get_db_conn(dbtype, dbinfo)
    # 删除表
    connect.drop_table(conn,dbinfo['table_name'],dbtype)
    # 创建表
    connect.create_table(conn, dbinfo['table_name'], table_info, dbtype)
    # 创建数据
    _genertor_data = genertor_data.genertor_data(count,len(table_info))
    for c in range(count):
        table_values = next(_genertor_data)
        print('创建的数据为:{}'.format(table_values))
        connect.insert_table(conn, dbinfo['table_name'], table_values,dbtype)
    # 关闭连接
    connect.close_coo(conn)
    endtime=time.time()
    print(endtime-starttime)



if __name__ == "__main__":
    create_mysql_db()
    # profile.run("create_mysql_db()")
    # create_oracle_db()

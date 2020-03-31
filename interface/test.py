# -*- encoding:UTF-8 -*-
import interface
import time
import sys
import os

ret_debug={"state":"INFO","message":""}

# 构建dbinfo
dbinfo = {
    "host": "192.168.5.37",
    "user": "root",
    "passwd": "schina1234",
    "port": 9207
}

url = 'https://192.168.5.11'
# 构建pars
pars = {
    "instId": '51',  ##实例id
    "username": 'root',  ##实例用户名
    "dbType": 'SQLSERVER',  ##实例数据库类型 (SQLSERVER , MySQL)
    "password": 'Schina1234',  ##实例密码（密文）
    "databaseRole": '0',  ##实例用户角色（Oracle选填，其它库忽略）
    "clientIp": '192.168.202.102',  ##限制ip地址/ip段
    "clientIpExcept": '',  ##例外ip
    "allowType": '0',  ##限制类型 0 -禁止   1 -允许
    "schemaName": '',  ##mysql数据库名
    "id": '3',  ##ip权控信息id
    "dbUserId": '270',  ##数据库用户id
    "tableArray": {"tableId": 3572672792},
    "permissionStr": "select,update,insert",
    "defVal": "",
    "databaseId": "14",
    "tableId": "1003",
    "protectionColumnList": {"columnName": "id", "defaultValues": "0", "isDefNull": 0, "remark": "null",
                             "colsTypeNum": 3},
    "tdeIp": "192.168.130.11",
    "tdePort": 10001,
    "instancename": '',  ##实例名，sqlserver数据库填写表示为动态端口模式
    "logbackuppath": 'c:\\bak',
    "tdename": '',
    "ifpwd": 1,
    "mppLogin": 2
}
# 获取加密后的密码
passwd = interface.encryptPwd(url, pars["password"])
pars["password"] = passwd

# # 添加实例
# count = 1
# tdeport = 10001
# while count <= 1:
#     pars["tdename"] = 'mssql' + str(int(time.time()))
#     pars["tdePort"] = tdeport
#     interface.log_debug("开始添加第{}个实例".format(count),sys._getframe().f_lineno,__file__)
#     ret = interface.addTde(url, pars)
#     count += 1
#     tdeport += 1
#     time.sleep(1)

# 删除实例
for i in range(1,998):
    pars["id"] = i
    interface.log_debug("开始删除第{}个实例".format(i),sys._getframe().f_lineno,__file__)
    ret = interface.deleteTde(url, pars)
    time.sleep(1)

# 添加ip权控
# count = 0
# for ip in def_fuc.get_ip(9000,'11.10.11.0'):
#     pars["clientIp"] = ip
#     interface.setClientPrivilege(url, pars)
#     count += 1
#     print('完成第{}个：{}'.format(count,ip))

# 删除ip权控
# for id in range(10,580):
#     pars["id"]=id
#     interface.delClientPrivilege(url,pars)

# 删除用户权控
# interface.deleteTableUserPerInfo(url, pars)

# 添加用户权控
# conn=def_fuc.get_db_conn('mysql',dbinfo)
# data=def_fuc.select_table(conn,'SELECT hash_uuid FROM dbscloud.sqlserver_obj_id where dbid=9 limit 50;')
# tableid=[i for i,*x in data]
# print(tableid)
# for _tableid in tableid:
#     pars["tableArray"]["tableId"]=_tableid
#     for i in range(163,363):
#         pars["dbUserId"]=i
#         print('tableid:{},dbuserid:{}'.format(_tableid,i))
#         interface.saveTableUserPerInfo(url, pars)


# # 连接数据库
# conn=def_fuc.get_db_conn('mysql',dbinfo)
# data=def_fuc.select_table(conn,'SELECT distinct userid FROM odcschema.userprivilege;')
# userid=[i for i,*x in data]
# data=def_fuc.select_table(conn,'SELECT distinct id FROM odcschema.cyphercolumn;')
# tableid=[i for i,*x in data]
# # 删除用户权限
# for tableid_ in tableid:
#     pars["tableArray"]["tableId"]=tableid_
#     for userid_ in userid:
#         pars["dbUserId"]=userid_
#         interface.deleteTableUserPerInfo(url, pars)


# # mysql设置保护列
# for i in range(1003,10993):
#     pars["tableId"]=i
#     ret=interface.setingDefaultValue(url,pars)
#     print("tableid:{},result:{}".format(i,ret))

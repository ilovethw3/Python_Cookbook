#-*- encoding:utf-8 -*-

import os, sys, json, time, random, subprocess
import pymysql, configparser,shutil
from urllib import parse
from urllib import request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def post_data(url,body_value):
    result={'state': '', 'code': '', 'message': '', 'content': ''}
    post_value = request.Request(url=url, data=body_value)
    try:
        resdata = request.urlopen(post_value)
        res = resdata.read().decode("utf-8")
        dict = json.loads(s=res)
        if "state" not in dict:
            dict["state"] = False
        result = dict
    except Exception as e:
        result['code']='-9999'
        result['content']=e

    return  result



def encryptPwd(url, passwd):
    url = "%s/v3/oracle/common/encryptPassword.action" % url
    data = {"password": passwd}
    body_value = parse.urlencode(data).encode("utf-8")
    # 访问url发送post参数
    enc_passwd = post_data(url, body_value)['content']
    return enc_passwd

def addTde(url,pars):
    url = "%s/tde/addTde.action" % url
    instanceinfo = {"tdeName": pars["tdeName"],
                    "dbType": 'SQLSERVER',
                    "tdeIp": pars["tdeIp"],  # tde实例的ip
                    "tdePort": int(pars["tdePort"]),  # tde port
                    "instanceName": '',
                    "databaseRole": 0,
                    "ifpwd": 1,
                    "username": pars["username"],  # tde 实例的用户名
                    "password": pars["password"],  # tde 实例的密码
                    "backuplogPath": pars["logBackupPath"],
                    "mppLogin": '0',
                    "subNodeId": '',
                    "subNodeName": '',
                    "subNodeIp": '',
                    "subNodePort": ''
                    }

    body_value = parse.urlencode(instanceinfo).encode("utf-8")
    ret = post_data(url, body_value)
    return ret

def setClientPrivilege(url,pars):
    url = "%s/v3/clientPrivilege/setClientPrivilege.action" % url
    instanceinfo = {"instId": pars["instId"],
                    "username": pars["username"],
                    "dbType": pars["dbType"],
                    "password": pars["password"],
                    "databaseRole": pars["databaseRole"],
                    "clientIp": pars["clientIp"],
                    "clientIpExcept": pars["clientIpExcept"],
                    "allowType": pars["allowType"],
                    "schemaName": pars["schemaName"]
                    }
    body_value = parse.urlencode(instanceinfo).encode("utf-8")
    ret = post_data(url, body_value)
    return ret

def delClientPrivilege(url,pars):
    url = "%s/v3/clientPrivilege/deleteClientIp.action" % url
    instanceinfo = {"instId": pars["instId"],
                    "username": pars["username"],
                    "dbType": pars["dbType"],
                    "password": pars["password"],
                    "databaseRole": pars["databaseRole"],
                    "id": pars["id"]
                    }
    body_value = parse.urlencode(instanceinfo).encode("utf-8")
    ret = post_data(url, body_value)
    return ret


def deleteTableUserPerInfo(url,pars):
    url = "%s/v3/permission/deleteTableUserPerInfo.action" % url
    instanceinfo = {"instId": pars["instId"],
                    "dbType": pars["dbType"],
                    "dbUserId":pars["dbUserId"],
                    "username": pars["username"],
                    "password": pars["password"],
                    "databaseRole": pars["databaseRole"],
                    "tableArray": [pars["tableArray"]]
                    }
    userTableRelationDetailObj = {"params": instanceinfo}
    body_value = parse.urlencode(userTableRelationDetailObj).encode("utf-8")
    ret = post_data(url, body_value)
    return ret

def saveTableUserPerInfo(url,pars):
    url = "%s/v3/permission/saveTableUserPerInfo.action" % url
    instanceinfo = {"instId": pars["instId"],
                    "dbType": pars["dbType"],
                    "dbUserId":pars["dbUserId"],
                    "username": pars["username"],
                    "password": pars["password"],
                    "databaseRole": pars["databaseRole"],
                    "permissionStr":pars["permissionStr"],          ##权限类型（组合权限时，使用“,” 分割）select,update,insert,delete,readOnly,readAndWrite
                    "defVal":pars["defVal"],                        ##缺省值开关 1-开启  0-关闭
                    "tableArray": [pars["tableArray"]]              ##权控表数组
                    }
    userTableRelationDetailObj = {"params": instanceinfo}
    body_value = parse.urlencode(userTableRelationDetailObj).encode("utf-8")
    ret = post_data(url, body_value)
    return ret

def setingDefaultValue(url,pars):
    url = "%s/v3/defaultValue/setingDefaultValue.action" % url
    instanceinfo = {"instId": pars["instId"],
                    "dbType": pars["dbType"],
                    "username": pars["username"],
                    "password": pars["password"],
                    "databaseRole": pars["databaseRole"],
                    "databaseId": pars["databaseId"],
                    "tableId": pars["tableId"],
                    "protectionColumnList": [pars["protectionColumnList"]]
                    }
    protectionColumns = {"protectionColumns": instanceinfo}
    body_value = parse.urlencode(protectionColumns).encode("utf-8")
    ret = post_data(url, body_value)
    return ret
if __name__=="__main__":
    pass

#coding:utf-8
from lib import task
websql = 'select address,port from blog.scan_scan_port where service like "http%" or service ="" or service="unknown" or port="80"'
websql_1 = "" #标准端口web服务
websql_2 = "" #非标准端口web服务
class shiro(task):
    taskname = "shiro-deserial-rce.py"
    sql = websql
    def __init__(self):
        task.__init__(self,self.taskname,self.sql)
class cors(task):
    config = {}
    config["scriptname"] = "cors-misconfigure.py"
    config["sql"] = websql
    config["isGetDomain"] = True
    config["isGevent"] = False
    def __init__(self):
        task.__init__(self, **(self.config))
if __name__ == "__main__":
    s = eval("cors()")
    s.scan()

#coding:utf-8

mysql_config_dev = "mysql+pymysql://root:@127.0.0.1:3306/blog"
mysql_config_prod = "mysql+pymysql://root:@127.0.0.1:3306/blog"

mysql_config = mysql_config_dev
#redis_server = "redis.nvmkzhtjhizl.scs.bj.baidubce.com"
redis_config = {"host":"127.0.0.1","port":6379,"password":""}

SCANDIR = "SCANLOG"
BINDIR = "/Users/dongguangli/work/github/POC-T/"
BIN = "/Users/dongguangli/work/github/POC-T/POC-T.py"
RUNLOG = "/tmp/poclog"


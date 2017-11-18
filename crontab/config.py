#coding:utf-8
import MySQLdb,random,time,os
mysql_server = "127.0.0.1"
mysql_user = "root"
mysql_pass = ""
mysql_port = 3306

SCANDIR = "SCANLOG"
BINDIR = "/Users/dongguangli/work/github/POC-T/"
BIN = "/Users/dongguangli/work/github/POC-T/POC-T.py"
RUNLOG = "/tmp/poclog"

#从数据库中返回记录
#去重,随机
def query(sql="select brother from blog.scan_scan_srcbrother"):
    conn = MySQLdb.connect(mysql_server, user=mysql_user, passwd=mysql_pass, port=mysql_port)
    cur = conn.cursor()
    cur.execute(sql)
    res = cur.fetchall()
    cur.close()
    res = list(set(res))
    random.shuffle(res)
    return res

class task:
    def __init__(self,taskname="",sql=""):
        self.taskname = taskname
        self.sql = sql
        self.logdir = RUNLOG + "/" + time.strftime('%Y%m%d%H',time.localtime(time.time())) + "/" + self.taskname
        if not os.path.exists(self.logdir):
            os.makedirs(self.logdir)
        self.fpath = self.logdir + "/" + "targets.txt"
        self.export2txt()
    def export2txt(self):
        res = query(self.sql)
        with open(self.fpath,"w") as f:
            for i in res:
                f.write("{ip}:{port}\n".format(ip=i[0],port=i[1]))
    def scan(self):
        os.chdir(BINDIR)
        os.system("python {0} -iF {1} -s script/{2}".format(BIN,self.fpath,self.taskname))
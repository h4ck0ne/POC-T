#coding:utf-8
import MySQLdb,random,time,os,redis,json
mysql_config = {"host":"127.0.0.1","user":"root","passwd":"","port":3306}
#redis_server = "redis.nvmkzhtjhizl.scs.bj.baidubce.com"
redis_config = {"host":"127.0.0.1","port":6379,"password":""}

SCANDIR = "SCANLOG"
BINDIR = "/Users/dongguangli/work/github/POC-T/"
BIN = "/Users/dongguangli/work/github/POC-T/POC-T.py"
RUNLOG = "/tmp/poclog"

#从数据库中返回记录
#去重,随机
def query(sql="select brother from blog.scan_scan_srcbrother"):
    conn = MySQLdb.connect(**mysql_config)
    cur = conn.cursor()
    cur.execute(sql)
    res = cur.fetchall()
    cur.close()
    res = list(set(res))
    random.shuffle(res)
    return res
"""
	根据ip 返回域名,使用redis做缓存
	针对nginx,apache多Host的情况 很常见,非常需要
	todo:也可以用来判断CDN,但是针对CDN的ip如何处置?
"""
def getdomainfromip(ip):
    key_prefix = "i2d"
    ret = [ip]
    redis_conn = redis.Redis(**redis_config)
    domains = redis_conn.get(key_prefix+ip)
    if domains:
        ret = json.loads(domains)
    else:
        res = query("select distinct(domain) from blog.scan_scan_domain where ip='{0}'".format(ip))
        for i in res:
            if i[0] == '' or i[0].startswith('IPc'):
                continue
            ret.insert(0,i[0])
        redis_conn.psetex(key_prefix+ip, 1000 * 61 * 60, json.dumps(ret))
    return ret

"""
    args
    taskname: 插件名
    processnum: 分割文件后的进程数
    threadnum: 线程/协程数
    isGevent: 是否使用协程
"""
class task:
    def __init__(self,taskname="",sql="",processnum=2,threadnum=50,isGevent=False):
        self.taskname = taskname
        self.sql = sql
        self.logdir = RUNLOG + "/" + time.strftime('%Y%m%d%H',time.localtime(time.time())) + "/" + self.taskname
        if not os.path.exists(self.logdir):
            os.makedirs(self.logdir)
        self.fpath = self.logdir + "/" + "targets.txt"
        self.processnum = processnum
        self.threadnum = threadnum
        self.isGevent = isGevent
        self.export2txt()
    def export2txt(self):
        res = query(self.sql)
        targetcount = 0
        with open(self.fpath,"w") as f:
            for i in res:
                for ip in getdomainfromip(i[0]):
                    f.write("{ip}:{port}\n".format(ip=ip, port=i[1]))
                    targetcount = targetcount + 1
        targetcount = targetcount + 1
        os.chdir(self.logdir)
        os.system("split -l {0} -a 2 {1} splittarget".format(targetcount/self.processnum,self.fpath))
    def scan(self):
        os.chdir(BINDIR)
        for i in os.listdir(self.logdir):
            if not i.startswith("splittarget"):
                continue
            if self.isGevent:
                os.system("python {0} -eG -iF {1} -s script/{2} -t {3} &".format(BIN,self.logdir+"/"+i,self.taskname,self.threadnum))
            else:
                os.system("python {0} -iF {1} -s script/{2} -t {3} &".format(BIN,self.logdir+"/"+i,self.taskname,self.threadnum))

#print getdomainfromip("140.205.230.49")
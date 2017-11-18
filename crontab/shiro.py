from config import task
class shiro(task):
    taskname = "shiro-deserial-rce.py"
    sql = "select address,port from blog.scan_scan_port where service like 'http%' or service ='' or service='unknown' or port='80'"
    def __init__(self):
        task.__init__(self,self.taskname,self.sql)
class cors(task):
    taskname = "cors-misconfigure.py"
    sql = "select address,port from blog.scan_scan_port where service like 'http%' or service ='' or service='unknown' or port='80'"
    def __init__(self):
        task.__init__(self, self.taskname, self.sql)
if __name__ == "__main__":
    s = eval("cors()")
    s.scan()

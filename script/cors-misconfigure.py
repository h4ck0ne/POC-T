# coding:utf-8
"""
	CORS滥用
"""
import requests

def poc(url):
    try:
		domain = url.split(":")[0]
		port = url.split(":")[1]
		return run(domain,port)
    except Exception:
        return url + ' [Error]'

def run(domain,port):
	for suffix in ["/"]:
		if str(port) == "443":
			url = "https://{0}:{1}".format(domain, port)
		else:
			url = "http://{0}:{1}".format(domain, port)
		url = url + suffix
		try:
			headers = {"Origin":url}
			r = requests.head(url,headers = headers)
			if "Access-Control-Allow-Origin" in r.headers.keys() and "Access-Control-Allow-Credentials" in r.headers.keys():
				return True
		except requests.RequestException:
			pass
		except Exception as e:
			pass
			#traceback.print_exc()
			#print(e, url)

def check(task):
	ip = task[0]
	port = str(task[1])
	if is_internal_ip(ip):
		return
	print("{0} Scanning: {1}".format(time.strftime("%d:%H:%M", time.localtime(time.time())), ip))
	for domain in getdomainfromip(ip):
		if domain == "" or domain.startswith("IPc"):
			continue
		run(domain,port)

"""
	检查结束后
"""
def clean():
	pass
"""
	测试
"""
def test(ip, port):
	check([ip, port])

def main():
	res = get_from_database(
		"select address,port from blog.scan_scan_port where service like 'http%' or service ='' or service='unknown' or port='80'")
	res = list(set(res))
	print("共检查{0}个IP".format(len(res)))
	random.shuffle(res)
	p = Pool(200)
	p.map(check, res)
if __name__ == "__main__":
	print("String...")
	#run("127.0.0.1","80")
	main()
	print("Finished...")
	clean()

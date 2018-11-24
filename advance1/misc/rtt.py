import time
import requests

def rtt(url):
	t1 = time.time()
	r = requests.get(url)
	t2 = time.time()
	tim = str(t2-t1)
	print ("time in sec : " + tim)

#url = "http://www.google.com"
url = "http://www.cricbuzz.com"
rtt(url)

import requests
import time
import sys
import random
from torrequest import TorRequest
from useragent import header

proxyPort=9050
ctrlPort=9051
referer= ["https://ask.com", "https://www.blogspot.com", "https://www.nasa.gov", "https://deepmind.com", "https://tokopedia.com", "https://bukalapak.com", "https://lazada.com", "https://alibaba.com", "https://www.dpr.go.id", "https://www.mpr.go.id"]

url = input("Url blog (ex: http://example.com) : ")
view = input("Number View : ")
view =int(view)
def run(i):
     #using torrequest
     #tr.resetidentity()
     response = tr.get(site, headers={"User-Agent": random.choice(header),"Referer":random.choice(referer)})
     print("View +", (i+1)-i)

if __name__ == '__main__':
	if len(sys.argv) > 3:
	   if sys.argv[1] and sys.argv[2]:proxyPort=sys.argv[1];ctrlPort=sys.argv[2]
	with TorRequest(proxy_port=proxyPort, ctrl_port=ctrlPort, password=None) as tr:
	    for i in range(view):run(i)
		

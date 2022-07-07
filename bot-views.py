import requests
import time
import sys
import random

from torrequest import TorRequest
from useragent import header

proxyPort=9050
ctrlPort=9051
referer= ["https://ask.com", "https://mobilelegends.com", "https://www.nasa.gov", "https://deepmind.com", "https://tokopedia.com", "https://bukalapak.com", "https://lazada.com", "https://alibaba.com", "https://www.dpr.go.id", "https://www.mpr.go.id"]
# site = input("ketikkan alamat blog (misal: http://link.com) : ")
jumlah = input("jumlah viewnya  : ")
jumlah =int(jumlah)
blogger= "https://pteridophytadev.blogspot.com/2022/05/cara-menghubungkan-2-vlan-berbeda.html"
def run(i):
     tr.reset_identity()
     response = tr.get(blogger, headers={"User-Agent": random.choice(header),"Referer":random.choice(referer) })
     print("View +", (i+1))

if __name__ == '__main__':
	if len(sys.argv) > 3:
	   if sys.argv[1] and sys.argv[2]:proxyPort=sys.argv[1];ctrlPort=sys.argv[2]
	with TorRequest(proxy_port=proxyPort, ctrl_port=ctrlPort, password=None) as tr:
	    for i in range(jumlah):run(i)
		
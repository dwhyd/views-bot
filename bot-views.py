import requests
import time
import sys
import random
from useragent import header

proxyPort=9050
ctrlPort=9051
referer= ["https://ask.com", "https://mobilelegends.com", "https://www.nasa.gov", "https://deepmind.com", "https://tokopedia.com", "https://bukalapak.com", "https://lazada.com", "https://alibaba.com", "https://www.dpr.go.id", "https://www.mpr.go.id"]
site = input("URL (ex: http://example.com) : ")
jumlah = input("Number View  : ")
jumlah =int(jumlah)
def run(i):
     requests.get(site, headers={"User-Agent": random.choice(header),"Referer":random.choice(referer) })
     print("View +", (i+1))

for i in range(jumlah):run(i)
		

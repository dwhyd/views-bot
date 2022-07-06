import requests
import time
import sys
from random import seed
from random import randint
from torrequest import TorRequest
from useragent import header

proxyPort=9050
ctrlPort=9051

site = input("ketikkan alamat blog (misal: http://link.com) : ")
jumlah = input("jumlah viewnya  : ")
jumlah =int(jumlah)
seed(1)
blogger= "https://pteridophytadev.blogspot.com/2022/05/cara-menghubungkan-2-vlan-berbeda.html"
def run(i):
     value = randint(0, 40)
     response = tr.get(site, headers={"User-Agent": header[value]})
     # print(response.text)  

   #   iplama = tr.get('http://ipecho.net/plain')
   #   print("Blog view added with",iplama.text)
   #   tr.reset_identity()
   #   newip =tr.get('http://ipecho.net/plain')
   #   print("New Ip Address", newip.text)
     print("View +", (i+1)-i)

if __name__ == '__main__':
	if len(sys.argv) > 3:
	   if sys.argv[1] and sys.argv[2]:proxyPort=sys.argv[1];ctrlPort=sys.argv[2]
	with TorRequest(proxy_port=proxyPort, ctrl_port=ctrlPort, password=None) as tr:
	    for i in range(jumlah):run(i)
		
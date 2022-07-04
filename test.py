import requests
import time
import sys
from torrequest import TorRequest

proxyPort=9050
ctrlPort=9051

headers = {
	# "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"
     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3819044589 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0"
}
header=["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3819044589 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v2141535957212055550 t6544303725462717120 ath5ee645e0 altpriv cvcv=2 smf=0", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v2023853916361174582 t1083003796742344377 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v8879454916927791572 t3226535056386821987 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3819053300 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v7237658846343994439 t6557865812607695948 ath5ee645e0 altpriv cvcv=2 smf=0" ]
angka =3
safelinku= "https://cararegistrasi.com/mjwEx4"
blogger= "https://pteridophytadev.blogspot.com/2022/05/cara-menghubungkan-2-vlan-berbeda.html"
def run(angka):
     response = tr.get(safelinku, headers={"User-Agent": header[angka]})
#     time.sleep(10)
     # print(response.text)  
     tr.reset_identity()
     ipnya = tr.get('http://ipecho.net/plain')
     print("Blog view added with")
     print(ipnya.text)

if __name__ == '__main__':
	if len(sys.argv) > 3:
	   if sys.argv[1] and sys.argv[2]:proxyPort=sys.argv[1];ctrlPort=sys.argv[2]
	with TorRequest(proxy_port=proxyPort, ctrl_port=ctrlPort, password=None) as tr:
	    for i in range(angka):run(angka)
		
#Proxy (Tor)

import socks # pip install pysocks
import requests

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, 'localhost', 9150)
socks.socket = socks.socksocket

def makeTorRequest(url):
  response = requests.get(url)
  return response

url = "https://www.google.com"
response = makeTorRequest(url)

print(response.headers)

import requests
import json

url = "http://www.baidu.com"
para ={}
header = {}
r = requests.get(url,params= para,headers = header)
print(r.text)
print(r.status_code)
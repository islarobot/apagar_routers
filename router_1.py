#apagar_router_principal

#192.168.0.1

import requests
from bs4 import BeautifulSoup

params ={'user':'admin'
,'password':'NZelgaSZoiXM+kix7UpMIg=='
,'userlevel':'-1'
,'refer':'/index.html'
,'failrefer':'/admin.shtml?fail'
,'login':'Login'}
 
url = 'http://192.168.0.1/cgi-bin/basicauth.cgi?index.html'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}
#response = requests.get(url,headers=headers)
response = requests.post(url,data=params)

url2 = 'http://192.168.0.1/index.html?count=0'

response = requests.get(url2,headers=headers)

html = response.content
print(response.content)






import requests
import urllib
from collections import OrderedDict
import json

url = 'http://ebulten.bddk.org.tr/HaftalikBulten/tr/Gosterim/VeriGetir'


headers = {
    'Host' : 'ebulten.bddk.org.tr' ,
    'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8' ,
    'Content-Length' : '77' ,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}



payload = OrderedDict([('kalem[]', ['0']), ('baslangic', '16/11/2018'), ('bitis', '16/11/2018') , ('taraf[]' , ['10001'])])
 

response = requests.get(url, headers=headers ,  data=payload)


bddk_result_json = response.json()

 

with open('haftalik_bulten_result.json', 'w') as outfile:  
    json.dump(bddk_result_json, outfile) 

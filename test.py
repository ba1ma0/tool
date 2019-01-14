'''此程序主要是测试一些功能函数是否有效'''
#-*- coding:utf-8 -*-
# Python 3.6.1
import hashlib,base64,string,os,sys,time,logging,string,re
from module import tools,argparse,random,printc,noAlphaPayload
#将base64编码格式转化为正常的字符类型
def b64ToString(s):
    origin = s
    s = tools.change2Bytes(s)
    decode = base64.b64decode(s)
    decode = tools.change2Str(decode)
    info1='\nBase64:' + origin
    info2 = 'Base64 decode:' + decode
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')
#将字符串转为b32编码格式
def stringToB32(s):
    origin = tools.change2Str(s)
    s = tools.change2Bytes(s)
    encode = base64.b32encode(s)
    encode = tools.change2Str(encode)
    info1='\nOriginal:' + origin
    info2 = 'Base32 encode:' + encode
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')

    
#将base32编码格式转化为正常的字符类型
def b32ToString(s):
    origin = tools.change2Str(s)
    decode = base64.b32decode(s)
    decode = tools.change2Str(decode)
    info1='\nBase32:' + origin
    info2 = 'Base32 decode:' + decode
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')
# 将base16编码格式转化为正常的字符类型
def b16ToString(s):
    origin = tools.change2Str(s)
    s = tools.change2Bytes(s)
    decode = base64.b16decode(s)
    encode = tools.change2Str(s)
    info1='\nBase16:' + s
    info2 = 'Base16 decode:' + decode
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')

# 将字符串转为base16编码格式
def stringToB16(s):
    origin = tools.change2Str(s)
    s = tools.change2Bytes(s)
    encode = base64.b16encode(s)
    encode = tools.change2Str(encode)
    info1='\nOriginal:' + origin
    info2 = 'Base16 encode:' + encode
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')
if __name__=='__main__':

    s = b"MNMGI3A="
    stringToB16(s)
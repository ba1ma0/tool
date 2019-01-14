#-*- coding:utf-8 -*-
# Python 3.5
# Author: 白猫 <cyber-security@qq.com>
import string
from module import tools
'''
此脚本主要是将PHP代码转化为没有字母的代码
'''
def withoutAlphas(payload,operator):
    #所有大小写字母的ASCII值
    A2z=[65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,
         97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
    #!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ 所有的符号
    special=["\n"," ","_"]#一些不处理的特殊字符如换行,空格等
    res=""
    for i in payload:
        if i in special:
            res=res+"'{i}'".format(i=i)+"."
        else:
            xorRes=ord(i)^ord(operator)#任何一个数异或两次都会得到本身
            hexRes=tools.decToHex(str(xorRes)).replace(' ','')
            #print(str(hexRes) +" " +str(len(hexRes)))
            if len(hexRes)<4:
                hexRes=hexRes.replace("0x","%0")
            else:
                hexRes=hexRes.replace("0x","%")
            temp=("('{hexRes}'^'{punc}')").format(hexRes=hexRes,punc=operator)+'.'
            res=res+temp
            temp=''
    return res[:-1]

# def usingCharacters(payload,operator):
    


        
        
        



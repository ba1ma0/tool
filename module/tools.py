import re
from module import printc
def split2List(s):
    p="\d+"
    try:
        return re.findall(p,s)
    except:
        msg="\n[-]您输入的数据好像不合法哦"
        printc.printf(msg,'red')
#导入需要的依赖包,如果用户没有安装则提示用户安装
def importModules():
    try:
        import PIL
        from PIL import Image
    except:
        msg="\n[-] 检测到你还没有安装依赖包PIL,请使用命令pip install PIL 进行安装"
        printc.printf(msg,'red')
    def lettToASCII(s):
        result = ''
        for i in s:
            result = result + str(ord(i)) + ' '
        return result

# 将ASCII转化为对应的字母以及字符
def asciiToLett(s):
    #list = s.split(' ')
    list=tools.split2List(s)
    print(list)
    result = ''
    for i in list:
        i = int(i)
        result = result + chr(i)
    return result

# 将十六进制转化为十进制
def hexToDec(s):
    original = s
    s = s.split(" ")
    if s[len(s)-1] =="":
        del s[len(s)-1]
    result = ''
    for i in s:
        result = result + " " + str(int(i, 16))
    return result

# 将十进制转化为十六进制
def decToHex(s):
    original = s
    s=s.split(" ")
    if s[len(s)-1] =="":
        del s[len(s)-1]
    result = ''
    for i in s:
        i = int(i)
        result = result + " " + hex(i)
    return result
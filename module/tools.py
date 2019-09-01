import re,os
from module import printc
#匹配输入的数据 例如输入 123,12,11程序匹配之后返回['123','12','11']列表
def split2List(s):
    p="\w+"
    try:
        return re.findall(p,s)
    except:
        msg="\n[-]您输入的数据好像不合法哦"
        printc.printf(msg,'red')
#导入需要的依赖包,如果用户没有安装则提示用户安装
def importModules():
    try:
        # import PIL
        from PIL import Image
    except:
        msg="\n[-] 检测到你还没有安装依赖包PIL,请使用命令pip install PIL 进行安装"
        printc.printf(msg,'red')

# 将字母转化为对应的ASCII
def lettToASCII(s):
    p="[\w\W]"
    p1=" "
    if len(re.findall(p1,s))>=2:
       s=s.replace(" ",'')
    s=re.findall(p,s)
    result = ''
    for i in s:
        result = result + str(ord(i)) + ' '
    return result

# 将ASCII转化为对应的字母以及字符
def asciiToLett(s):
    #list = s.split(' ')
    list=split2List(s)
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

#读取含有rgb值的txt文件
def readFile2list(add):
    l=[]
    p="\d+,\d+,\d+"
    f = open(add,'rb')
    for i in f.readlines():
        i=str(i)
        l.append(re.findall(p,i)[0])
    return l 
#删除文件中无用且重复的信息            
def delUseless(add):
    try:
        l1=l2=[]
        f=open(add,"r+")
        for i in f.readlines():
            i=i.replace("\n","") 
            l1.append(i)
        f.close()
        # s=list(set(s))
        l2 = sorted(set(l1),key=l1.index)
        with open(add,"w+") as f:
            for i in l2:
                f.write(i+"\n")
            f.close()
        msg="\n[+] 已经清除 {add} 文件中的重复元素".format(add=add)
        printc.printf(msg,"green")
    except:
        msg1="[-] 是不是路径输错了呢?"
        printc.printf(msg1,"red")
#将字符串设定为统一长度
def setStr2SameLen(length,string):
    length=length-len(string)
    for i in range(length):
        string=string+' '
    return string
#将字符串转化为数组
def string2arr(strs):
    s=[]
    for i in strs:
        s.append(i)
    return s
#字符串中是否含有字母
def ifHasLetters(str):
    p='[a-zA-Z]+'
    res=re.findall(p,str)
    if len(res)>=1:
        return True
    else:
        return False
#不管是什么类型都将其转化为bytes类型
def change2Bytes(s):
    if type(s) == bytes:
        return s
    else:
        s = bytes(s,encoding="utf-8")
        return s 
#不管是什么类型都将其转化为str类型
def change2Str(s):
    if type(s) == str:
        return s
    else:
        return str(s,encoding="utf-8")

#批量修改某文件夹下某文件后缀  例如   123.txt  ->  123.py
#写这个函数的原因是有一次分析webshell时,拿到的疑似木马的文件全是txt,但是我要转化为jsp,php文件这时工作量就很大,就想有个工具就很棒了
def rename(path,old_ext,new_ext):
    # path= input("请输入要处理的文件夹路径")
    # print (path)
    print("\n")
    old_ext= "." + str(old_ext)
    # print (old_ext)
    new_ext= "." + str(new_ext)
    # print (new_ext)
    for (path, dirs, files) in os.walk(path):#遍历目录树
        for filename in files:
            ext = os.path.splitext(filename)[1]#取得文件类型，注意它还带着点号
            #print (ext)
            if(ext == old_ext):
                #print ("----------------")
                newname = filename.replace(old_ext, new_ext)
                oldpath = path+ "\\" + filename
                newpath = path+ "\\" + newname
                msg     = "[+] %s  ->  %s"%(oldpath,newpath)
                # print(msg)
                printc.printf(msg,"green")    
                try:   
                    os.rename(oldpath, newpath)
                except :
                   print(str(e))
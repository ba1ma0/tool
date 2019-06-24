'''该工具的设计初衷是在渗透中遇到什么需求就添加什么功能,所以后期会不断添加新功能,当然也非常期待与别人一同开发完善该工具'''
#-*- coding:utf-8 -*-
# Python 3.6
# Author: 白猫 <cyber-security@qq.com>
# Date: 2019-1-18 13:57:54
import hashlib,base64,string,os,sys,time,logging,string,re
from module import tools,argparse,random,printc,noAlphaPayload,fileMonitor,ip2Int
try:
    import PIL
    from PIL import Image
except:
    msg="\n[-] 检测到你还没有安装依赖包PIL,请使用命令pip install PIL 进行安装"
    printc.printf(msg,'red')

presentAdd = os.getcwd()
sys.path.append(presentAdd+"\\module\\urllib")
sys.path.append(presentAdd+"\\module\\zxing")
from module import zxing
import urllib
from urllib import parse
visibleCharacter={
    ' ': '%08','    ': '%09',
    '!': '%21', "\"": '%22', '#': '%23', '$': '%24', '%': '%25', '&': '%26','\'':'%27' ,'(': '%28',')': '%29',
    '*':'%2a','+':'%2b',',':'%2c','-':'%2d','.':'%2e','/':'%2f',
    '0': '%30', '1': '%31', '2': '%32', '3': '%33', '4': '%34', '5': '%35', '6': '%36', '7': '%37', '8': '%38', '9': '%39',
    ':':'%3a',';':'%3b','<':'%3c','=':'%3d','>':'%3e','?':'%3f','@':'%40',
    'A':'%41','B':'%42','C':'%43','D':'%44','E':'%45','F':'%46','G':'%47','H':'%48','I':'%49','J':'%4a','K':'%4b','L':'%4c','M':'%4d','N':'%4e','O':'%4f','P':'%50','Q':'%51','R':'%52','S':'%53','T':'%54','U':'%55','V':'%56','W':'%57','X':'%58','Y':'%59','Z':'%5a',
    '[':'%5b','\\':'%5c',']':'%5d','^':'%5e','_':'%5f','\`':'%60',
    'a':'%61','b':'%62','c':'%63','d':'%64','e':'%65','f':'%66','g':'%67','h':'%68','i':'%69','j':'%6a','k':'%6b','l':'%6c','m':'%6d','n':'%6e','o':'%6f','p':'%70','q':'%71','r':'%72','s':'%73','t':'%74','u':'%75','v':'%76','w':'%77','x':'%78','y':'%79','z':'%7a',
    '{':'%7b','|':'%7c','}':'%7d','~':'%7e',
    ',':'%82','\"':'%84',
}

def menu():
    usage = """  -m MD5 encryption
       -s        SH1 encryption
       -help     Show help information
       -b64      Base64 encode
       -b32      Base32 encode
       -b16      Base16 encode
       -db64     Base64 decode
       -db32     Base32 decode
       -db16     Base16 decode
       -urlen    URL encode
       -urlde    URL decode
       -unien    Unicode Encode                 Example:  -unien    "A"        Result: \\u0061
       -unide    Unicode Decode                 Example:  -unide    "\\u0061"   Result: A
       -hten     HTML Encode                    Example:  -hten    "A"         Result: &#97;
       -htde     HTML Decode                    Example:  -htde    "&#97"      Result: A
       -bin      Binary To Decimal
       -octal    Octal Decimal to Decimal
       -hex      Hexadecimal to Decimal
       -dbin     Decimal To Binary 
       -doctal   Decimal to Octal 
       -dhex     Decimal to Hexadecimal
       -ip2int   Convert IP to Decimal           Example:  -ip2int  127.0.0.1
       -int2ip   Convert int to IP               Example:  -int2ip  2130706433
       -ord      Letter To ASCII  attention      Example:  -ord asdfasfa      -ord "dfafs afasfa  asfasf"
       -chr      ASCII  To Letters               Example:  -chr 105           -chr "102 258 654"
       -roten    Rot Encode                      Example:  -roten dafsdfa -offset 13  Means rot_13 Encode
       -rotde    Rot Decode                      Example:  -rotde dafsdfa -offset 13  Means rot_13 Decode
       -offset   Rot Encode or Decode Offset     
       -gqr      Generate QRcode images          Example:  -gqr  "I love you"
       -pqr      Parse QRcode  images            Example:  -pqr  "C:\\QR.png"  
       -add      File address                    Example:  -add  "C:\\1.txt"
       -delete   Delete File's repeated info     Example:  -del  "C:\\1.txt" 
       -r2i      Convert RGB txt to Images       Example:  -r2i  "C:\\rgb.txt" -x 100 -y 200   
       -monitor  Directory file changes monitor  Example:  -monitor  "C:\directory" 
       -x      X 
       -y      y   
      """

    #在使用ord 和chr命令的时候要注意如果输入的字符和数字不包含空格则直接实用例子前面的命令如果包含空格则使用后面的命令

    parser = argparse.ArgumentParser()

    parser.add_argument('-m',dest='md',help='MD5 encryption')
    parser.add_argument('-s', dest='sh', help='SH1 encryption')
    parser.add_argument('-help', action="store_true", help='To show help information')
    parser.add_argument('-b64', dest='b64', help='Base64 encode')
    parser.add_argument('-b32', dest='b32', help='Base32 encode')
    parser.add_argument('-b16', dest='b16', help='Base16 encode')
    parser.add_argument('-db64', dest='db64', help='Base64 decode')
    parser.add_argument('-db32', dest='db32', help='Base32 decode')
    parser.add_argument('-db16', dest='db16', help='Base16 decode')
    parser.add_argument('-urlen', dest='urlen', help='URL encode')
    parser.add_argument('-urlde', dest='urlde', help='URL decode')
    parser.add_argument('-unien', dest='unien', help='Unicode Encode')
    parser.add_argument('-unide', dest='unide', help='Unicode Decode ')
    parser.add_argument('-hten', dest='hten', help='HTML Encode')
    parser.add_argument('-htde', dest='htde', help='HTML Decode ')
    parser.add_argument('-bin', dest='bin', help='Binary To Decimal')
    parser.add_argument('-octal', dest='octal', help='Octal  to Decimal')
    parser.add_argument('-hex', dest='hex', help='Hexadecimal to Decimal')
    parser.add_argument('-dbin', dest='dbin', help='Decimal To Binary ')
    parser.add_argument('-doctal', dest='doctal', help='Decimal to Octal ')
    parser.add_argument('-dhex', dest='dhex', help='Decimal to Hexadecimal')

    parser.add_argument('-ip2int', dest='ip2int', help='Convert IP to Decimal ')
    parser.add_argument('-int2ip', dest='int2ip', help='Convert Decimal to IP ')
    
    parser.add_argument('-ord', dest='ord', help="Letter To ASCII               Example:  -ord aaaaaa  , -ord=\"aaa aaa\"")
    parser.add_argument('-chr', dest='chr', help="ASCII  To Letter              Example:  -chr 105     ,  -chr = \"101 101\" ")
    parser.add_argument('-roten',dest='roten', help='Rot Encode                      Example:  -roten dafsdfa -offset 13  Means rot_13 Encode')
    parser.add_argument('-rotde', dest='rotde', help='Rot Decode                      Example:  -rotde dafsdfa -offset 13  Means rot_13 Decode')
    parser.add_argument('-gqr', dest='gqr', help='Generate QRcode images          Example:  -gqr = "I love you"')
    parser.add_argument('-pqr', dest='pqr', help='Parse QRcode  images            Example:  -pqr = "C:\\QR.png"')
    parser.add_argument('-delete', dest='delete', help='Delete File\'s repeated info     Example:  -del  "C:\\1.txt" ')
    parser.add_argument('-i2r', dest='i2r', help='Convert Image to RGB txt        Example:  -i2r = "C:\\png.png"')
    parser.add_argument('-r2i', dest='r2i', help='Convert RGB txt to Images       Example:  -r2i = "C:\\rgb.txt" -x 100 -y 200 ')
    parser.add_argument('-monitor', dest='monitor', help='File monitor')
    parser.add_argument('-x', dest='x', help='X')
    parser.add_argument('-y', dest='y', help='y')
    parser.add_argument('-offset', dest='offset', type=int,help=' ')
    # try:
    options = parser.parse_args()
    if options.md :
        s = options.md
        md5(s)
    elif options.sh:
        s = options.sh
        sh1(s)
    elif options.b64:
        s = options.b64
        stringToB64(s)
    elif options.b32:
        s = options.b32
        stringToB32(s)
    elif options.b16:
        s = options.b16
        stringToB16(s)
    elif options.db64:
        s = options.db64
        b64ToString(s)
    elif options.db32:
        s = options.db32
        b32ToString(s)
    elif options.db16:
        s = options.db16
        b16ToString(s)
    elif options.urlen:
        s = options.urlen
        urlEncode(s)
    elif options.urlde:
        s = options.urlde
        urlDecode(s)
    elif options.bin:
        s = options.bin
        binToDec(s)
    elif options.octal:
        s = options.octal
        octToDec(s)
    elif options.hex:
        s = options.hex
        hexToDec(s)
    elif options.dbin:
        s = options.dbin
        decToBin(s)
    elif options.doctal:
        s = options.doctal
        decToOct(s)
    elif options.dhex:
        s = options.dhex
        decToHex(s)
    elif options.ip2int:
        ip = options.ip2int
        ip_int = ip2Int.ip2int(ip)
        msg1 = "IP:" + str(ip)
        msg2 = "Decimal:" + str(ip_int)
        printc.printf(msg1,'blue')
        printc.printf(msg2,'green')

    elif options.int2ip:
        decimal = options.int2ip
        ip   = ip2Int.int2ip(str(decimal))
        msg1 = "Decimal:" + str(decimal)
        msg2 = "IP:" + str(ip)
        printc.printf(msg1,'blue')
        printc.printf(msg2,'green')

    elif options.ord:
        s = options.ord
        lettToASCII(s)
    elif options.chr:
        s = options.chr
        asciiToLett(s)
    elif options.roten and options.offset:
        s = options.roten
        offset = options.offset
        msg1="\nOrigina    :"+s
        msg2="Rot{offset} Encode:".format(offset=offset)+rotEncode(s,offset)
        printc.printf(msg1,'blue')
        printc.printf(msg2,'green')
    elif options.rotde and options.offset:
        s = options.rotde
        offset = options.offset
        msg1="\nRot_{offset} Encode:".format(offset=offset) + s
        msg2="Rot_{offset} Decode:".format(offset=offset)+ str(rotDecode(s, offset))
        printc.printf(msg1,"blue")
        printc.printf(msg2,"green")
    elif options.gqr:
        print()
        s = options.gqr
        generateQR(s)
    elif options.pqr:
        print()
        s = options.pqr
        parseQR(s)
    elif options.unien:
        print()
        s = options.unien
        uniencode(s)
    elif options.unide:
        print()
        s = options.unide
        unidecode(s)
    elif options.hten:
        print()
        s = options.hten
        htmlencode(s)
    elif options.htde:
        print()
        s = options.htde
        htmldecode(s)
    elif options.i2r:
        file_add=options.i2r
        png2rgb(file_add)
    elif options.delete:
        add=options.delete
        tools.delUseless(add)
    elif options.r2i:
        file_add=options.r2i
        if options.x:
            x=options.x
            if options.y:
                y = options.y
                rgb2png(int(x),int(y),file_add)
            else:
                info1="\n[-] 您需要输入生成图片的尺寸y参数"
                printc.printf(info1,'red')
        else:
            info1="\n[-] 您需要输入生成图片的尺寸x参数"
            printc.printf(info1,'red')  
    elif options.monitor:
        path = options.monitor
        fileMonitor.showChangeInfo(path)
    else:
        helpInfo()
    # except:
    #     info1="\n[-]是不是输错参数了,试一下python tool.py -help 看一下帮助信息吧"
    #     printc.printf(info1,'red')

def helpInfo():
    printc.printf("""++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
       -s        SH1 encryption
       -help     Show help information
       -b64      Base64 encode
       -b32      Base32 encode
       -b16      Base16 encode
       -db64     Base64 decode
       -db32     Base32 decode
       -db16     Base16 decode
       -urlen    URL encode
       -urlde    URL decode
       -unien    Unicode Encode                 Example:  -unien    "A"        Result: \\u0061
       -unide    Unicode Decode                 Example:  -unide    "\\u0061"   Result: A
       -hten     HTML Encode                    Example:  -hten    "A"         Result: &#97;
       -htde     HTML Decode                    Example:  -htde    "&#97"      Result: A
       -bin      Binary To Decimal
       -octal    Octal Decimal to Decimal
       -hex      Hexadecimal to Decimal
       -dbin     Decimal To Binary 
       -doctal   Decimal to Octal 
       -dhex     Decimal to Hexadecimal
       -ip2int   Convert IP to Decimal           Example:  -ip2int  127.0.0.1
       -int2ip   Convert int to IP               Example:  -int2ip  2130706433
       -ord      Letter To ASCII  attention      Example:  -ord asdfasfa      -ord "dfafs afasfa  asfasf"
       -chr      ASCII  To Letters               Example:  -chr 105           -chr "102 258 654"
       -roten    Rot Encode                      Example:  -roten dafsdfa -offset 13  Means rot_13 Encode
       -rotde    Rot Decode                      Example:  -rotde dafsdfa -offset 13  Means rot_13 Decode
       -offset   Rot Encode or Decode Offset     
       -gqr      Generate QRcode images          Example:  -gqr  "I love you"
       -pqr      Parse QRcode  images            Example:  -pqr  "C:\\QR.png"  
       -add      File address                    Example:  -add  "C:\\1.txt"
       -delete   Delete File's repeated info     Example:  -del  "C:\\1.txt" 
       -r2i      Convert RGB txt to Images       Example:  -r2i  "C:\\rgb.txt" -x 100 -y 200   
       -monitor  Directory file changes monitor  Example:  -monitor  "C:\directory" 
       -x      X 
       -y      y   
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""","skyblue")

# 进行MD5加密
def md5(s):
    original = s
    md  = hashlib.md5()
    s = s.encode(encoding = 'utf-8')
    md.update(s)
    info1='\nOriginal:'+original
    info2='Md5 Encryption:'+md.hexdigest()
    printc.printf(info1,'blue')
    printc.printf(info2,'green')

#进行sh1加密
def sh1(s):
    original = s
    sh = hashlib.sha1()
    s = s.encode(encoding='utf-8')
    info1='\nOriginal:' + original
    info2='SH1 Encryption:' + sh.hexdigest()
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')

#将字符串转换为base64编码格式
def stringToB64(s):
    origin = tools.change2Str(s)
    s = tools.change2Bytes(s)
    res = base64.b64encode(s)
    res = tools.change2Str(res)
    info1='\nOriginal:' + origin
    info2 = 'Base64 encode:' + res
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')

#将base64编码格式转化为正常的字符类型
def b64ToString(s):
    origin = tools.change2Str(s)
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


# 将base16编码格式转化为正常的字符类型
def b16ToString(s):
    origin = tools.change2Str(s)
    s = tools.change2Bytes(s)
    decode = base64.b16decode(s)
    decode = tools.change2Str(decode)
    info1='\nBase16:' + origin
    info2 = 'Base16 decode:' + decode
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')

def isVisibleCharacter(s):
    try:
        for i in string.printable:
            if (s==i):
                return True
                break
    except:
        return False


#进行url编码
def urlEncode(s):
    encodeString=''
    for i in s:
        if (isVisibleCharacter(i)):
            encodeString=encodeString+visibleCharacter[i]
        else:
            encodeString=encodeString+urllib.parse.quote(i)
    info1='\nOriginal:' + s
    info2 = 'URL encode:' + encodeString
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')



#进行url解码
def urlDecode(s):
    decode=''
    p = '%[0-9]+'
    for i in re.findall(p,s):
        res = tools.change2Str(urllib.parse.unquote(i))
        if res =="\x08":
            decode = decode + " "
        else:
            decode = decode + res 
    info1='\nURL encode:' + s
    info2 = 'URL decode:' + decode
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')


#将二进制转化为十进制
def binToDec(s):
    original = s
    #s = s.split(" ")
    s=tools.split2List(s)
    result = ''
    for i in s:
        result = result+" "+str(int(i,2))
    info1='\nBinary :'+str(original)
    info2 = 'Decimal :' + str(result)
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')


# 将八进制转化为十进制
def octToDec(s):
    original = s
    #s = s.split(" ")
    s=tools.split2List(s)
    result = ''
    for i in s:
        result = result+" "+str(int(i, 8))
    info1='\nOctal :' + str(original)
    info2 = 'Decimal :' + str(result)
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')


# 将十六进制转化为十进制
def hexToDec(s):
    original = s
    #s = s.split(" ")
    s=tools.split2List(s)
    result = ''
    for i in s:
        result = result+" "+str(int(i, 16))
    info1='\nHex :' + str(original)
    info2 = 'Decimal :' + str(result)
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')


# 将十进制转化为二进制
def decToBin(s):
    original=s
    #s =s.split(" ")
    s=tools.split2List(s)
    result=''
    for i in s:
        i = int(i)
        result =result+ " "+bin(i)
    info1='\nDecimal:' + str(original)
    info2 = 'Binary:' + str(result)
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')

# 测试
def test(s):
    print("Successful:"+str(s))

# 将十进制转化为八进制
def decToOct(s):
    original = s
    #s = s.split(" ")
    s=tools.split2List(s)
    result = ''
    for i in s:
        i = int(i)
        result = result+" "+oct(i)
    info1='\nDecimal :' + str(original)
    info2 = 'Octal :' + str(result)
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')


# 将十进制转化为十六进制
def decToHex(s):
    original = s
    #s = s.split(" ")
    s=tools.split2List(s)
    result = ''
    for i in s:
        i = int(i)
        result = result+" "+hex(i)
    info1='\nDecimal :' + str(original)
    info2 = 'Hex :' + str(result)
    printc.printf(info1, 'blue')
    printc.printf(info2, 'green')


#将字母转化为对应的ASCII

def lettToASCII(s):
   original=s
   p="[\w\W]"
   p1=" "
   if len(re.findall(p1,s))>=2:
       s=s.replace(" ",'')
   s=re.findall(p,s)
   result = ''
   for i in s:
       result = result+str(ord(i)) + ' '
   info1='\nLetters:'+original
   info2 = 'ASCII  :'+result
   printc.printf(info1, 'blue')
   printc.printf(info2, 'green')


#将ASCII转化为对应的字母以及字符
def asciiToLett(s):
   #list=s.split(' ')
   list=tools.split2List(s)
   result = ''
   for i in list:
       i = int(i)
       result =result + chr(i)

   info1='\nASCII    :'+s
   info2 = 'Letters  :'+result
   printc.printf(info1, 'blue')
   printc.printf(info2, 'green')


#Rot类型的加密：就是将字母在字母表中向前移动n位

def rotEncode(st,offset):
    def rot(ch):
        f = lambda x : chr((ord(ch)-x+offset)%26+x)
        return f(97) if ch.islower() else (f(65) if ch.isupper() else ch)
    return ''.join(rot(c) for c in st)



#Rot类型的解密：rot加密的逆向过程

def rotDecode(st,offset):
    def rot(ch):
        f = lambda x : chr((ord(ch)-x-offset)%26+x)
        return f(97) if ch.islower() else (f(65) if ch.isupper() else ch)
    return ''.join(rot(c) for c in st)

#生成二维码图片
def generateQR(data):
    QRImagePath =os.getcwd()+"/qrcode.png"
    info1="\n照片存储在:"+QRImagePath
    info2="信息:"+data
    printc.printf(info1,"blue")
    printc.printf(info2,"green")
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    #data = input("请输入信息:")
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    img.save('qrcode.png')
    if sys.platform.find('darwin') >= 0:
        os.system('open %s' % QRImagePath)
    elif sys.platform.find('linux') >= 0:
        os.system('xdg-open %s' % QRImagePath)
    else:
        os.system('call %s' % QRImagePath)
    time.sleep(1)

#解析二维码图片
def parseQR(filename):
    #filename=input("请输入二维码照片路径:")
    img=Image.open(filename)
    ran=int(random.random()*100000)
    img.save('%s%s.jpg' % (os.path.basename(filename).split('.')[0], ran))
    zx=zxing.BarCodeReader()
    data=''
    zxdata = zx.decode('%s%s.jpg' % (os.path.basename(filename).split('.')[0], ran))
    info1="\n二维码路径:"+filename
    info2="二维码详情:"+str(zxdata)
    printc.printf(info1,"blue")
    printc.printf(info2,"green")

#将字符串进行unicode编码
def uniencode(s):
    original=s
    s=tools.lettToASCII(s)
    s=tools.decToHex(s)
    s=" "+s
    s=s.replace(" 0x","\\u00")
    info1="\nString       : "+original
    info2="UnicodeEncode: "+s

    printc.printf(info1, "blue")
    printc.printf(info2, "green")

#将unicode编码格式的字符串解码为正常的字符串
def unidecode(s):
    original = s
    temp=''
    s=s.replace("\\u00"," 0x")
    s=s.split(" ")
    del s[0]
    for i in range(len(s)):
        if i<len(s)-1:
            temp = temp + str(s[i]) + " "
        else:
            temp=temp+str(s[i])
    s=temp
    s=tools.hexToDec(s)
    s=s.split(" ")
    temp=''
    del s[0]
    for i in range(len(s)):
        if i < len(s) - 1:
            temp = temp + str(s[i]) + " "
        else:
            temp = temp + str(s[i])
    s=temp
    s=tools.asciiToLett(s)

    info1 = "String:      " + original
    info2 = "UnicodeDecode:  " + s
    printc.printf(info1, "blue")
    printc.printf(info2, "green")

def htmlencode(s):
    original=s
    temp=""
    s=tools.lettToASCII(s)
    s=s.split()
    for i in range(len(s)):
        temp = temp +"&#"+ str(s[i]) + ";"
    s=temp

    info1="\nOriginal String: "+original
    info2="HTML   Encoding: "+s
    printc.printf(info1, "blue")
    printc.printf(info2, "green")

def htmldecode(s):
    original=s
    temp=''
    s = s.replace(";", "")
    s = s.replace("&#", " ")
    s = s.split()
    for i in range(len(s)):
        if i < len(s) - 1:
            temp = temp + str(s[i]) + " "
        else:
            temp = temp + str(s[i])
    s=temp
    s=tools.asciiToLett(s)
    info1="\nHTML Encode:"+original
    info2="HTML Decode:"+s
    printc.printf(info1, "blue")
    printc.printf(info2, "green")
#根据含有rgb值的txt文件转化为png照片

def rgb2png(x,y,add):
    try:
        # x = 8 #x坐标  通过对txt里的行数进行整数分解
        # y = 12 #y坐标  x*y = 行数
        im = Image.new("RGB",(x,y))#创建图片
        #file = open() #打开rbg值文件
        lists = tools.readFile2list(add)
        index=0
        for i in range(0,x):
            for j in range(0,y):
                line=lists[index]
                index+=1
                rgb = line.split(",")#分离rgb
                im.putpixel((i,j),(int(rgb[0]),int(rgb[1]),int(rgb[2])))#rgb转化为像素
        im.save("res.png")
        os.system(' %s' % "res.png")
        file_name="res.png"
        file_add = os.getcwd()+"/"+file_name
        # os.system(' %s' % file_name)
        info1="\n源RGB文件地址 :  "+add
        info2="生成PNG的地址 :  "+file_add
        printc.printf(info1, "blue")
        printc.printf(info2, "green")
    except:
        info1="\n\n[-] 您输入的x和y值可能不合适,再试一下其他x y组合吧,注意xy相乘结果应该等于txt文件的总行数"
        printc.printf(info1,'red')

#将照片转化为RGB值并保存为txt文件
def png2rgb(add):
    image = Image.open(add)
    file_name="res.txt"
    file_add=os.getcwd()+"\\res.txt"
    pic =image.load()
    width = image.size[0]
    height = image.size[1]
    f =open(file_name,'wb')
    for x in range(width):
        for y in range(height):
            print(image[x][y])
            # f.write(str(image[x][y]))
    f.close
    info1="\n源照片地址:  "+add
    info2="生成RGB的txt文件地址:"+file_add
    printc.printf(info1, "blue")
    printc.printf(info2, "green")

if __name__=='__main__':
    #jsencode('chindshdhjsd')
    #jsdecode("%63%68%69%6e%64%73%68%64%68%6a%73%64")
    # htmlencode("Q B n d")
    # htmldecode("&#81;&#32;&#66;&#32;&#110;&#32;&#100;")
    menu()
    # s=noAlphaPayload.withoutAlphas("assert_","`")
    # fileMonitor.showChangeInfo("C:\\")

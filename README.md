﻿中文说明:
========
## 更新日志
1. 新增将含有rgb值的txt文件转化为png照片的实用功能 python tool.py -r2i  "C:\rgb.txt" -x 100 -y 200

## 使用说明 
这是一款在Windows上基于python3的强大的编码解码的工具!

您只需要下载即可使用,因为我已经将需要的东西全部封装起来

您只需要输入python tool.py就可以并且得到如下结果:
	 	
       -m      MD5  encryption
       -s      SH1 encryption
       -help   Show help information
       -b64    Base64 encode
       -b32    Base32 encode
       -b16    Base16 encode
       -db64   Base64 decode
       -db32   Base32 decode
       -db16   Base16 decode
       -urlen  URL encode
       -urlde  URL decode
       -unien  Unicode Encode                 Example:  -unien    "A"        Result: \u0061
       -unide  Unicode Decode                 Example:  -unide    "\u0061"   Result: A
       -hten   HTML Encode                    Example:  -hten    "A"         Result: &#97;
       -htde   HTML Decode                    Example:  -htde    "&#97"      Result: A
       -bin    Binary To Decimal
       -octal  Octal Decimal to Decimal
       -hex    Hexadecimal to Decimal
       -dbin   Decimal To Binary
       -doctal Decimal to Octal
       -dhex   Decimal to Hexadecimal
       -ord    Letter To ASCII  attention      Example:  -ord asdfasfa      -ord "dfafs afasfa  asfasf"
       -chr    ASCII  To Letters               Example:  -chr 105           -chr "102 258 654"
       -roten  Rot Encode                      Example:  -roten dafsdfa -offset 13  Means rot_13 Encode
       -rotde  Rot Decode                      Example:  -rotde dafsdfa -offset 13  Means rot_13 Decode
       -offset Rot Encode or Decode Offset
       -gqr    Generate QRcode images          Example:  -gqr  "I love you"
       -pqr    Parse QRcode  images            Example:  -pqr  "C:\QR.png"
       -add    File address                    Example:  -add  "C:\1.txt"
       -r2i    Convert RGB txt to Images       Example:  -r2i  "C:\rgb.txt" -x 100 -y 200
       -x      X
       -y      y


优     点:小巧,方便,强大，常见的编码方式应有尽有.

比如您输入: python tool.py -urlen="Hello China"您可以得到如下结果

Original:Hello China

URL encode:%48%65%6c%6c%6f%08%43%68%69%6e%61

	
******************************************************************************
分割线 分割线	分割线	分割线	分割线	分割线	分割线
******************************************************************************
English introduction:
========
This is an powerful encoding&decoding tool based on python3

What you need to do is just download it and use it because have packaged all third-part modules

What you need to do is just type python tool.py and then you can get the result as follows

       -m      MD5  encryption
       -s      SH1 encryption
       -help   Show help information
       -b64    Base64 encode
       -b32    Base32 encode
       -b16    Base16 encode
       -db64   Base64 decode
       -db32   Base32 decode
       -db16   Base16 decode
       -urlen  URL encode
       -urlde  URL decode
       -unien  Unicode Encode                 Example:  -unien    "A"        Result: \u0061
       -unide  Unicode Decode                 Example:  -unide    "\u0061"   Result: A
       -hten   HTML Encode                    Example:  -hten    "A"         Result: &#97;
       -htde   HTML Decode                    Example:  -htde    "&#97"      Result: A
       -bin    Binary To Decimal
       -octal  Octal Decimal to Decimal
       -hex    Hexadecimal to Decimal
       -dbin   Decimal To Binary
       -doctal Decimal to Octal
       -dhex   Decimal to Hexadecimal
       -ord    Letter To ASCII  attention      Example:  -ord asdfasfa      -ord "dfafs afasfa  asfasf"
       -chr    ASCII  To Letters               Example:  -chr 105           -chr "102 258 654"
       -roten  Rot Encode                      Example:  -roten dafsdfa -offset 13  Means rot_13 Encode
       -rotde  Rot Decode                      Example:  -rotde dafsdfa -offset 13  Means rot_13 Decode
       -offset Rot Encode or Decode Offset
       -gqr    Generate QRcode images          Example:  -gqr  "I love you"
       -pqr    Parse QRcode  images            Example:  -pqr  "C:\QR.png"
       -add    File address                    Example:  -add  "C:\1.txt"
       -r2i    Convert RGB txt to Images       Example:  -r2i  "C:\rgb.txt" -x 100 -y 200
       -x      X
       -y      y

Advantage:small but powerful ,it includes most of usual encoding methods

For example: python tool.py -urlen="Hello English" then you can get as follows

Original:Hello English

URL encode:%48%65%6c%6c%6f%08%45%6e%67%6c%69%73%68
				


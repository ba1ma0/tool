#-*-coding:utf-8-*-
'''
    IP转换为整形：形如123.125.0.236 可以看成用点分割的四个小段的整数，每个小段的范围为0~255，那么就可以将每个数字转换为二进制的数字。
     第一段：123转换为二进制   01111011
     第二段：125转换为二进制   01111101
     第三段： 0   转换为二进制   00000000
     第四段： 236转换为二进制  11101100
     然后将四段拼接起来成了长的二进制数：01111011011111010000000011101100
     并将这个厂二进制数转换为整形的数字：2071789804
'''
#将ip地址转化为十进制数字
def ip2int(a):
    #  转换为4个段的列表
    a_list = a.split('.',4)
    # a_list.reverse()
    a_str = ''
    for i in a_list:
        a_tem = bin(int(i))[2:] # 字符串
        if len( a_tem) != 8:
        # 在前面加 0
            a_str += '0'*(8-len(a_tem))+a_tem
        else:
            a_str += a_tem
    # print a_str
    return int(a_str,2)
#将十进制数字转化为标准的IP地址
def int2ip(b):
    #先转换为二进制
    b_tem = bin(int(b))[2:]
    b_str = ''
    # 将所有的 0 补齐
    if len(b_tem) < 32:
       b_str = '0' * (32 - len(b_tem)) + b_tem
    else:
        b_str = b_tem
        # print(len(b_tem))
        # print("ERROR")
    #32位二进制数字均分为四块
    print(b_str)
    b1 = b_str[0:8]
    b2 = b_str[8:16]
    b3 = b_str[16:24]
    b4 = b_str[24:]
    # print(b1)
    # print(b2)
    # print(b3)
    # print(b4)
    b_out= str(int(b1,2))+'.'+str(int(b2 ,2))+'.'+str(int(b3,2))+'.'+str(int(b4,2))
    return b_out

if __name__ == '__main__':
    #a = input('您需要将IP转为整型，请输入IP：\n')
    b = input('您需要将整型转为IP，请输入整型：\n')
    #a_c = ip2int(a)
    b_c = int2ip(b)
    #print (a_c)
    print (b_c)
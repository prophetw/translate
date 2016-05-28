import requests
import random
import re
import time
url = 'http://www.baidu.com'
# s = requests.session()
# print(s)
# r = s.request('get', url)
# print(r.cookies)


'''
GET 请求下方的地址 会 response 里面 会有  token 参数
但是  传递的参数  里面
gid=12810E0-0DC4-4DD4-A9AB-F165A1A94BD2  tt=1464073931297 这两个参数比较特殊

gid 是一个 随机数 生成的 什么 编码
tt  代表 当前时间

https://passport.baidu.com/v2/api/?getapi&tpl=mn&apiver=v3&tt=1464073931297&class=login&gid=12810E0-0DC4-4DD4-A9AB-F165A1A94BD2&logintype=dialogLogin&callback=bd__cbs__vj837r



'''
def generateGid():
    demo = 'xxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'
    reg_exp = r'[xy]'
    result = ''
    for i in demo:
        if i=='x' or i=='y':
            c = int(random.random() * 16)
            v = c if i == 'x' else (c & 3 | 8)
            s = str(hex(v))
            result += str(s[2:]).upper()
        else:
            result += str(i)
    return result
def generateTime():
    return int(time.time()*1000)


gid = generateGid()
print(gid)
tt = generateTime()
print(tt)




def getToken():
    token=1








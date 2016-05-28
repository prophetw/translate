import requests


'''
header  for first request


GET / HTTP/1.1
Host	115.com

Cache-Control	max-age=0
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
'Upgrade-Insecure-Requests':	'1'
'User-Agent':	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 115Browser/7.0.0'
'Accept-Encoding':	'gzip, deflate, sdch'
'Accept-Language':	'zh-CN,zh;q=0.8'
'Cookie':	'loginType=0'

login

header
loginType	0
OOFL	85475634
UID	85475634_A1_1464339148
CID	90924ff7695a79fba4e19a02b03b7fb5
SEID	14acc22933908aa07701044418874738b41b46e8874faf70440e35247f02ab4c49d430122c94296b03aaab614cdc9e0c064dc33e59973a88024a39bd




'''
headers = {
    "Cache-Control":"max-age=0",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Upgrade-Insecure-Requests':    '1',
    'User-Agent':    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 115Browser/7.0.0',
    'Accept-Encoding':    'gzip, deflate, sdch',
    'Accept-Language':    'zh-CN,zh;q=0.8',
    'Cookie':    'loginType=0'
}

s = requests.Session()
url = 'http://115.com'
r = s.get(url, headers=headers)
# print(r.text)
print(r.request.headers)
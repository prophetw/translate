#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: python regular expressions
regExp=re.compile(r'\d')
result=regExp.search(str)    return the first result you can use result.group() to get it
result1=regExp.findAll(str)  result1 is an array contains all result
"""
import re
xmasRegex = re.compile(r'\d+\s\w+')
result = xmasRegex.findall('12 drummers, 11pipers, 10 lords, 9 ladies, 8 maids ,7 swans , 6 geese,5 rings , 4 birds, 3 hens,2 doves, 1 partridge')
print(result)
#  ['12 drummers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']
xmasRegex = re.compile(r'\d+\s\w+')
result = xmasRegex.search('12 drummers, 11pipers, 10 lords, 9 ladies, 8 maids ,7 swans , 6 geese,5 rings , 4 birds, 3 hens,2 doves, 1 partridge')
print(result.group())
# 12 drummers
print(result.group(0))
# 12 drummers
# regular expression re.compile(firstArgument,secondArgument)   secondArgument configure some
#  re.IGNORECASE(简写 re.I)  忽略大小写
#  re.VERBOSE  可以在正则里面写 注释
#  re,DOTALL
# second argument re.compile('',re.I | re.VERBOSE | re.IGNORECASE )   可以用pipe的方式  配置参数


# email address regular expressions and phone regular
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # 区域码  类似 0551之类  可有可无
    (\s|-|\.)?   # 分割
    (\d{3})     # 开始的3个数字
    (\s|-|\.)   # 分割
    (\d{4})     # 最后的4个数字
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
)''',re.VERBOSE)
print(phoneRegex.search('222 3333').group())
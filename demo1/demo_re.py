#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: hmchen
@software: PyCharm
@file: demo_re.py
@time: 2021/4/7 
"""

import re

# 正则表达式

"""
复习:
?       匹配零次或一次前面的分组
*       匹配零次或多次前面的分组
+       匹配一次或多次前面的分组
{n}     匹配n次前面的分组
{n,}    匹配n次或更多前面的分组
{,m}    匹配零次到m次前面的分组
{n,m}   匹配至少n次，至多m次前面的分组
{n,m}?或*?或+?对前面的分组进行非贪心匹配
^spam   意味着字符串必须以spam开始
spam$   意味着字符串以spam结束
. 匹配所有的字符，换行符除外
\d 、\w 和 \s 分别匹配数字，单词和空格
\D 、\W 和 \S 分别匹配除数字，单词和空格外的所有字符
[abc]   匹配方括号内的任意字符(如 a,b或c)
[^abc]  匹配不在方括号内的任意字符
   



"""

"""
正则表达式匹配
1、用import re导入正则表达式
2、用re.compile()函数创建一个Regex对象（使用原始字符串）
3、向Regex对象的search()方法传入想查找的字符串，返回一个Match对象.
4、调用Match对象的group()方法，返回实际匹配文本的字符串.

"""

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search('My number is 415-555-4242')
print('Phone number found :' + mo.group())

# 利用括号分组
print('---------------------利用括号分组---------------------------------')
phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search('My number is 415-555-4242')
print('mo.group(1) :', mo.group(1))
print('mo.group(2) :', mo.group(2))
print('mo.group(0) :', mo.group(0))
print('mo.group() :', mo.group())

# groups()
print('---------------------groups()---------------------------------')
areaCode, mainNumber = mo.groups()
print('areaCode :', areaCode)
print('mainNumber :', mainNumber)

"""
管道匹配多个分组
返回匹配的第一个出现的匹配文本

"""
print('---------------------管道匹配多个分组---------------------------------')
heroRegex = re.compile(r'Batman|Tina Fey.')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print('mo.group() :', mo.group())
# mo.group(1)返回第一个括号分组内匹配的文本
print('mo.group(1) :', mo.group(1))

"""
? 问号实现可选匹配

匹配？之前的分组零次或者一次

"""
print('---------------------问号实现可选匹配----------------------------')

batRegex = re.compile(r'Bat(wo)?man')
mo3 = batRegex.search('The Adventures of Batman')
print('mo3.group() :', mo3.group())

mo4 = batRegex.search('The Adventures of Batwoman ')
print('mo4.group() :', mo4.group())

"""
用星号(*)匹配零次或者多次

* 意味着匹配零次或者多次

"""
print("-----------用星号(*)匹配零次或者多次--------")

batRegex = re.compile(r'Bat(wo)*man')
mo5 = batRegex.search('The Adventures of Batman')
print('mo5.group() :', mo5.group())

mo6 = batRegex.search('The Adventures of Batwoman ')
print('mo6.group() :', mo6.group())

mo7 = batRegex.search('The Adventures of Batwowowowowowowowowoman ')
print('mo7.group() :', mo7.group())

"""
用加号匹配一次或多次
+ (加号) 意味着 匹配一次或者多次

"""
print("-----------------------用加号匹配一次或多次------------------------")
batRegex = re.compile(r'Bat(wo)+man')
mo8 = batRegex.search('The Adventures of Batwoman')
print('mo8.group()', mo8.group())

mo9 = batRegex.search('The Adventures of Batwowowowoman')
print('mo9.group()', mo9.group())

mo10 = batRegex.search('The Adventures of Batman')
print('mo10 == None  :', mo10 == None)

"""
花括号匹配特定次数
"""
print('-------------------------------花括号匹配特定次数-------------------------------')

haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('HaHaHa')
print('mo.group() :', mo.group())

mo1 = haRegex.search('Ha')
print('mo1 == None :', mo1 == None)

"""
findall

"""

"""
贪心和非贪心匹配

python正则表达式默认是贪心模式
花括号的非贪心版本匹配尽可能最短的字符串，在结束的花括号后跟着一个问号

"""
print("----------------------------贪心和非贪心匹配-------------------------------")

haRegex = re.compile(r'(Ha){3,5}')
mo = haRegex.search('HaHaHaHaHaHa')
print('mo.group() :', mo.group())

haRegex = re.compile(r'(Ha){3,5}?')
mo = haRegex.search('HaHaHaHaHaHa')
print('mo.group() :', mo.group())

"""
findall()

"""

print('---------------------findall()---------------------------------')

phoneNumberRegex = re.compile(r'\d\d\d\-\d\d\d-\d\d\d\d')
ls = phoneNumberRegex.findall('Cell : 415-555-9999 Work: 212-555-0000')
print('phoneNumberRegex.findall :', ls)

phoneNumberRegex2 = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
ls2 = phoneNumberRegex2.findall('Cell : 415-555-9999  Work: 212-555-0000')
print('phoneNumberRegex2.findall :', ls2)

print('------------------------------------字符分类------------------------------------------')
"""
字符分类

\d  0-9的任何数字
\D  除了0到9的数字以外的任何字符
\w  任何字母、数字或下划线字符（可以认为是匹配“单词”字符）
\W  除了字母、数字和下划线以外的任何字符
\s  空格、制表符或者换行符（可以认为是匹配“空白”字符）
\S  除空格、制表符和换行符以外的任何字符

"""

xmasRegex = re.compile(r'\d+\s\w+')
ls = xmasRegex.findall(
    '12 drummers,'
    '11 pipers,'
    '10 lords,'
    '9 ladies,'
    '8 maids,'
    '7 swans,'
    '6 geese,'
    '5 rings ,'
    '4 birds ,'
    '3 hens,'
    '2 doves,'
    '1 partridge')
print('xmasRegex.findall', ls)

# 插入字符(^)和美元字符($)
# 正则表达式使用插入符号^，表明匹配必须发生在被查找文本开始处

print("-------------------------插入字符和美元字符---------------------------")
beginsWithHello = re.compile(r'^Hello')
mo = beginsWithHello.search('Hello World!')
print('beginsWithHello.search', mo)
print(beginsWithHello.search('He said hello') == None)

# 正则表达式r'\d$' 匹配0到9结束的字符串
endWithNumber = re.compile(r'\d$')
mo = endWithNumber.search('Your number is 42')
print('endWithNumber.search', mo)
print(endWithNumber.search('Your number is forty two') == None)

# 正则表达式r'^\d+$'
wholeStringIsNum = re.compile(r'^\d+$')
flag = wholeStringIsNum.search('1234567890')
print("wholeStringIsNum.search('1234567890') :", flag)
flag2 = wholeStringIsNum.search('123456xyz7890') == None
print("wholeStringIsNum.search('123456xyz7890') == None :", flag2)
flag3 = wholeStringIsNum.search('123 45678890') == None
print("wholeStringIsNum.search('123 45678890') == None :", flag3)

# 通配字符
# .（句点）字符称为通配符，它匹配除了换行之外的所有字符。
atRegex = re.compile(r'.at')
ls = atRegex.findall('The cat in the hat sat on the flat mat.')
print(ls)

# 点-星匹配所有字符
nameRegex = re.compile(r'First Name:(.*) Last Name:(.*)')
mo = nameRegex.search('First Name:A1 Last Name:Sweigart')
print("mo.group(1)", mo.group(1))
print("mo.group(2)", mo.group(2))

# 非贪心模式
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

# 贪心模式
greedRegex = re.compile(r'<.*>')
mo2 = greedRegex.search('<To serve man> for dinner.>')
print(mo2.group())

# 句点字符匹配换行 .* 将匹配除换行外的所有字符
# re.DOTALL 句点字符匹配所有字符，包括换行字符
noNewlineRegex = re.compile('.*')
mo = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.'
                           '\nUphold the law.').group()
print('noNewlineRegex.search:', mo)
newlineRegex = re.compile('.*', re.DOTALL)
mo2 = newlineRegex.search('Serve the public trust. \nProtect the innocent.'
                          '\nUphold the law.').group()
print('newlineRegex.search :', mo2)

# 不区分大小写的匹配
regex1 = re.compile('RoboCop')
regex2 = re.compile('ROBOCOP')
regex3 = re.compile('robOcop')
regex4 = re.compile('RobocOp')

robocop = re.compile(r'robocop', re.I)
mo = robocop.search('RoboCop is part man ,part machine ,all cop.').group()
print(mo)

mo2 = robocop.search('ROBOCOP protects the innocent.').group()
print(mo2)

mo3 = robocop.search('Al,why does your programming book talk about robocop so much ?').group()
print(mo3)

# sub（）方法替换字符串
namesRegex = re.compile(r'Agent \w+')
str = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Sub.')
print(str)

agentNamesRegex = re.compile(r'Agent (\w)\w*')
str = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(str)

# 管理复杂的正则表达式
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?  #area_code
(\s|-|\.)?          #separator
\d{3}               #first 3 digits
(\s|-|\.)           #separator
\d{4}               #last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})?    #extension 
)''', re.VERBOSE)

# 组合使用re.IGNORECASE(忽略大小写)，re.DOTALL（句点字符匹配所有字符，包括换行字符），re.VERBOSE(加备注信息)
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

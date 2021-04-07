# Author: hmchen
# DATE  : 2021/4/6 21:46


import re


def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
        if text[3] != '-':
            return False
        for i in range(4, 7):
            if not text[i].isdecimal():
                return False
        if text[7] != '-':
            return False
        for i in range(8, 12):
            if not text[i].isdecimal():
                return False
        return True


print(isPhoneNumber('414-555-4242'))
print(isPhoneNumber('15972972990'))

message = 'Call me at 415-555-1011 tomorrow, 415-555-999 is my office'
for i in range(len(message)):
    chunk = message[i:i + 12]
    if isPhoneNumber(chunk):
        print("phone number found " + chunk)
print('Done')

# 正则表达式
phoneNumRegex = re.compile(r'\d\d\d\-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found :' + mo.group())

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('mo.group(1)', mo.group(1))
print('mo.group(2)', mo.group(2))
print('mo.group(0)', mo.group(0))
print('mo.group()', mo.group())

areaCode, mainNumber = mo.groups()
print('areaCode', areaCode)
print('mainNumber', mainNumber)

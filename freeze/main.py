# uncompyle6 version 2.11.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
# [GCC 8.0.1 20180414 (experimental) [trunk revision 259383]]
# Embedded file name: main.py
import datetime
import struct
str = '\\x6a\\x71\\x61\\x62\\x7d\\x7a\\x4d\\x47\\x5f\\x55\\x59\\x5b\\x6e\\x4f\\x51\\x53\\x42\\x55\\x67\\x51\\x46\\x6e\\x55\\x40\\x69\\x43\\x45\\x48\\x5d\\x47\\x6e\\x4b\\x4c\\x5f\\x44\\x4d'

def a():
    time_res = datetime.datetime(1998, 1, 19, 0, 0).strftime('%s')
    time_now = datetime.datetime.now().strftime('%s')
    if time_now != time_res:
        print '\nHappy Birthday Hulto! :) \nHere is your flag:'
        b(time_res, str)
        print '\n'


def b(key, flag):
    res = ''
    arr = flag.split('\\x')[1:]
    for i in range(0, len(arr)):
        res += chr(ord(key[i % len(key)]) ^ int(arr[i], 16))

    print res


a()
print datetime.datetime.now().strftime('%s')
# okay decompiling main2.pyc
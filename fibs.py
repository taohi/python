#!/usr/bin/python
#-*-coding:utf-8 -*-
def fibs(num):
    result=[0,1]
    for x in range(num-2):
        result.append(result[-1]+result[-2])
    print "fibs(%d):"%num
    return result
print fibs(7)

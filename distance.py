#!/usr/bin/python
#-*-encoding:utf-8 -*-
#计算地球上两点之间的距离，坐标用经纬度表示。 
#1公里范围误差1米左右 
import math
import sys
def rad (degree):
    '''角度换算数 '''
    radian = degree * math.pi / 180.0
    return radian

def distance (latA,lonA,latB,lonB):
    earth_radius = 6378137.0
    radlatA = rad(latA)
    radlonA = rad(lonA)
    radlatB = rad(latB)
    radlonB = rad(lonB)
    diffLat = radlatA - radlatB
    diffLon = radlonA - radlonB
    distan = 2 * math.asin(math.sqrt(math.pow(math.sin(diffLat/2),2) + math.cos(radlatA)*math.cos(radlatB)*math.pow(math.sin(diffLon/2),2)))
    distan =round(distan * earth_radius ,2)
    return distan


#print distance(float(sys.argv[1]) , float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]))
print distance(30.51372 , 114.42658,30.50929,114.42150)
print distance(30.50929,114.42150,30.5766,111.8457)


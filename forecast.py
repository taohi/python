#!/usr/bin/python
#-*-encoding:utf-8 -*-
import urllib
import re
import PyWapFetion
from xml.etree.ElementTree import parse
print "什么啊"

#PyWapFetion.send("15171456231","eric111235","15171456231","什么啊")
source = urllib.urlopen("http://weather.raychou.com/?/detail/57466/rss")
weather_data = source.read()
f = open("weather.xml","wb")
f.write(weather_data)
f.close()

doc=parse("weather.xml")
for  title in  doc.findall("channel"):
    print title.findtext("title")


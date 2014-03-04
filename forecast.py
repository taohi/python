#!/usr/bin/python
#-*-coding:utf-8 -*-
from PyWapFetion import Fetion
import feedparser
myfetion=Fetion('15171456231','eric111235')
weather_source = "http://weather.raychou.com/?/detail/57466/rss"
d=feedparser.parse(weather_source)
send_content = d.feed.title + "\n明天:" + d.entries[1].description + "\n后天:" +  d.entries[2].description
#print send_content
myfetion.send("15971653106",send_content,sm=True)
myfetion.logout()
print 'forecast success.'

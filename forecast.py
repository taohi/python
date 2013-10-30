#!/usr/bin/python
#-*-coding:utf-8 -*-
import PyWapFetion
import feedparser
weather_source = "http://weather.raychou.com/?/detail/57466/rss"
d=feedparser.parse(weather_source)
send_content = d.feed.title + "\n明天:" + d.entries[1].description + "\n后天:" +  d.entries[2].description
print send_content
PyWapFetion.send("15171456231","eric111235","15171456231",send_content)

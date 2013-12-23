#!/usr/bin/python
import feedparser
source = "http://rss.sina.com.cn/news/allnews/tech.xml"
d =  feedparser.parse(source)

all_news=d.feed.title + d.feed.published+"\n\n"
for single_news in d.entries:
    all_news+= "\r\n"+single_news.title+"\n"
    all_news+= single_news.description+"\n"
    all_news+="-"*50

all_news+="\n"
f=open("data.txt","w")
f.write(all_news)
f.close
print "Call me Big Brother.No thanks.\n"

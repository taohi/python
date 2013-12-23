#!/usr/bin/python
import feedparser
source = "http://rss.sina.com.cn/news/allnews/tech.xml"
d =  feedparser.parse(source)

all_news=d.feed.title + d.feed.published+"\n\n"
for single_news in d.entries:
    all_news+= single_news.title
    all_news+= single_news.description

f=open("news.txt","w+")
f.write(all_news)
f.close
print "Call me Big Brother.No thanks.\n"

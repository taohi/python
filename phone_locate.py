#!/usr/bin/python
#encoding:utf-8
'''利用suds模块，使用web service，查询号码归属地 '''
'''用法:$./phone_locate.py 1517xxxxx'''
import sys
import suds
url = 'http://webservice.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'
client = suds.client.Client(url)
#print client
phone_num=sys.argv[1]
result =client.service.getMobileCodeInfo(phone_num)  
print result
#print client.last_received

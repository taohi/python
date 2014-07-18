#!/usr/bin/python
#encoding:utf-8
'''利用suds模块，使用web service，查询号码归属地 '''
import suds
url = 'http://webservice.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'
client = suds.client.Client(url)
#print client
result =client.service.getMobileCodeInfo(18086111076)  
print result
#print client.last_received

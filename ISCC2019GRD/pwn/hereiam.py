#!/usr/bin/python3
#__author__:TaQini
import requests

# header
s=requests.session()                                     
s.headers['Accept']='text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
s.headers['Accept-Encoding']='gzip, deflate, br'
s.headers['Host']='url'                 
s.headers['Accept-Language']='zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,ko;q=0.6'
s.headers['User-Agent']='zilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'

url = 'http://172.16.100.4:4000/profile'
login = 'http://172.16.100.4:4000/login'
# post

data = {'name':'player26','password':'ZZZZ@@@@'}
def p(d):                          
	res = s.post(url=login,data=d)
	res.encoding = res.apparent_encoding
	return res.text 

def g():
	res = s.get(url=url)
	res.encoding = res.apparent_encoding
	return res.text

p(data)

res = g()

l = res.split('<strong id="team-sig">')

print('hereiam -t ' + l[1][:6])


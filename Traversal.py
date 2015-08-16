#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#遍历当前目录及其子目录下的文件，并按(**kw)函数判断是否输出该文件路径

import os
import time

def Traversal(path, keys, kw):
#1
	# for x in os.listdir(path):
	# 	if os.path.isfile(os.path.join(path, x)):
	# 		if kw(keys, os.path.join(path, x)):
	# 			print(os.path.join(path, x))
	# 	else:
	# 		Traversal(os.path.join(path, x), keys, kw)

#2 time save
	for root, dirs, files in os.walk(path):
		for name in files:
			if kw(keys, os.path.join(root, name)):
				print(os.path.join(root, name))

def Judge(key, path):
	return True

path = os.path.split(os.path.abspath('.'))
key = ()

start = time.time()
Traversal(path[0], key, Judge)
end = time.time()
print(end - start)

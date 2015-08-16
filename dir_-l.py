# -*- coding: utf-8 -*-
#利用os模块编写一个能实现dir -l输出的程序。
#参考作者答案得知不需要打印出权限，但是，如何打印出权限？

from datetime import datetime
import os

f = os.path.abspath('.')

print('total', 4 * len(os.listdir(os.getcwd())))

for x in os.listdir(f):
	p = os.path.abspath(x)
	print(os.path.getsize(p), datetime.fromtimestamp(os.path.getmtime(p)).strftime('%m月 %d %H:%M'), x)

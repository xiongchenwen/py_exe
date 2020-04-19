#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import os.path

# ui文件所在的路径

dir = './'

#列出目录下的所有ui文件

def listUiFile():
	list =[]
	files = os.listdir(dir)
	for filename in files:
		#print(dir+os.sep+f)
		#print(filename)
		if os.path.splitext(filename)[1] == '.ui':
			list.append(filename)
	return list

#把扩展名为.ui的文件转换成.py的文件
def transPyFile(filename):
	return os.path.splitext(filename)[0]+'.py'

#调用系统命令把ui文件转换为python文件
def runMain():
	list = listUiFile()
	for uifile in list:
		pyfile = transPyFile(uifile)
		cmd = 'pyuic5 -o {pyfile} {uifile}'.format(pyfile=pyfile,uifile=uifile)
		#print(cmd)
		os.system(cmd)

if __name__ == '__main__':
	runMain()
#try:
#<语句>        #运行别的代码
#except <名字>：
#<语句>        #如果在try部份引发了'name'异常
#except <名字>，<数据>:
#<语句>        #如果引发了'name'异常，获得附加的数据
#else:
#<语句>        #如果没有异常发生


#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print ("Error: 没有找到文件或读取文件失败")
else:
    print ("内容写入文件成功")
    fh.close()
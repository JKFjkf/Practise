#idle中按F5可以运行代码
#引入外部模块 import xxx
#random模块，randint(开始数，结束数) 产生整数随机数
import random
import sys
import os
secret = random.randint(1,10)
temp = input("请输入一个数字\n")
#print(type(temp))#<class 'str'> 类型判断
#print(isinstance(temp,int))#False
#异常处理 try except finally 没有catch函数
try:
  guess = int(temp)
except:
  print("输入的不是数字，程序终止了")#注释内容不能在逻辑代码块里独立一行进行
  os._exit(0)#os._exit() 用于在线程中退出,sys.exit()用于在主线程中退出，exit(0)#终止退出程序，会关闭窗口
count = 0;
while guess != secret: #猜错的时候才进入循环条件
  if count == 0 and guess > secret:
    print("猜大了")
  if count == 0 and guess < secret:
    print("猜小了")
  temp = input("请重新输入数字\n") #需要在判断之前让用户输入，否则猜对了就直接退出了
  try:
    guess = int(temp)
  except (ZeroDivisionError,Exception):
    print("输入的不是数字，请重新输入")
    print(ZeroDivisionError,":",Exception)
  count += 1 #不能使用count++这种方式
  if count > 2:
    print("猜错4次自动退出了")
    break #退出循环
  if guess == secret:
    print("恭喜，你猜对了")
    print("猜对了也就那样")
  else:
    if guess > secret:
      print("猜大了")
    else:
      print("猜小了")
print("游戏结束")


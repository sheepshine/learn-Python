#数字求和
#coding=utf-8
# num1=input("请输入第一个数字")
# num2=input("请输入第二个数字")
# sum=float(num1)+float(num2);
# print("数字{0}和{1}相加的结果为：{2}".format(num2,num1,sum))

# #判断字符串是否为数字

# def is_number(s):
# 	try:
# 		float(s)
# 		return True
# 	except ValueError:
# 		pass

# 	try:
# 		import unicodedata
# 		unicodedata.numeric(s)
# 		return True
# 	except (TypeError,ValueError):
# 		pass
# 	return False

# #测试字符串和数字
# print(is_number('foo'))
# print(is_number('1'))

# while True:
# 	s=input("Enter something:")
# 	if s=='quit':
# 		break
# 	if len(s)<3:
# 		continue
# 	print('Input is of sufficient length')

# def say(message,times=1):
# 	print(message*times)
# say("Hello")
# say("World",5)
# def func(a,b=5,c=10):
# 	'''example out function.

# 	it is a test of function argument'''
# 	print('a is',a,'and b is',b,'and c is',c)

# func(10)
# func(10,b=20)
# func(c=30,a=20)
# print(func.__doc__)

import sys,use_name

print('The command line arguments are:')
for i in sys.argv:
	print(i)

print('\n\nThe PYTHONPATH is',sys.path,'n')
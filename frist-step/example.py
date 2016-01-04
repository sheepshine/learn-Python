#数字求和
#coding=utf-8
num1=input("请输入第一个数字")
num2=input("请输入第二个数字")
sum=float(num1)+float(num2);
print("数字{0}和{1}相加的结果为：{2}".format(num2,num1,sum))

#判断字符串是否为数字

def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		pass

	try:
		import unicodedata
		unicodedata.numeric(s)
		return True
	except (TypeError,ValueError):
		pass
	return False

#测试字符串和数字
print(is_number('foo'))
print(is_number('1'))
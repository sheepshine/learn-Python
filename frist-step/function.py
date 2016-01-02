def hello():
	print("Hello World")

hello();

def area(width,height):
	return width*height

def print_welcome(name):
	print("Welcome",name)

print_welcome("sheepshine")
w=4
h=5
print(area(w,h))

#关键字参数
def parrot(voltage,state='a stiff',action='voom',type='Norwegian Blue'):
	print("--this parrot would't",action,end="")
	print("if you put",voltage,"volts through it.")
	print("--Lovely plumage,the",type)
	print("--It's",state,"!")

parrot(1000)
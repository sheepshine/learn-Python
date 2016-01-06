class Person:
	population=0;
	def __init__(self,name):
		self.name=name
		print('Intializing %s' % self.name)
		Person.population+=1
	def __del__(self):
		print('%s syas bye' % self.name)
		Person.population-=1
		if Person.population==0:
			print("I am the last one.")
		else:
			print("There are still %d people left" % Person.population)
	def sayHi(self):
		print('Hello.how are you?',self.name)
	def howMany(self):
		if Person.population==1:
			print("I am the only person here.")
		else:
			print("We hava %d person here" % Person.population)
p=Person("hehe")
p.sayHi()

p2=Person("haha")
p2.sayHi()
p2.howMany()
p.howMany()
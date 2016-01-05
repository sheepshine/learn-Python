class SchoolMember:
	def __init__(self,name,age):
		self.name=name
		self.age=age
		print("初始化学校成员：%s" % self.name)
	def tell(self):
		print("名字:'%s' 年龄:'%s'" % (self.name,self.age))
class Teacher(SchoolMember):
	def __init__(self,name,age,salary):
		SchoolMember.__init__(self,name,age)
		self.salary=salary
		print("初始化老师：%s" % self.name)
	def tell(self):
		SchoolMember.tell(self)
		print("工资：%d" % self.salary)
class Student(SchoolMember):
	def __init__(self,name,age,marks):
		SchoolMember.__init__(self,name,age)
		self.marks=marks
		print("初始化学生：%s" % self.name)
	def tell(self):
		SchoolMember.tell(self)
		print("成绩：%d" % self.marks)
		
t=Teacher('陈老师',40,30000)
s=Student('小调',22,80)
members=[t,s]
for member in members:
	member.tell()
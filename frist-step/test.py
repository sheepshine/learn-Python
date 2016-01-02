print("hello, Python!");
a,b,c,d=20,5.5,True,4+3j
print(type(a),type(b),type(c),type(d))
s='Yes,he doesn\'t';
print(s,type(s),len(s));
print(r'c:\some\name');
print('str'+'ing','my'*3);
word='Python';
print(word[0],word[5]);
print(word[-1],word[-6]);
word1='ilovepython';
print(word1[1:5],word1[5:],word1[-10:6]);
#Sets
student={'Tom','Jim','Marry','Tom'};
print(student);
isTom='Tom' in student;
print(isTom);
#Dictionaries
tel={'Jack':1157,'Tom':1320,'Rose':1186,'Adobe':1578};
print(tel);
print(tel['Jack']);
del tel['Tom'];
sorted(tel.keys())
print(tel);
dic={x:x**2 for x in (2,4,6)};
print(dic)
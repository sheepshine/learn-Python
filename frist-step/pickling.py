#coding:utf-8
import pickle as p
shoplistfile="shoplist.data"
shoplist=['apple','mango','carrot']
f=open(shoplistfile,'wb')
p.dump(shoplist,f)
f.close()
del shoplist
f=open(shoplistfile)
#编码问题
storelist=p.load(f)
print(storelist)
#list creation,indexing,negative indexing,deleting,,
l1=[50,20,80,10,60,40]
print (l1)
print(l1[2])
print(l1[-1])
print(l1[-4])
l2=[7.6,50,5+3j,"ace",True]
print(l2[-3])
print(l2[-4])
print(l2[-1])
del l1[1],l2[-3]
print(l1)
print(l2)
for i in l1:
    print(i,end=' ')
j=0
while j<1:
   print(l1,end=' ')
   j+=1


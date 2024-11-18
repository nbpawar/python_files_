#w.a.p to print the first n even natural no in reverse order 
n=int(input("enter the no"))
r1=range(n*2,1,-2)
for e in r1:
  print(e, end=' ')

#same but in short then square also
for e in range((int(input("enter the no")))*2,1,-2):
    print (e*e,end=' ')
#wrint a program to give a variable from user and count the no of 'a' in the given variable by using the for loop#
s=input("Enter the string")
count=0
for e in s:
    if e=='a':
        count +=1

print("total no 0f 'a' occurance in a string",count)

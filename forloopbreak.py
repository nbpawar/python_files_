#print all the character of a string, but stop printing if 'r' appered in the sequence if all the character successfully printed the print message "all the characters are processed!"
x=input ('enter a string')
for i in x:
    if i == 'r':
        break
    print (i,end='')

else:
    print("all the characters are printed ") 
#write a program to ask user an even numer at most 3 times.if the user failed tp enter even no in all the chances then he has lost the game. if user enter even no then no more chanceds to enter no will be given and announced to  he is the winner.

i=1
while i<=3:
    a=int(input('enter a even no'))
    if a%2==0:
        break
    i+=1
if i==4:
    print ('you lose the game')
else:
    print ('you won the game')


print()
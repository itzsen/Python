import random
import sys

randnumber=random.randint(1,10)

#print(randnumber)

print('What is your name')
name=input()
print('Hi',name,'Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess')



for i in range (0,5):
    number=int(input())
    if number == randnumber:
        print('Good job',name,'you guessed the number in',i+1,'tries')
        sys.exit()
    elif number >randnumber:
        print('number too high')
        i=i+1
    elif number < randnumber:
        print('number too low')
        i=i+1

print('Sorry',name,'you have exhausted your 5 tries')
print('my guess is',randnumber)


    








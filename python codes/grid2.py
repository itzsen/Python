Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:59:38) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> random.randint(1,10)
8
>>> random.randint(1,10)
8
>>> random.randint(1,10)
8
>>> random.randint(1,10)
8
>>> random.randint(1,10)
8
>>> random.randint(1,10)
7
>>> random.randint(1,10)
9
>>> from random import *
>>> randint(1,10)
6
>>> randint(1,10)
10
>>> sys.exit()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    sys.exit()
NameError: name 'sys' is not defined
>>> import sys
>>> sys.exit()
>>> sys.exit(0)
>>> import math
>>> import pyperclip
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    import pyperclip
ModuleNotFoundError: No module named 'pyperclip'
>>> import pyperclip
>>> pyperclip.copy(hello)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    pyperclip.copy(hello)
NameError: name 'hello' is not defined
>>> pyperclip.copy('hello')
>>> pyperclip.paste('hello')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    pyperclip.paste('hello')
TypeError: paste_osx_pbcopy() takes 0 positional arguments but 1 was given
>>> pyperclip.paste()
'hello'
>>> pwd
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    pwd
NameError: name 'pwd' is not defined
>>> ls
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    ls
NameError: name 'ls' is not defined
>>> dir
<built-in function dir>
>>> 
====== RESTART: /Users/senthilnatarajan/Dropbox/Programming/fnHello.py ======
Howdy
how are you?
wazzup
Howdy
how are you?
wazzup
Howdy
how are you?
wazzup
>>> print('Hello has'+Str(len('Hello'))+' letters in it')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print('Hello has'+Str(len('Hello'))+' letters in it')
NameError: name 'Str' is not defined
>>> print('Hello has'+str(len('Hello'))+' letters in it')
Hello has5 letters in it
>>> print('Hello has'+str(len('Hello'))+' letters in it')
Hello has5 letters in it

>>> print ('cat','mouse')
cat mouse
>>> print('Hello has',Str(len('Hello')),' letters in it')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print('Hello has',Str(len('Hello')),' letters in it')
NameError: name 'Str' is not defined
>>> print('Hello has',str(len('Hello')),' letters in it')
Hello has 5  letters in it
>>> print('Hello has',str(len('Hello')),'letters in it')
Hello has 5 letters in it
>>> print ('cat','mouse',sep='ABC')
catABCmouse
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/fnDIV42by.py ==
42.0
1 None
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/fnDIV42by.py ==
1 42.0
2 42.0
3 42.0
0 42.0
5 42.0
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/fnDIV42by.py ==
1 42.0
2 21.0
3 14.0
Traceback (most recent call last):
  File "/Users/senthilnatarajan/Dropbox/Programming/Python/fnDIV42by.py", line 7, in <module>
    print ('0',Div42by(0))
  File "/Users/senthilnatarajan/Dropbox/Programming/Python/fnDIV42by.py", line 2, in Div42by
    return 42/number
ZeroDivisionError: division by zero
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/fnDIV42by.py ==
1 42.0
2 21.0
3 14.0
Error: You tried to divide by Zero
0 None
5 8.4
>>> 
= RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/try_Except.py =
How many cats?
6
thats a lot of cats
>>> 
= RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/try_Except.py =
How many cats?
2
not too many cats
>>> 
= RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/try_Except.py =
How many cats?
six
Traceback (most recent call last):
  File "/Users/senthilnatarajan/Dropbox/Programming/Python/try_Except.py", line 5, in <module>
    if int(x) >= 4:
ValueError: invalid literal for int() with base 10: 'six'
>>> 
= RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/try_Except.py =
How many cats?
six
Error - You have entered alphanumeric characters
>>> 
= RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/try_Except.py =
How many cats?
-1
not too many cats
>>> 
= RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/try_Except.py =
How many cats?
-5
Error - Negative number
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
What is your name
Senthil
Hi Senthil Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
1
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
What is your name
sen
Hi sen Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
1
Good job sen you guessed the number in 1 tries
Good job sen you guessed the number in 2 tries
Good job sen you guessed the number in 3 tries
Good job sen you guessed the number in 4 tries
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
What is your name
sen
Hi sen Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
1
number too low, try again please?
number too low, try again please?
number too low, try again please?
number too low, try again please?
>>> system.exit()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    system.exit()
NameError: name 'system' is not defined
>>> system.out()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    system.out()
NameError: name 'system' is not defined
>>> sys.exit()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    sys.exit()
NameError: name 'sys' is not defined
>>> import system
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    import system
ModuleNotFoundError: No module named 'system'
>>> import sys
>>> sys.exit()
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
What is your name
sen
Hi sen Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
1
number too low, try again please?
2
number too low, try again please?
3
number too low, try again please?
4
number too low, try again please?
5
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
What is your name
Sen
Hi Sen Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
3
number too low, try again please?
6
number too low, try again please?
8
number too low, try again please?
9
Good job Sen you guessed the number in 4 tries
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
What is your name
Senthil
Hi Senthil Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
5
Good job Senthil you guessed the number in 1 tries
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
What is your name
23
Hi 23 Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
six
Traceback (most recent call last):
  File "/Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py", line 10, in <module>
    number=int(input())
ValueError: invalid literal for int() with base 10: 'six'
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
What is your name
Senthil
Hi Senthil Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
7
number too low, try again please?
9
number too low, try again please?
10
number too low, try again please?
8
number too low, try again please?
1
Sorry Senthil you have exhausted your 5 tries
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
What is your name
Senthil
Hi Senthil Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
10
number too low, try again please?
1
number too low, try again please?
2
number too low, try again please?
3
Good job Senthil you guessed the number in 4 tries
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
What is your name
Senthil
Hi Senthil Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
3
number too low, try again please?
7
number too high, try again please?
6
number too high, try again please?
8
number too high, try again please?
9
Sorry Senthil you have exhausted your 5 tries
my guess is 5
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
What is your name
senthil
Hi senthil Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
4
number too low, try again please?
5
number too low, try again please?
7
number too high, try again please?
6
number too high, try again please?
9
Sorry senthil you have exhausted your 5 tries
my guess is 10
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
What is your name
Senthil
Hi Senthil Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
5
number too high, try again please?
3
number too high, try again please?
2
number too high, try again please?
1
number too high, try again please?
4
Sorry Senthil you have exhausted your 5 tries
my guess is 8
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
What is your name
Senthil
Hi Senthil Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
5
number too low, try again please?
7
Good job Senthil you guessed the number in 2 tries
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
What is your name
Senthil
Hi Senthil Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
1
number too low, try again please?
3
number too low, try again please?
6
number too low, try again please?
8
number too high, try again please?
7
Sorry Senthil you have exhausted your 5 tries
my guess is 7
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
What is your name
Senthil
Hi Senthil Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
5
number too high, try again please?
4
number too high, try again please?
3
number too high, try again please?
2
number too high, try again please?
1
Sorry Senthil you have exhausted your 5 tries
my guess is 1
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
3
What is your name
Senthil
Hi Senthil Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
3
Good job Senthil you guessed the number in 1 tries
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
1
What is your name
Sen
Hi Sen Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
3
number too high, try again please?
1
Good job Sen you guessed the number in 2 tries
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
1
What is your name
S
Hi S Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
5
number too high, try again please?
4
number too high, try again please?
2
number too high, try again please?
1
Good job S you guessed the number in 4 tries
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
2
What is your name
Sen
Hi Sen Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
6
number too high, try again please?
5
number too high, try again please?
4
number too high, try again please?
3
number too high, try again please?
2
Sorry Sen you have exhausted your 5 tries
my guess is 2
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
6
What is your name
Sen
Hi Sen Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
2
number too low, try again please?
3
number too low, try again please?
4
number too low, try again please?
5
number too low, try again please?
6
Good job Sen you guessed the number in 4 tries
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
5
What is your name
Sen
Hi Sen Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
1
number too low, try again please?
1
number too low, try again please?
1
number too low, try again please?
1
number too low, try again please?
1
number too low, try again please?
1
Sorry Sen you have exhausted your 5 tries
my guess is 5
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
9
What is your name
Sen
Hi Sen Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
7
number too low, try again please?
8
number too low, try again please?
9
Good job Sen you guessed the number in 3 tries
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
6
What is your name
4
Hi 4 Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
4
number too low, try again please?
4
number too low, try again please?
4
number too low, try again please?
4
number too low, try again please?
6
Sorry 4 you have exhausted your 5 tries
my guess is 6
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
4
What is your name
Senthil
Hi Senthil Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
3
number too low, try again please?
3
number too low, try again please?
3
number too low, try again please?
3
number too low, try again please?
3
number too low, try again please?
3
Sorry Senthil you have exhausted your 5 tries
my guess is 4
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
7
What is your name
Senthil
Hi Senthil Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
1
number too low, try again please?
1
number too low, try again please?
1
number too low, try again please?
1
number too low, try again please?
1
Sorry Senthil you have exhausted your 5 tries
my guess is 7
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
2
What is your name
Senthil
Hi Senthil Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
4
number too high, try again please?
4
number too high, try again please?
4
number too high, try again please?
4
number too high, try again please?
Sorry Senthil you have exhausted your 5 tries
my guess is 2
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
5
What is your name
4
Hi 4 Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
4
number too low, try again please?
4
number too low, try again please?
4
number too low, try again please?
4
number too low, try again please?
4
number too low, try again please?
Sorry 4 you have exhausted your 5 tries
my guess is 5
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
5
What is your name
Senthil
Hi Senthil Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
4
number too low
4
number too low
4
number too low
4
number too low
4
number too low
Sorry Senthil you have exhausted your 5 tries
my guess is 5
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
1
What is your name
Senthil
Hi Senthil Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
2
number too high
2
number too high
2
number too high
2
number too high
1
Good job Senthil you guessed the number in 4 tries
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
10
What is your name
Senthil
Hi Senthil Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
10
Good job Senthil you guessed the number in 1 tries
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
10
What is your name
Senthil
Hi Senthil Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
9
number too low
10
Good job Senthil you guessed the number in 2 tries
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
8
What is your name
Senthil
Hi Senthil Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
8
Good job Senthil you guessed the number in 1 tries
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
7
What is your name
Senthil
Hi Senthil Welcome to my guessing game. I am thinking of a number between 1 to 10. Take a guess
8
number too high
8
number too high
8
number too high
8
number too high
7
Good job Senthil you guessed the number in 5 tries
>>> 
== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py ==
What is your name
Traceback (most recent call last):
  File "/Users/senthilnatarajan/Dropbox/Programming/Python/guessGame.py", line 9, in <module>
    name=input()
KeyboardInterrupt
>>> 
>>> 
>>> 
>>> 
>>> 
>>> ['cat','bat','rat']
['cat', 'bat', 'rat']
>>>  spam= ['cat','bat','rat']
SyntaxError: unexpected indent
>>> spam= ['cat','bat','rat']
>>> spam
['cat', 'bat', 'rat']
>>> spam[0]
'cat'
>>> spam[2]
'rat'
>>> spam[-1]
'rat'
>>> spam[3]
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    spam[3]
IndexError: list index out of range
>>> spam[1,2]
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    spam[1,2]
TypeError: list indices must be integers or slices, not tuple
>>>  spam= [['cat','bat','rat'],['a','b','c'],['1','2','3']
	    
SyntaxError: unexpected indent
>>> spam= [['cat','bat','rat'],['a','b','c'],['1','2','3']]
	    
>>> spam[0]
	    
['cat', 'bat', 'rat']
>>> spam[1]
	    
['a', 'b', 'c']
>>> spam[2]
	    
['1', '2', '3']
>>> spam[3]
	    
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    spam[3]
IndexError: list index out of range
>>> spam[-1]
	    
['1', '2', '3']
>>> spam[-2]
	    
['a', 'b', 'c']
>>> spam[-3]
	    
['cat', 'bat', 'rat']
>>> spam[-4]
	    
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    spam[-4]
IndexError: list index out of range
>>> spam[1,2]
	    
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    spam[1,2]
TypeError: list indices must be integers or slices, not tuple
>>> spam[1][0]
	    
'a'
>>> spam
	    
[['cat', 'bat', 'rat'], ['a', 'b', 'c'], ['1', '2', '3']]
>>> spam[0][1]
	    
'bat'
>>> spam[-3][-3]
	    
'cat'
>>> spam[0][1]
	    
'bat'
>>> spam[0][0]
	    
'cat'
>>> spam[-3][-3]
	    
'cat'
>>> spam
	    
[['cat', 'bat', 'rat'], ['a', 'b', 'c'], ['1', '2', '3']]
>>> spam[0:3]
	    
[['cat', 'bat', 'rat'], ['a', 'b', 'c'], ['1', '2', '3']]
>>> spam[0:1]
	    
[['cat', 'bat', 'rat']]
>>> spam=['cat', 'bat', 'rat']
	    
>>> spam[0:2]
	    
['cat', 'bat']
>>> spam=[1,2,3]
	    
>>> spam[1]='Hello'
	    
>>> spam
	    
[1, 'Hello', 3]
>>> spam[1:5]=[5,5,5,5,5,5,5,5,5,5,5]
	    
>>> spam
	    
[1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
>>> spam[:4]
	    
[1, 5, 5, 5]
>>> spam[5:]
	    
[5, 5, 5, 5, 5, 5, 5]
>>> spam=[['cat', 'bat', 'rat'], ['a', 'b', 'c'], ['1', '2', '3']]
	    
>>> spam[3:]
	    
[]
>>> spam[1:]
	    
[['a', 'b', 'c'], ['1', '2', '3']]
>>> spam[1:][1:]
	    
[['1', '2', '3']]
>>> spam[1:][1:][1:]
	    
[]
>>> spam[1:][1:]
	    
[['1', '2', '3']]
>>> spam[1:][1:][0]
	    
['1', '2', '3']
>>> spam[1:][1:][0]
	    
['1', '2', '3']
>>> spam[1:][1:]
	    
[['1', '2', '3']]
>>> spam[1:][1:][0:1]
	    
[['1', '2', '3']]
>>> spam[1:][1:2]
	    
[['1', '2', '3']]
>>> spam[1:][0:1]
	    
[['a', 'b', 'c']]
>>> spam
	    
[['cat', 'bat', 'rat'], ['a', 'b', 'c'], ['1', '2', '3']]
>>> spam[1:][0:1]
	    
[['a', 'b', 'c']]
>>> spam
	    
[['cat', 'bat', 'rat'], ['a', 'b', 'c'], ['1', '2', '3']]
>>> len(spam)
	    
3
>>> spam=[1,2,3,4,5,6]
	    
>>> len (spam)
	    
6
>>> [1,2,3,4,5]+[1,2,3,4,5]
	    
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
>>> [1,2,3,4,5]-[1,2,3,4,5]
	    
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    [1,2,3,4,5]-[1,2,3,4,5]
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> [1,2,3]+['a',2,'b']
	    
[1, 2, 3, 'a', 2, 'b']
>>> del spam[2:]
	    
>>> spam
	    
[1, 2]
>>> [1, 2]
	    
[1, 2]

>>> list['hello']
	    
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    list['hello']
TypeError: 'type' object is not subscriptable
>>> list('hello')
	    
['h', 'e', 'l', 'l', 'o']
>>> list ('this is my list')
	    
['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'm', 'y', ' ', 'l', 'i', 's', 't']
>>> spam='this is my list'
	    
>>> 'i' in list(spam)
	    
True
>>> 'z' in list(spam)
	    
False
>>> list(spam)
	    
['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'm', 'y', ' ', 'l', 'i', 's', 't']
>>> 'howdy' in ['a','howdy']
	    
True
>>> 'howdy' in ['a','howdy']
	    
True
>>> 'howdya' in ['a','howdy']
	    
False
>>> 'howdya' not in ['a','howdy']
	    
True
>>> 'howdy' not in ['a','howdy']
	    
False
>>> 
	    
>>> 
	    
>>> for i in range(4):
	    print(i)

0
1
2
3
>>> range(4)
	    
range(0, 4)
>>> list(range(4))
	    
[0, 1, 2, 3]
>>> 
	    
>>> 
	    
>>> for i in [0,1,2,3]:
	    print(i)

0
1
2
3
>>> list(range(0,100,2))
	    
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> 
	    
>>> 
	    
>>> 
	    
>>> groceries = ['cheese','tomato','onion','milk']
	    
>>> for i in range(len(groceries)):
	    print ('Index '+str(i)+'in groceries is '+groceries[i])

	    
Index 0in groceries is cheese
Index 1in groceries is tomato
Index 2in groceries is onion
Index 3in groceries is milk
>>> for i in range(len(groceries)):
	    print ('Index '+str(i)+' in groceries is '+groceries[i])

	    
Index 0 in groceries is cheese
Index 1 in groceries is tomato
Index 2 in groceries is onion
Index 3 in groceries is milk
>>> 
	    
>>> 
	    
>>> 
	    
>>> cat=['a','b','c']
	    
>>> a,b,c=cat
	    
>>> a
	    
'a'
>>> b
	    
'b'
>>> c
	    
'c'
>>> a,a,a=cat
	    
>>> a
	    
'c'
>>> a
	    
'c'
>>> a
	    
'c'
>>> b
	    
'b'
>>> c
	    
'c'
>>> a,b,c=cat
	    
>>> a,b,c=c,b,a
	    
>>> a
	    
'c'
>>> b
	    
'b'
>>> c
	    
'a'
>>> a,b,c=c,b,a
	    
>>> a
	    
'a'
>>> b
	    
'b'
>>> c
	    
'c'
>>> spam = [1,2,3,4,5]
	    
>>> spam.index(3)
	    
2
>>> spam.index(5)
	    
4
>>> spam
	    
[1, 2, 3, 4, 5]
>>> spam.append('moose')
	    
>>> spam
	    
[1, 2, 3, 4, 5, 'moose']
>>> spam.append('moose')
	    
>>> spam.append('moose')
	    
>>> spam
	    
[1, 2, 3, 4, 5, 'moose', 'moose', 'moose']
>>> spam.insert(0,'test')
	    
>>> spam
	    
['test', 1, 2, 3, 4, 5, 'moose', 'moose', 'moose']
>>> spam.remove(0)
	    
Traceback (most recent call last):
  File "<pyshell#178>", line 1, in <module>
    spam.remove(0)
ValueError: list.remove(x): x not in list
>>> spam.remove('test')
	    
>>> spam
	    
[1, 2, 3, 4, 5, 'moose', 'moose', 'moose']
>>> spam.remove('moose')
	    
>>> spam
	    
[1, 2, 3, 4, 5, 'moose', 'moose']
>>> spam.remove('moose')
	    
>>> spam.remove('moose')
	    
>>> spam.remove('moose')
	    
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    spam.remove('moose')
ValueError: list.remove(x): x not in list
>>> spam
	    
[1, 2, 3, 4, 5]
>>> spam=[1, 2, 3, 4, 5, 'moose', 'moose']
	    
>>> spam
	    
[1, 2, 3, 4, 5, 'moose', 'moose']
>>> spam=spam.remove('moose')
	    
>>> spam
	    
>>> spam =[1, 2, 3, 4, 5, 'moose', 'moose']
	    
>>> spam.sort()
	    
Traceback (most recent call last):
  File "<pyshell#192>", line 1, in <module>
    spam.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> spam.sort(*)
	    
SyntaxError: invalid syntax
>>> spam=[1,5,2,-1,5,6,1,3,2]
	    
>>> spam.sort()
	    
>>> spam
	    
[-1, 1, 1, 2, 2, 3, 5, 5, 6]
>>> spam=['ants','cats','b']
	    
>>> spam.sort()
	    
>>> spam
	    
['ants', 'b', 'cats']
>>> spam.sort(reverse=true)
	    
Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    spam.sort(reverse=true)
NameError: name 'true' is not defined
>>> spam.sort(reverse=True)
	    
>>> spam
	    
['cats', 'b', 'ants']
>>> spam=['1','2','3','4','5','moose','moose']
	    
>>> spam.sort()
	    
>>> spam
	    
['1', '2', '3', '4', '5', 'moose', 'moose']
>>> 
	    
>>> 
	    
>>> 
	    
>>> spam
	    
Traceback (most recent call last):
  File "<pyshell#209>", line 1, in <module>
    pam
NameError: name 'pam' is not defined
>>> spam
	    
['1', '2', '3', '4', '5', 'moose', 'moose']
>>> 
	    
>>> 
	    
>>> 
	    
>>> cheese = spam
	    
>>> cheese[1]='hello'
	    
>>> cheese
	    
['1', 'hello', '3', '4', '5', 'moose', 'moose']
>>> spam
	    
['1', 'hello', '3', '4', '5', 'moose', 'moose']
>>> 
	    
>>> 
	    
>>> 
	    
>>> spam=42
	    
>>> cheese=spam
	    
>>> spam=100
	    
>>> spam
	    
100
>>> cheese
	    
42
>>> 
	    
>>> spam=[1,2,3]
	    
>>> spam
	    
[1, 2, 3]
>>> spam
	    
[1, 2, 3]
>>> import copy
	    
>>> cheese=copy.deepcopy(spam)
	    
>>> cheese
	    
[1, 2, 3]
>>> cheese[1]='S'
	    
>>> cheese
	    
[1, 'S', 3]
>>> spam
	    
[1, 2, 3]
>>> 
	    
>>> 
	    
>>> name=senthil
	    
Traceback (most recent call last):
  File "<pyshell#238>", line 1, in <module>
    name=senthil
NameError: name 'senthil' is not defined
>>> name='senthil'
	    
>>> list(name)
	    
['s', 'e', 'n', 't', 'h', 'i', 'l']
>>> spam=list(name)
	    
>>> newname=copy.deepcopy(spam)
	    
>>> newname
	    
['s', 'e', 'n', 't', 'h', 'i', 'l']
>>> newname.sort(reverse=True)
	    
>>> newname
	    
['t', 's', 'n', 'l', 'i', 'h', 'e']
>>> newname=copy.deepcopy(spam)
	    
>>> newname
	    
['s', 'e', 'n', 't', 'h', 'i', 'l']
>>> newname.sort()
	    
>>> newname
	    
['e', 'h', 'i', 'l', 'n', 's', 't']
>>> str(newname)
	    
"['e', 'h', 'i', 'l', 'n', 's', 't']"
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/list.py ====
['apples', 'bananas', 'tofu', 'cats']
['apples', 'bananas', 'tofu', 'cats']
['apples', 'bananas', 'tofu', 'cats']
['apples', 'bananas', 'tofu', 'cats']
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/list.py ====
0
1
2
3
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/list.py ====
apples
bananas
tofu
cats
>>> print('senthil',end=")
	  
SyntaxError: EOL while scanning string literal
>>> grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
	  
>>> 
	  
>>> 
	  
>>> 
	  
>>> for i in range(6):
	  for x in range(len(grid)):
	  print(grid[x][i],end=")
		
SyntaxError: expected an indented block
>>> print(")
	  
SyntaxError: EOL while scanning string literal
>>> print('')
	  

>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====
.
.
O
O
.
O
O
.
.
.
O
O
O
O
O
O
O
.
.
O
O
O
O
O
O
O
.
.
.
O
O
O
O
O
.
.
.
.
.
O
O
O
.
.
.
.
.
.
.
O
.
.
.
.
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====
..OO.OO...OOOOOOO..OOOOOOO...OOOOO.....OOO.......O....
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====
.
.
O
O
.
O
O
.
.
.
O
O
O
O
O
O
O
.
.
O
O
O
O
O
O
O
.
.
.
O
O
O
O
O
.
.
.
.
.
O
O
O
.
.
.
.
.
.
.
O
.
.
.
.
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====
..OO.OO...OOOOOOO..OOOOOOO...OOOOO.....OOO.......O....
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====
..OO.OO...OOOOOOO..OOOOOOO...OOOOO.....OOO.......O....
>>> grid
	  
[['.', '.', '.', '.', '.', '.'], ['.', 'O', 'O', '.', '.', '.'], ['O', 'O', 'O', 'O', '.', '.'], ['O', 'O', 'O', 'O', 'O', '.'], ['.', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', '.'], ['O', 'O', 'O', 'O', '.', '.'], ['.', 'O', 'O', '.', '.', '.'], ['.', '.', '.', '.', '.', '.']]
>>> 
	  
>>> 
	  
>>> len(grid)
	  
9
>>> grid[1][0]
	  
'.'
>>> grid[2][0]
	  
'O'
>>> grid[0][0]
	  
'.'
>>> grid[0][0]
	  
'.'
>>> grid[0][1]
	  
'.'
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====
......Traceback (most recent call last):
  File "/Users/senthilnatarajan/Dropbox/Programming/Python/grid.py", line 14, in <module>
    print(grid[i][x],end='')
IndexError: list index out of range
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====
..OO.OO...OOOOOOO..OOOOOOO...OOOOO.....OOO.......O....
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====
.
.
O
O
.
O
O
.
.
.
O
O
O
O
O
O
O
.
.
O
O
O
O
O
O
O
.
.
.
O
O
O
O
O
.
.
.
.
.
O
O
O
.
.
.
.
.
.
.
O
.
.
.
.
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====
..OO.OO...OOOOOOO..OOOOOOO...OOOOO.....OOO.......O....
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====
. 
. 
O 
O 
. 
O 
O 
. 
. 
. 
O 
O 
O 
O 
O 
O 
O 
. 
. 
O 
O 
O 
O 
O 
O 
O 
. 
. 
. 
O 
O 
O 
O 
O 
. 
. 
. 
. 
. 
O 
O 
O 
. 
. 
. 
. 
. 
. 
. 
O 
. 
. 
. 
. 
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====
.
.
O
O
.
O
O
.
.
.
O
O
O
O
O
O
O
.
.
O
O
O
O
O
O
O
.
.
.
O
O
O
O
O
.
.
.
.
.
O
O
O
.
.
.
.
.
.
.
O
.
.
.
.
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====
..OO.OO...OOOOOOO..OOOOOOO...OOOOO.....OOO.......O.... 
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====
..OO.OO...OOOOOOO..OOOOOOO...OOOOO.....OOO.......O....A
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====
.A
.A
OA
OA
.A
OA
OA
.A
.A
.A
OA
OA
OA
OA
OA
OA
OA
.A
.A
OA
OA
OA
OA
OA
OA
OA
.A
.A
.A
OA
OA
OA
OA
OA
.A
.A
.A
.A
.A
OA
OA
OA
.A
.A
.A
.A
.A
.A
.A
OA
.A
.A
.A
.A
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====
. . O O . O O . . . O O O O O O O . . O O O O O O O . . . O O O O O . . . . . O O O . . . . . . . O . . . . 
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====
.  .  O  O  .  O  O  .  .  .  O  O  O  O  O  O  O  .  .  O  O  O  O  O  O  O  .  .  .  O  O  O  O  O  .  .  .  .  .  O  O  O  .  .  .  .  .  .  .  O  .  .  .  .  
>>> print("Building internam Index for %d tile(s) ..." % len(inputTiles), end=' ')
	  
Traceback (most recent call last):
  File "<pyshell#270>", line 1, in <module>
    print("Building internam Index for %d tile(s) ..." % len(inputTiles), end=' ')
NameError: name 'inputTiles' is not defined
>>> print("Building internam Index for %d tile(s) ...",end=' ')
	  
Building internam Index for %d tile(s) ... 
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====
. . O O . O O . . . O O O O O O O . . O O O O O O O . . . O O O O O . . . . . O O O . . . . . . . O . . . . 
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====
. . O O . O O . . . O O O O O O O . . O O O O O O O . . . O O O O O . . . . . O O O . . . . . . . O . . . . 
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====
.
.
O
O
.
O
O
.
.
.
O
O
O
O
O
O
O
.
.
O
O
O
O
O
O
O
.
.
.
O
O
O
O
O
.
.
.
.
.
O
O
O
.
.
.
.
.
.
.
O
.
.
.
.
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====
.
.
O
O
.
O
O
.
.
.
O
O
O
O
O
O
O
.
.
O
O
O
O
O
O
O
.
.
.
O
O
O
O
O
.
.
.
.
.
O
O
O
.
.
.
.
.
.
.
O
.
.
.
.
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====
.
.
O
O
.
O
O
.
.
.
O
O
O
O
O
O
O
.
.
O
O
O
O
O
O
O
.
.
.
O
O
O
O
O
.
.
.
.
.
O
O
O
.
.
.
.
.
.
.
O
.
.
.
.
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====
..OO.OO...OOOOOOO..OOOOOOO...OOOOO.....OOO.......O....
>>> print(\)
	
SyntaxError: unexpected character after line continuation character
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====
..OO.OO...OOOOOOO..OOOOOOO...OOOOO.....OOO.......O....

>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====
.

.

O

O

.

O

O

.

.

.

O

O

O

O

O

O

O

.

.

O

O

O

O

O

O

O

.

.

.

O

O

O

O

O

.

.

.

.

.

O

O

O

.

.

.

.

.

.

.

O

.

.

.

.

>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====
.
.
O
O
.
O
O
.
.
.
O
O
O
O
O
O
O
.
.
O
O
O
O
O
O
O
.
.
.
O
O
O
O
O
.
.
.
.
.
O
O
O
.
.
.
.
.
.
.
O
.
.
.
.
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====
..OO.OO...OOOOOOO..OOOOOOO...OOOOO.....OOO.......O....
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====
.-.-O-O-.-O-O-.-.-.-O-O-O-O-O-O-O-.-.-O-O-O-O-O-O-O-.-.-.-O-O-O-O-O-.-.-.-.-.-O-O-O-.-.-.-.-.-.-.-O-.-.-.-.-
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====


.-.-O-O-.-O-O-.-.-

.-O-O-O-O-O-O-O-.-

.-O-O-O-O-O-O-O-.-

.-.-O-O-O-O-O-.-.-

.-.-.-O-O-O-.-.-.-

.-.-.-.-O-.-.-.-.-
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====


..OO.OO..

.OOOOOOO.

.OOOOOOO.

..OOOOO..

...OOO...

....O....
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====


..OO.OO..

.OOOOOOO.

.OOOOOOO.

..OOOOO..

...OOO...

....O....
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====


..OO.OO..

.OOOOOOO.

.OOOOOOO.

..OOOOO..

...OOO...

....O....
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====


......Traceback (most recent call last):
  File "/Users/senthilnatarajan/Dropbox/Programming/Python/grid.py", line 15, in <module>
    print(grid[i][x],end='')
IndexError: list index out of range
>>> 
==== RESTART: /Users/senthilnatarajan/Dropbox/Programming/Python/grid.py ====


..OO.OO..

.OOOOOOO.

.OOOOOOO.

..OOOOO..

...OOO...

....O....
>>> 

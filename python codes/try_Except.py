print('How many cats?')

x=input()

try:
    if int(x) >= 4:
        print('thats a lot of cats')
    elif int(x)<0:
        print('Error - Negative number')
    else:
        print('Not too many cats')
except ValueError:
    print('Error - You have entered alphanumeric characters')


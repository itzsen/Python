def Div42by(number):
    try:
        return 42/number
    except ZeroDivisionError:
        print('Error: You tried to divide by Zero')

print ('1',Div42by(1))
print ('2',Div42by(2))
print ('3',Div42by(3))
print ('0',Div42by(0))
print ('5',Div42by(5))

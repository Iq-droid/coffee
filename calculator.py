import math

def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    return a / b

def square_root(a):
    return math.sqrt(a)

def power(a, b):
    return a ** b

opt = int(input("Choose Operation from 1(Add), 2(Sub), 3(Multi), 4(Div), 5(Square Root), 6(Power) = "))
a = int(input("First Number = "))

if opt == 1:
    b = int(input("Second Number = "))
    print(a, ' + ', b, '  =  ', addition(a, b))
elif opt == 2:
    b = int(input("Second Number = "))
    print(a, ' - ', b, '  =  ', subtraction(a, b))
elif opt == 3:
    b = int(input("Second Number = "))
    print(a, ' * ', b, '  =  ', multiplication(a, b))
elif opt == 4:
    b = int(input("Second Number = "))
    print(a, ' / ', b, '  =  ', division(a, b))
elif opt == 5:
    print('Square Root of', a, ' = ', square_root(a))
elif opt == 6:
    b = int(input("Power = "))
    print(a, ' ^ ', b, '  =  ', power(a, b))
else:
    print('Invalid Input')
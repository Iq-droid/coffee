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
n1 = int(input("First Number        = "))
n2 = int(input("Second Number = "))

if opt == 1:
    print(n1, ' + ', n2, '  =  ', addition(n1, n2))
elif opt == 2:
    print(n1, ' - ', n2, '  =  ', subtraction(n1, n2))
elif opt == 3:
    print(n1, ' * ', n2, '  =  ', multiplication(n1, n2))
elif opt == 4:
    print(n1, ' / ', n2, '  =  ', division(n1, n2))
elif opt == 5:
    print('Square Root of', n1, ' = ', square_root(n1))
    print('Square Root of', n2, ' = ', square_root(n2))
elif opt == 6:
    print(n1, ' ^ ', n2, '  =  ', power(n1, n2))
else:
    print('Invalid Input')
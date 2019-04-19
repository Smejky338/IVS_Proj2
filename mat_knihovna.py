#implementacia mat. kniznice


import math

def Plus(a, b):
    return a+b

def Minus(a, b):
    return a-b

def Multiply(a, b):
    return a*b

def Divide(a, b):
    if b==0:
        raise ZeroDivisionError("Nie je mozne delit nulou!")
    return a/b

def Factorial(a):
    if a<0 or isinstance(a, float):
        raise ValueError("Faktorial je definovany len pre prirodzene cisla a nulu!")
    if a>990:
        raise ValueError("Factorial pracuje len s cislami do 990!")
    if a==0:
        return 1
    else:
        return a*Factorial(a-1)

def Power(x, y):
    if y<0 or isinstance(y, float):
        raise ValueError("Power pracuje len s prirodzenym exponentom!")
    return x ** y


def Odmocnina(x, y):
    if x<0 and (y%2 ==0):
        raise ValueError("Zaklad nemoze byt zaporny pre parne odmocniny!")
    if y<=0 or isinstance(y, float):
        raise ValueError("Odmocnina musi byt prirodzene cislo!")
    return x ** (1/y)

def Log(x):
    if x <= 0:
        raise ValueError("Zaklad logaritmu musi byt kladne cislo!")
    return math.log10(x)
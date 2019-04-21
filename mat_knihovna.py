## @file mat_knihovna.py
# @brief Modul s funkciami vykonavajucimi matematicke operacie
# @author Veronika Svitkova xsvitk00
# @date April 2019

import math

##
# Vykona a + b a vrati vysledok. Pracuje aj so zapornymi a desatinnymi cislami.
# @brief Aritmeticke plus
# @param a Prvy scitanec
# @param b Druhy scitanec
# @return Sucet cisel "a" a "b"
#
def Plus(a, b):
    return a+b
##
# Vykona a - b a vrati vysledok. Pracuje aj so zapornymi a desatinnymi cislami.
# @brief Aritmeticke minus
# @param a Mensenec
# @param b Mensitel
# @return Rozdiel cisel "a" a "b"
#
def Minus(a, b):
    return a-b

##
# Vykona a * b a vrati vysledok. Pracuje aj so zapornymi a desatinnymi cislami.
# @brief Aritmeticke krat
# @param a Prvy cinitel
# @param b Druhy cinitel
# @return Sucin cisel "a" a "b"
#
def Multiply(a, b):
    return a*b

##
# Vykona a / b a vrati vysledok. Pracuje aj so zapornymi a desatinnymi cislami.
# @brief Aritmeticke deleno
# @param a Delenec
# @param b Delitel
# @return Podiel cisel "a" a "b"
# @exception ZeroDivisionError ak "b" == 0
#
def Divide(a, b):
    if b==0:
        raise ZeroDivisionError("Nie je mozne delit nulou!")
    return a/b

##
# Rekurzivne vypocita faktorial a vrati vysledok. Pracuje len s nulou a prirodzenymi cislami do 990.
# @brief Faktorial a!
# @param a Cislo, z ktoreho sa pocita faktorial
# @return Faktorial cisla a
# @exception ValueError v pripade, ze "a" je desatinne, zaporne alebo vacsie ako 990 
#
def Factorial(a):
    if a<0 or isinstance(a, float):
        raise ValueError("Faktorial je definovany len pre prirodzene cisla a nulu!")
    if a>990:
        raise ValueError("Factorial pracuje len s cislami do 990!")
    if a==0:
        return 1
    else:
        return a*Factorial(a-1)

##
# Vypocita x ^ y a vrati vysledok. Pracuje aj so zapornymi cislami, exponent je prirodzeny.
# @brief Umocnovanie s prirodzenym exponentom
# @param x Zaklad mocniny
# @param y Exponent
# @return Vysledok umocnovania x^y
# @exception ValueError v pripade, ze "y" nie je prirodzene cislo 
#
def Power(x, y):
    if x<0 or isinstance(x, float):
        raise ValueError("Power pracuje len s prirodzenym exponentom!")
    return x ** y

##
# Vypocita odmocninu (a^(1/n)) a vrati vysledok. Pracuje aj s desatinnym zakladom.
# @brief Vseobecna odmocnina
# @param x Zaklad odmocniny
# @param y Uroven odmocniny
# @return Vysledok odmocnovania
# @exception ValueError v pripade zaporneho zakladu a zaporneho alebo desatinneho "y" 
#
def Odmocnina(x, y):
    if x<0 and (y%2 ==0):
        raise ValueError("Zaklad nemoze byt zaporny pre parne odmocniny!")
    if y<=0 or isinstance(y, float):
        raise ValueError("Odmocnina musi byt prirodzene cislo!")
    return x ** (1/y)

##
# Vypocita dekadicky logaritmus a vrati vysledok.
# @brief Dekadicky logaritmus
# @param x Zaklad logaritmu, x>=0
# @return Vysledok logaritmu
# @exception ValueError v pripade zaporneho "x"
#
def Log(x):
    if x <= 0:
        raise ValueError("Zaklad logaritmu musi byt kladne cislo!")
    return math.log10(x)




#Spusteni pres prikazovou radku:
#pytest [Param] test_mat_knihovna.py 

import mat_knihovna
import pytest

def test_Plus():
    assert mat_knihovna.Plus(0,0)==0
    assert mat_knihovna.Plus(10,-10)==0
    assert mat_knihovna.Plus(5,8)==13
    assert mat_knihovna.Plus(-5,-8)==-13
    assert mat_knihovna.Plus(250,-120)==130
    assert mat_knihovna.Plus(120,-250)==-130
    assert mat_knihovna.Plus(5000000,5000000)==10000000
    assert mat_knihovna.Plus(5000000,-1000000)==4000000
    assert mat_knihovna.Plus(0.25,0.25)==0.5
    assert mat_knihovna.Plus(0.123456,0)==0.123456

def test_Minus():
    assert mat_knihovna.Minus(0,0)==0
    assert mat_knihovna.Minus(10,10)==0
    assert mat_knihovna.Minus(5,8)==-3
    assert mat_knihovna.Minus(15,8)==7
    assert mat_knihovna.Minus(-5,-8)==3
    assert mat_knihovna.Minus(250,-120)==370
    assert mat_knihovna.Minus(-120,-250)==130
    assert mat_knihovna.Minus(5000000,-5000000)==10000000
    assert mat_knihovna.Minus(5000000,1000000)==4000000
    assert mat_knihovna.Minus(0.75,0.25)==0.5
    assert mat_knihovna.Minus(0.123456,0)==0.123456
    assert mat_knihovna.Minus(0,0.123456)==-0.123456

def test_Multiply():
    assert mat_knihovna.Multiply(5,5)==25
    assert mat_knihovna.Multiply(-5,5)==-25
    assert mat_knihovna.Multiply(-5,-5)==25
    assert mat_knihovna.Multiply(5,0)==0
    assert mat_knihovna.Multiply(0,5)==0
    assert mat_knihovna.Multiply(0,0)==0
    assert mat_knihovna.Multiply(5,5)==25
    assert mat_knihovna.Multiply(2018,2019)==4074342
    assert mat_knihovna.Multiply(526894,58965)==31068304710
    assert mat_knihovna.Multiply(5,0.2)==1
    assert mat_knihovna.Multiply(0.3425,0.12345)==0.042281625
    assert mat_knihovna.Multiply(0.3425,-0.12345)==-0.042281625

def test_Divide():
    assert mat_knihovna.Divide(25,5)==5
    assert mat_knihovna.Divide(25,-5)==-5
    assert mat_knihovna.Divide(-25,-5)==5
    assert mat_knihovna.Divide(5,5)==1
    assert mat_knihovna.Divide(-5,-5)==1
    assert mat_knihovna.Divide(15,8)==1.875
    assert mat_knihovna.Divide(0,5)==0
    assert mat_knihovna.Divide(25,-50)==-0.5
    assert mat_knihovna.Divide(4000000,-2000000)==-2
    assert mat_knihovna.Divide(0.324,0.48)==0.675
    assert mat_knihovna.Divide(0.324,-0.48)==-0.675
    with pytest.raises(ZeroDivisionError):
        mat_knihovna.Divide(5,0)
        mat_knihovna.Divide(1234.5678,0)
        mat_knihovna.Divide(-500,0)

def test_Factorial():
    assert mat_knihovna.Factorial(0)==1
    assert mat_knihovna.Factorial(1)==1
    assert mat_knihovna.Factorial(8)==40320
    assert mat_knihovna.Factorial(18)==6402373705728000
    with pytest.raises(ValueError):
        mat_knihovna.Factorial(-5)
        mat_knihovna.Factorial(-5.85)
        mat_knihovna.Factorial(5.123456789)

def test_Power():
    assert mat_knihovna.Power(0,0)==1
    assert mat_knihovna.Power(5,0)==1
    assert mat_knihovna.Power(-5,0)==1
    assert mat_knihovna.Power(5,1)==5
    assert mat_knihovna.Power(5,5)==3125
    assert mat_knihovna.Power(-5,5)==-3125
    assert mat_knihovna.Power(5,10)==9765625
    assert mat_knihovna.Power(18,18)==39346408075296537575424
    with pytest.raises(ValueError):
        assert mat_knihovna.Power(10,3.5)
        assert mat_knihovna.Power(10,-3.5)
        assert mat_knihovna.Power(5,-1)

def test_Odmocnina():
    assert mat_knihovna.Odmocnina(0,2)==0
    assert mat_knihovna.Odmocnina(1,20)==1
    assert mat_knihovna.Odmocnina(4,2)==2
    assert mat_knihovna.Odmocnina(8,3)==2
    assert mat_knihovna.Odmocnina(0.58,2)==0.7615773105863908
    assert mat_knihovna.Odmocnina(1000000,8)==5.623413251903491
    with pytest.raises(ValueError):
        mat_knihovna.Odmocnina(-5,2)
        mat_knihovna.Odmocnina(-5,-2)
        mat_knihovna.Odmocnina(1,-20)

def test_Log():
    assert mat_knihovna.Log(1) == 0
    assert mat_knihovna.Log(10)==1
    assert mat_knihovna.Log(1000)==3   
    assert mat_knihovna.Log(15)==1.1760912590556813
    assert mat_knihovna.Log(5.25)==0.7201593034059569
    assert mat_knihovna.Log(0.25)==-0.6020599913279624
    assert mat_knihovna.Log(12000)==4.079181246047625
    with pytest.raises(ValueError):
        mat_knihovna.Log(0)
        mat_knihovna.Log(-15)

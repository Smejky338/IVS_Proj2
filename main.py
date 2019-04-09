#import mat_knihovna.py
import gui

def Plus (a,b):
    return a+b 


number=""
number2=""
x=0
def test(text_input, num):
    global number
    number = number + str(num) 
    text_input.set(number)

    #global number2
    #number2 = number2 + str(num)
    #text_output.set(number2)

   

def plus(text_input):
    global number 
    global x
    x = int(number)
    number= ""
   


def solve(text_input):
    global x
    global number
    y = int(number)
    sucet = Plus(x,y)
    text_input.set(sucet)
    print (sucet)
    number = sucet
    y= 0



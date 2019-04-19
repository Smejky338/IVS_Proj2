import mat_knihovna as mk

## 1+2 = ; a potom 2+2 = tu vyhodi chybu
## pri velkych vysledkoch pise mimo okna
##treba obmedzit pocet cislic na vstupe a vystupe
## 2+2+2+2

number=""
number2=""
x=0
y=0
operator=""
point = False

#Vymazat obsah kalkulacky
def clear(text_input,text_output):
    global number
    global number2
    global x
    global y
    global operator
    global point
    point = False
    operator=""
    number=""
    number2=""
    x=0
    y=0
    text_input.set(number)
    text_output.set(number2)

#cinnosti ktore musi kazda operacia nastavit
def operation():
    global number 
    global x
    global point
    point = False
    x = int(number)
    number= ""


def digit(text_input, num, text_output):
    global point
    global number
    global y
    #kontrola ci je to string lebo ak dam priklad a = tak potom uz sa neda zapisovat (vtedy uz je float)
    if isinstance(number, str):
        #kontrola desatinneho cisla - v cisle sa moze nachadzat len jedna bodka 
        if point==False or num!='.':
            number = number + str(num) 
            text_input.set(number)
            global number2
            number2 = number2 + str(num)
            text_output.set(number2)
        if num == ".":
            point= True



def plus(text_output):
    operation()
    global operator
    operator = "+"
    global number2
    number2 = number2 + " + "
    text_output.set(number2)
        
def minus(text_output):
    operation()
    global operator
    operator = "-"
    global number2
    number2 = number2 + " - "
    text_output.set(number2)

def mul(text_output):
    operation()
    global operator
    operator = "x"
    global number2
    number2 = number2 + " x "
    text_output.set(number2)

def div(text_output):
    operation()
    global operator
    operator = "/"
    global number2
    number2 = number2 + " / "
    text_output.set(number2)

def pow(text_output):
    operation()
    global operator
    operator = "^"
    global number2
    number2 = number2 + " ^ "
    text_output.set(number2)

def sqrt(text_output):
    operation()
    global operator
    operator = "sqrt"
    global number2
    number2 = number2 + " sqrt "
    text_output.set(number2)

def log(text_output):
    operation()
    global operator
    operator = "log"
    global number2
    number2 = number2 + " log "
    text_output.set(number2)

def fact(text_output):
    operation()
    global operator
    operator = "!"
    global number2
    number2 = number2 + " ! "
    text_output.set(number2)
    global number
    number = 0


def solve(text_input):
    global x
    global number
    global operator
    global y
    global point
    if operator != '':
        y = int(number)
        if operator == '+':
            result = mk.Plus(x,y)
            text_input.set(result)
        if operator == '-':
            result = mk.Minus(x,y)
            text_input.set(result)
        if operator == 'x':
            result = mk.Multiply(x,y)
            text_input.set(result)
        if operator == '/':
            result = mk.Divide(x,y)
            text_input.set(result)
        if operator == '^':
            result = mk.Power(x,y)
            text_input.set(result)
        if operator == 'sqrt':
            result = mk.Odmocnina(x,y)
            text_input.set(result)
        if operator == 'log':
            result = mk.Log(x,y)
            text_input.set(result)
        if operator == '!':
            result = mk.Factorial(x)
            text_input.set(result)
        number = result
        y = 0
        x = 0
        operator=""
        point = False
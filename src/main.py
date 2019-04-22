import mat_knihovna as mk

## 1+2 = ; a potom 2+2 = tu vyhodi chybu
## pri velkych vysledkoch pise mimo okna
##treba obmedzit pocet cislic na vstupe a vystupe
## 2+2+2+2

#####################################################
#Premenne ktore reguluju operacie alebo vstupne cisla
#####################################################
number=""   #vstupne cislo
number2=""  #cely vstup - priklad
x=0     #prve cislo nad ktorym je robena operacia
y=0     #prve cislo nad ktorym je robena operacia
operator=""     #urcuje operaciu ktora bude robena nad cislami x a y
point = False    #reguluje desatinne cisla - moze byt len jedna desatinna ciarka vo vstupnom cisle

#Vymazat obsah kalkulacky
# @brief Vymaze pamat kalkulacky, vynuluje globalne premenne, nastavi program ako pri spusteni
# @param text_input Okno pre vypis vysledku a jednotlivych vstupnych cisel
# @param text_output Okno pre priklad
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

#Cinnosti ktore musi kazda operacia nastavit
# @brief Funkcia spracuje a nastavi "x" hodnotu kalkulacky a vynuluje vstup - teda pripravi kalkulacku na prijatie druheho cisla "y" + vynuluje kontrolu desatinnej ciarky resp. bodky
def operation():
    global number 
    global x
    global point
    point = False
    x = int(number)
    number= ""

# @brief Funckia spracovava vstupne cislice - stlacenia buttonov - do jedneho cisla 
# @param text_input Urcuje do ktoreho okna sa vypisuje cislo s ktorym nasledne budu robene operacie
# @param text_output Urcuje do ktoreho okna sa vypisuje priklad - cely vstup prikladu aj s operandom 
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


# @brief  Funkcia ktora pripravi x na scitanie s druhym cislom y (ocakava sa zadanie y)
# @param text_output Urcuje okno do ktoreho je vypisane cislo x a dana operacia ktora bude robena
def plus(text_output):
    operation()
    global operator
    operator = "+"
    global number2
    number2 = number2 + " + "
    text_output.set(number2)

# @brief  Funkcia ktora pripravi x (nastavi prislusny operand) na odcitanie s druhym cislom y (ocakava sa zadanie y)
# @param text_output Urcuje okno do ktoreho je vypisane cislo x a dana operacia ktora bude robena        
def minus(text_output):
    operation()
    global operator
    operator = "-"
    global number2
    number2 = number2 + " - "
    text_output.set(number2)

# @brief  Funkcia ktora pripravi x (nastavi prislusny operand) na nasobenie s druhym cislom y (ocakava sa zadanie y)
# @param text_output Urcuje okno do ktoreho je vypisane cislo x a dana operacia ktora bude robena
def mul(text_output):
    operation()
    global operator
    operator = "x"
    global number2
    number2 = number2 + " x "
    text_output.set(number2)

# @brief  Funkcia ktora pripravi x (nastavi prislusny operand) na delenie s druhym cislom y (ocakava sa zadanie y)
# @param text_output Urcuje okno do ktoreho je vypisane cislo x a dana operacia ktora bude robena
def div(text_output):
    operation()
    global operator
    operator = "/"
    global number2
    number2 = number2 + " / "
    text_output.set(number2)


# @brief  Funkcia ktora pripravi x (nastavi prislusny operand) na umocnenie druhym cislom y (ocakava sa zadanie y)
# @param text_output Urcuje okno do ktoreho je vypisane cislo x a dana operacia ktora bude robena
def pow(text_output):
    operation()
    global operator
    operator = "^"
    global number2
    number2 = number2 + " ^ "
    text_output.set(number2)


# @brief  Funkcia ktora pripravi x (nastavi prislusny operand) na odmocnenie druhym cislom y (ocakava sa zadanie y)
# @param text_output Urcuje okno do ktoreho je vypisane cislo x a dana operacia ktora bude robena
def sqrt(text_output):
    operation()
    global operator
    operator = "sqrt"
    global number2
    number2 = number2 + " sqrt "
    text_output.set(number2)


# @brief  Funkcia ktora pripravi x na operaciu log (nastavi prislusny operand)
# @param text_output Urcuje okno do ktoreho je vypisane cislo x a dana operacia ktora bude robena
def log(text_output):
    operation()
    global operator
    operator = "log"
    global number2
    number2 = number2 + " log "
    text_output.set(number2)


# @brief  Funkcia ktora pripravi x na operaciu factorial (nastavi prislusny operand)
# @param text_output Urcuje okno do ktoreho je vypisane cislo x a dana operacia ktora bude robena
def fact(text_output):
    operation()
    global operator
    operator = "!"
    global number2
    number2 = number2 + " ! "
    text_output.set(number2)
    global number
    number = 0

# @brief Funkcia najprv spracuje - nastavi cislo "y" a nasledne riesi zadany priklad podla nastaveneho operandu
# @param text_input Urcuje okno do ktoreho ma byt vypisany vysledok  
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
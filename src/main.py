## @file main.py
# @brief Modul pro backend cast kalkulacky a linkovani s matematickou knihovnou
# @author Ondrej Kondek xkonde04
# @date April 2019
# @todo osetrenie nespravnych vstupov pri factiorial...
# @todo pri velkych vysledkoch pise mimo okna
# @todo treba obmedzit pocet cislic na vstupe a vystupe
# @todo 2.1 + 2.2 = x a potom ! tak ma hodit chybu
# @todo 8/3 = x 5 -- zly vysledok
# @todo nefunguje operacia bez x 

import mat_knihovna as mk


#####################################################
#Premenne ktore reguluju operacie alebo vstupne cisla
#####################################################
##vstupne cislo
number=""  
##cely vstup - priklad 
number2="" 
##prve cislo nad ktorym je robena operacia (operand)
x=0     
##prve cislo nad ktorym je robena operacia (operand)
y=0     
##urcuje operaciu ktora bude robena nad cislami x a y
operator=""  
##reguluje desatinne cisla - moze byt len jedna desatinna ciarka vo vstupnom cisle   
point = False
sol = False     
#counter na velkost cisla
counter = 1
##pro zaznam chyby
error = False   

##
# @brief Funkcia zahlasi ERROR a pripravi kalkulacku na opatovne pouzitie
# @param text_input Okno do ktoreho ma byt vypisana chybova hlaska 
def ERROR(text_input):
    global error
    text_input.set("M-error")
    error = True
    number = "" 


##
# @brief Dany string konvertuje na int alebo float podla typu
# @param n String ktory ma byt konvertovany
# @return n Vracia cislo - bud int alebo float 
def num_type(n):
    try:
        num = int(n)
    except ValueError:
        return float(n)
    else:
        return int(n)

##
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
    global counter
    counter = 1
    point = False
    operator=""
    number=""
    number2=""
    x=0
    y=0
    text_input.set(number)
    text_output.set(number2)

##
#Cinnosti ktore musi kazda operacia nastavit
# @brief Funkcia spracuje a nastavi "x" hodnotu kalkulacky a vynuluje vstup - teda pripravi kalkulacku na prijatie druheho cisla "y" + vynuluje kontrolu desatinnej ciarky resp. bodky
def operation():         
    global number 
    global x
    global point
    global sol
    global counter
    counter = 1
    sol = False
    point = False
    x = num_type(number)
    number= ""

##
# @brief Funckia spracovava vstupne cislice - stlacenia buttonov - do jedneho cisla 
# @param text_input Urcuje do ktoreho okna sa vypisuje cislo s ktorym nasledne budu robene operacie
# @param text_output Urcuje do ktoreho okna sa vypisuje priklad - cely vstup prikladu aj s operandom 
def digit(text_input, num, text_output):
    global counter
    if counter<11:
        global point
        global number
        global y
        global sol
        if sol == True:
            clear(text_input,text_output)
            sol = False
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
        counter= counter + 1

## 
# @brief  Funkcia ktora pripravi x na scitanie s druhym cislom y (ocakava sa zadanie y)
# @param text_output Urcuje okno do ktoreho je vypisane cislo x a dana operacia ktora bude robena
def plus(text_output):
    global number
    if number != "": 
        global operator 
        if operator == "":
            operation()
            operator = "+"
            global number2
            number2 = number2 + " + "
            text_output.set(number2)

##
# @brief  Funkcia ktora pripravi x (nastavi prislusny operand) na odcitanie s druhym cislom y (ocakava sa zadanie y)
# @param text_output Urcuje okno do ktoreho je vypisane cislo x a dana operacia ktora bude robena        
def minus(text_output):
    global number
    if number != "": 
        global operator 
        if operator == "":
            operation()
            operator = "-"
            global number2
            number2 = number2 + " - "
            text_output.set(number2)

##
# @brief  Funkcia ktora pripravi x (nastavi prislusny operand) na nasobenie s druhym cislom y (ocakava sa zadanie y)
# @param text_output Urcuje okno do ktoreho je vypisane cislo x a dana operacia ktora bude robena
def mul(text_output):
    global number
    if number != "": 
        global operator 
        if operator == "":
            operation()
            operator = "x"
            global number2
            number2 = number2 + " x "
            text_output.set(number2)

##
# @brief  Funkcia ktora pripravi x (nastavi prislusny operand) na delenie s druhym cislom y (ocakava sa zadanie y)
# @param text_output Urcuje okno do ktoreho je vypisane cislo x a dana operacia ktora bude robena
def div(text_output):
    global number
    if number != "": 
        global operator 
        if operator == "":
            operation()
            operator = "/"
            global number2
            number2 = number2 + " / "
            text_output.set(number2)

##
# @brief  Funkcia ktora pripravi x (nastavi prislusny operand) na umocnenie druhym cislom y (ocakava sa zadanie y)
# @param text_output Urcuje okno do ktoreho je vypisane cislo x a dana operacia ktora bude robena
def pow(text_output):
    global number
    if number != "": 
        global operator 
        if operator == "":
            operation()
            operator = "^"
            global number2
            number2 = number2 + " ^ "
            text_output.set(number2)

##
# @brief  Funkcia ktora pripravi x (nastavi prislusny operand) na odmocnenie druhym cislom y (ocakava sa zadanie y)
# @param text_output Urcuje okno do ktoreho je vypisane cislo x a dana operacia ktora bude robena
def sqrt(text_output):
    global number
    if number != "": 
        global operator 
        if operator == "":
            operation()
            operator = "sqrt"
            global number2
            number2 = number2 + " sqrt "
            text_output.set(number2)

##
# @brief  Funkcia ktora pripravi x na operaciu log (nastavi prislusny operand)
# @param text_output Urcuje okno do ktoreho je vypisane cislo x a dana operacia ktora bude robena
def log(text_output):
    global number
    if number != "": 
        global operator 
        if operator == "":
            operation()
            operator = "log"
            global number2
            number2 = number2 + " log "
            text_output.set(number2)
            number = "0"

##
# @brief  Funkcia ktora pripravi x na operaciu factorial (nastavi prislusny operand)
# @param text_output Urcuje okno do ktoreho je vypisane cislo x a dana operacia ktora bude robena
def fact(text_output):
    global number
    if number != "": 
        global operator 
        if operator == "":
            operation()
            operator = "!"
            global number2
            number2 = number2 + " ! "
            text_output.set(number2)
            number = "0"

##
# @brief Funkcia najprv spracuje - nastavi cislo "y" a nasledne riesi zadany priklad podla nastaveneho operandu
# @param text_input Urcuje okno do ktoreho ma byt vypisany vysledok  
def solve(text_input):
    global x
    global number
    global operator
    global y
    global point
    global sol
    global error
    if operator != '':
        y = num_type(number)
        if operator == '+':
            result = mk.Plus(x,y)
        if operator == '-':
            result = mk.Minus(x,y)
        if operator == 'x':
            result = mk.Multiply(x,y)
        if operator == '/':
            if y==0:
                ERROR(text_input)
            else:
                result = mk.Divide(x,y)
        if operator == '^':
            if y<0 or isinstance(y, float):
                ERROR(text_input)
            else:
                result = mk.Power(x,y)
        if operator == 'sqrt':
            if x<0 and (y%2 ==0):
                ERROR(text_input) 
            elif y<=0 or isinstance(y, float):
                ERROR(text_input)
            else:
                result = mk.Odmocnina(x,y)
        if operator == 'log':
            if x <= 0:
                ERROR(text_input)
            else:
                result = mk.Log(x)
        if operator == '!':
            if x>990 or x<0 or isinstance(x, float):
                ERROR(text_input)
            else:
                result = mk.Factorial(x)

        if error==False:
            result = round(result,5)
            if result>9999999999 or result<-9999999999:
                text_input.set("M-error")
                number = ""
            else:
                text_input.set(result)
                number = str(result)
        y = 0
        x = 0
        operator=""
        point = False
        sol = True
        global counter
        counter = 1
        error = False
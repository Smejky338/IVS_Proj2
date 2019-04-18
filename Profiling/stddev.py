#program pro vypocet vyberove smerodatne odchylky z posloupnosti cisel, cte ze stdin az do 1000 cisel(radku).
import sys
sys.path.append("..")
import mat_knihovna as mat
import fileinput

#while scan != EOF:
    #suma1=xi-(aritm.prumer)

#mat_knihovna.Plus()


def odchylka():
    soucet=0
    pole=[]
    sumax2=0
    pocet=0
    for line in fileinput.input():
        #print(line)
        pole.append(float(line))
        #if line)) != line:#chybi overovani vstupu, ze je cislo
         #   print("neocekavany vstup!")
          #  return -1
        soucet += float(line)
        sumax2 += mat.Power(float(line), 2)#suma(x^2)
        pocet += 1#N

    prumer = soucet/len(pole)
    
    suma = mat.Odmocnina( mat.Multiply(mat.Divide(1, mat.Minus(pocet, 1)), mat.Minus(sumax2, pow(prumer , 2) ) ), 2 ) #odm(1/N-1 * (sumax2 - N*prumer^2))
    
    #print("jebo")
    print(suma)

odchylka()
#HOVNOOOOOOOOOOOOOOOOOOOOOOOOOOO
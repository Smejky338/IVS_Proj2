#program pro vypocet vyberove smerodatne odchylky z posloupnosti cisel, cte ze stdin az do 1000 cisel(radku).
import sys
sys.path.append("..")#kvuli tomu, ze mat_knihovna je o slozku vyse
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
        pole.append(float(line))
        
        soucet = mat.Plus(soucet, float(line))
        sumax2 = mat.Plus(sumax2, mat.Power(float(line), 2))#suma(x^2)
        pocet = mat.Plus(pocet, 1)#N++
    prumer = mat.Divide(soucet, pocet)
    
#                                                   1/N-1                *                  -                       x^2   *   N
    suma = mat.Odmocnina( mat.Multiply(mat.Divide(1, mat.Minus(pocet, 1)), mat.Minus( sumax2, mat.Multiply( pow(prumer , 2), pocet ) ) ), 2 ) #odm(1/N-1 * (sumax2 - N*prumer^2))
    
    print(suma)
    return

#volani samotne funkce
#odchylka()
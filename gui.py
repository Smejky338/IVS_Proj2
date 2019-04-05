from tkinter import *
from kalkulacka import *


calc = Tk()
calc.title('Kalkulacka')
calc.configure(background='gray93')
calc.geometry("234x332")
#70+50+2+50+2+50+2+50+2+50+2

operator=""
text_input= StringVar()

#okno na vysledok
result=Entry(calc,font=('comicsans', 25), width=12, textvariable=text_input)
result.place(x=6,y=15)

#####################
#1.riadok buttonov
#####################
button_clear=Button(calc, text='C', fg='maroon',   bg='gray75', font=('comicsans', 12))
button_clear.config(width=5, height=2)
button_clear.place(x=4,y=70)

button_div=Button(calc, text='/', fg='maroon',   bg='gray75', font=('comicsans', 12))
button_div.config(width=5, height=2)
button_div.place(x=4+55+2,y=70)

button_mul=Button(calc, text='X', fg='maroon',   bg='gray75', font=('comicsans', 12))
button_mul.config(width=5, height=2)
button_mul.place(x=4+55+2+55+2,y=70)

button_fact=Button(calc, text='!', fg='maroon',   bg='gray75', font=('comicsans', 12))
button_fact.config(width=5, height=2)
button_fact.place(x=4+55+2+55+2+55+2,y=70)

#Button 7
button_7=Button(calc, text='7', fg='black', bg='gray83', font=('comicsans', 12), command=lambda :test())
button_7.config(width=5, height=2)
button_7.place(x=4,y=70+50+2)

#Button 8
button_8=Button(calc, text='8', fg='black',   bg='gray83', font=('comicsans', 12))
button_8.config(width=5, height=2)
button_8.place(x=4+55+2,y=70+50+2)

#Button 9
button_9=Button(calc, text='9', fg='black',   bg='gray83', font=('comicsans', 12))
button_9.config(width=5, height=2)
button_9.place(x=4+55+2+55+2,y=70+50+2)


button_pow=Button(calc, text='pow', fg='maroon',   bg='gray75', font=('comicsans', 12))
button_pow.config(width=5, height=2)
button_pow.place(x=4+55+2+55+2+55+2,y=70+50+2)

#Button 4
button_4=Button(calc, text='4', fg='black',   bg='gray83', font=('comicsans', 12))
button_4.config(width=5, height=2)
button_4.place(x=4,y=70+50+2+50+2)

#Button 5
button_5=Button(calc, text='5', fg='black',   bg='gray83', font=('comicsans', 12))
button_5.config(width=5, height=2)
button_5.place(x=4+55+2,y=70+50+2+50+2)

#Button 6
button_6=Button(calc, text='6', fg='black',   bg='gray83', font=('comicsans', 12))
button_6.config(width=5, height=2)
button_6.place(x=4+55+2+55+2,y=70+50+2+50+2)


button_sqr=Button(calc, text='sqr', fg='maroon',   bg='gray75', font=('comicsans', 12))
button_sqr.config(width=5, height=2)
button_sqr.place(x=4+55+2+55+2+55+2,y=70+50+2+50+2)

#Button 1
button_1=Button(calc, text='1', fg='black',   bg='gray83', font=('comicsans', 12))
button_1.config(width=5, height=2)
button_1.place(x=4,y=70+50+2+50+2+50+2)

#Button 2
button_2=Button(calc, text='2', fg='black',   bg='gray83', font=('comicsans', 12))
button_2.config(width=5, height=2)
button_2.place(x=4+55+2,y=70+50+2+50+2+50+2)

#Button 3
button_3=Button(calc, text='3', fg='black',   bg='gray83', font=('comicsans', 12))
button_3.config(width=5, height=2)
button_3.place(x=4+55+2+55+2,y=70+50+2+50+2+50+2)

button_func=Button(calc, text='func', fg='maroon',   bg='gray75', font=('comicsans', 12))
button_func.config(width=5, height=2)
button_func.place(x=4+55+2+55+2+55+2,y=70+50+2+50+2+50+2)

#Button napoveda
button_nap=Button(calc, text='?', fg='black',   bg='gray83', font=('comicsans', 12))
button_nap.config(width=5, height=2)
button_nap.place(x=4,y=70+50+2+50+2+50+2+50+2)

#Button 0
button_0=Button(calc, text='0', fg='black',   bg='gray83', font=('comicsans', 12))
button_0.config(width=5, height=2)
button_0.place(x=4+55+2,y=70+50+2+50+2+50+2+50+2)

#Button .point
button_point=Button(calc, text='.', fg='black',   bg='gray83', font=('comicsans', 12))
button_point.config(width=5, height=2)
button_point.place(x=4+55+2+55+2,y=70+50+2+50+2+50+2+50+2)

#Button =
button_eq=Button(calc, text='=', fg='maroon',   bg='gray75', font=('comicsans', 12))
button_eq.config(width=5, height=2)
button_eq.place(x=4+55+2+55+2+55+2,y=70+50+2+50+2+50+2+50+2)








calc.mainloop()

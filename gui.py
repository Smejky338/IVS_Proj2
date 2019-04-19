from tkinter import *
import main

window = Tk()
window.title=('TEST')
window.geometry("276x407")
window.configure(background='gray26')

text_input=StringVar()
text_output=StringVar()

frame = Frame(window)
frame.place(x=5,y=10)

frame2 = Frame(window)
frame2.configure(background='gray26')
frame2.place(x=5,y=90)

result2=Entry(frame, fg= 'white', font=('comicsans', 11), bg = 'gray26', width=33, bd=0, justify='right', textvariable=text_input)
result2.pack(side = TOP)

result=Entry(frame, fg= 'white',  font=('comicsans', 33), width=11, bg = 'gray26', bd=0, justify='right', textvariable=text_output)
#result.focus_set()
result.pack(side = BOTTOM)


#1 riadok
button_pow=Button(frame2, text='pow', fg='maroon', bg='gray75', font=('comicsans', 12))
button_pow.config(width=6, height=2)
button_pow.grid(column=0, row=0, padx= 1, pady= 1)

button_sqr=Button(frame2, text='sqr', fg='maroon', bg='gray75', font=('comicsans', 12))
button_sqr.config(width=6, height=2)
button_sqr.grid(column=1, row=0, padx= 1, pady= 1)

button_func=Button(frame2, text='func', fg='maroon', bg='gray75', font=('comicsans', 12))
button_func.config(width=6, height=2)
button_func.grid(column=2, row=0, padx= 1, pady= 1)

button_hint=Button(frame2, text='?', fg='maroon', bg='gray75', font=('comicsans', 12))
button_hint.config(width=6, height=2)
button_hint.grid(column=3, row=0, padx= 1, pady= 1)

#2. riadok

button_clear=Button(frame2, text='C', fg='maroon', bg='gray75', font=('comicsans', 12))
button_clear.config(width=6, height=2)
button_clear.grid(column=0, row=1, padx= 1, pady= 1)

button_div=Button(frame2, text='/', fg='maroon', bg='gray75', font=('comicsans', 12))
button_div.config(width=6, height=2)
button_div.grid(column=1, row=1, padx= 1, pady= 1)

button_mul=Button(frame2, text='X', fg='maroon', bg='gray75', font=('comicsans', 12))
button_mul.config(width=6, height=2)
button_mul.grid(column=2, row=1, padx= 1, pady= 1)

button_fact=Button(frame2, text='!', fg='maroon', bg='gray75', font=('comicsans', 12))
button_fact.config(width=6, height=2)
button_fact.grid(column=3, row=1, padx= 1, pady= 1)

#3.riadok

button_7=Button(frame2, text='7', fg='black', bg='gray83', font=('comicsans', 12))
button_7.config(width=6, height=2, command=lambda: main.digit(text_input,7,text_output))
button_7.grid(column=0, row=2, padx= 1, pady= 1)

button_8=Button(frame2, text='8', fg='black', bg='gray83', font=('comicsans', 12))
button_8.config(width=6, height=2)
button_8.grid(column=1, row=2, padx= 1, pady= 1)

button_9=Button(frame2, text='9', fg='black', bg='gray83', font=('comicsans', 12))
button_9.config(width=6, height=2)
button_9.grid(column=2, row=2, padx= 1, pady= 1)

button_min=Button(frame2, text='-', fg='maroon', bg='gray75', font=('comicsans', 12))
button_min.config(width=6, height=2)
button_min.grid(column=3, row=2, padx= 1, pady= 1)

# 4. riadok

button_4=Button(frame2, text='4', fg='black', bg='gray83', font=('comicsans', 12))
button_4.config(width=6, height=2)
button_4.grid(column=0, row=3, padx= 1, pady= 1)

button_5=Button(frame2, text='5', fg='black', bg='gray83', font=('comicsans', 12))
button_5.config(width=6, height=2)
button_5.grid(column=1, row=3, padx= 1, pady= 1)

button_6=Button(frame2, text='6', fg='black', bg='gray83', font=('comicsans', 12))
button_6.config(width=6, height=2)
button_6.grid(column=2, row=3, padx= 1, pady= 1)

button_plus=Button(frame2, text='+', fg='maroon', bg='gray75', font=('comicsans', 12))
button_plus.config(width=6, height=2)
button_plus.grid(column=3, row=3, padx= 1, pady= 1)

# 5.riadok

button_1=Button(frame2, text='1', fg='black', bg='gray83', font=('comicsans', 12))
button_1.config(width=6, height=2)
button_1.grid(column=0, row=4, padx= 1, pady= 1)

button_2=Button(frame2, text='2', fg='black', bg='gray83', font=('comicsans', 12))
button_2.config(width=6, height=2)
button_2.grid(column=1, row=4, padx= 1, pady= 1)

button_3=Button(frame2, text='3', fg='black', bg='gray83', font=('comicsans', 12))
button_3.config(width=6, height=2)
button_3.grid(column=2, row=4, padx= 1, pady= 1)

button_eq=Button(frame2, text='=', fg='maroon', bg='gray75', font=('comicsans', 12))
button_eq.config(width=6, height=2)
button_eq.grid(column=3, row=4, rowspan=2, padx= 1, pady= 1, ipady=26)

# 6.riadok

button_0=Button(frame2, text='0', fg='black', bg='gray83', font=('comicsans', 12))
button_0.config(width=6, height=2)
button_0.grid(column=0, row=5, columnspan=2, padx=1, pady= 1, ipadx= 33)

button_point=Button(frame2, text='.', fg='black', bg='gray83', font=('comicsans', 12))
button_point.config(width=6, height=2)
button_point.grid(column=2, row=5, padx= 1, pady= 1)



window.mainloop()

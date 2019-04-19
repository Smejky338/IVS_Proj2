import mat_knihovna

number=""
number2=""
x=0

def digit(text_input, num, text_output):
    global number
    number = number + str(num) 
    text_input.set(number)

    global number2
    number2 = number2 + str(num)
    text_output.set(number2)

 
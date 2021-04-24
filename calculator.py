from tkinter import *


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_ip.set(operator)


def btnClearDisplay():
    global operator
    operator = ""
    text_ip.set("")


def btnEquallInput():
    global operator
    sum = str(eval(operator))
    text_ip.set(sum)
    operator = ''


window = Tk()
window.title('Calculator')
window.selectbackground=('black')
# window.geometry('1000x500')
operator = ''
text_ip = StringVar()

# Adding pic and Heading
pic = PhotoImage(file="img/cal1.png")

heading2 = Label(window, image=pic).grid(row=0, column=0)
heading3 = Label(window, image=pic).grid(row=0, column=3)
heading4 = (Label(window, text="Calculator",fg='orange',justify='center', font=('arial', 25, 'bold'),bd=5)).grid(columnspan=4)
# adding text display
txtDisplay = Entry(window, font=('large,_font', 24, 'bold'), justify='right', textvariable=text_ip,
                   bd=20, insertwidth=4, bg='Gray', ).grid(columnspan=4)

# Adding buttons

btn7 = Button(window, text='7', padx=10, pady=10, bd=5, fg="black", font=('arial', 20, 'bold'),
              command=lambda: btnClick(7),
              bg="powder blue").grid(row=3, column=0)
btn8 = Button(window, text='8', padx=10, pady=10, bd=5, fg="black", font=('arial', 20, 'bold')
              , command=lambda: btnClick(8), bg='powder blue').grid(row=3, column=1)

btn9 = Button(window, text='9', padx=10, pady=10, bd=5, fg="black", font=('arial', 20, 'bold')
              , command=lambda: btnClick(9), bg='powder blue').grid(row=3, column=2)

divbtn = Button(window, text='/', padx=15, pady=10, bd=5, fg="black", font=('arial', 20, 'bold'), bg='powder blue'
                , command=lambda: btnClick("/")).grid(row=3, column=3)

btn4 = Button(window, text='4', padx=10, pady=10, bd=8, fg="black", font=('arial', 20, 'bold'),
              command=lambda: btnClick(4)
              , bg='powder blue').grid(row=4, column=0)

btn5 = Button(window, text='5', padx=10, pady=10, bd=8, fg="black", font=('arial', 20, 'bold')
              , command=lambda: btnClick(5), bg='powder blue').grid(row=4, column=1)

btn6 = Button(window, text='6', padx=10, pady=10, bd=8, fg="black", font=('arial', 20, 'bold')
              , command=lambda: btnClick(6), bg='powder blue').grid(row=4, column=2)

subbtn = Button(window, text='-', padx=10, pady=10, bd=8, fg="black", font=('arial', 20, 'bold'), bg='powder blue'
                , command=lambda: btnClick('-')).grid(row=4, column=3)

btn1 = Button(window, text='1', padx=10, pady=10, bd=8, fg="black", font=('arial', 20, 'bold')
              , command=lambda: btnClick(1), bg='powder blue').grid(row=5, column=0)

btn2 = Button(window, text='2', padx=10, pady=10, bd=8, fg="black", font=('arial', 20, 'bold')
              , command=lambda: btnClick(2), bg='powder blue').grid(row=5, column=1)

btn3 = Button(window, text='3', padx=10, pady=10, bd=8, fg="black", font=('arial', 20, 'bold')
              , command=lambda: btnClick(3), bg='powder blue').grid(row=5, column=2)

multn = Button(window, text='*', padx=10, pady=10, bd=8, fg="black", font=('arial', 20, 'bold'), bg='powder blue'
               , command=lambda: btnClick("*")).grid(row=5, column=3)

btn0 = Button(window, text='0', padx=10, pady=10, bd=8, fg="black", font=('arial', 20, 'bold')
              , command=lambda: btnClick(0), bg='powder blue').grid(row=6, column=0)

clearbtn = Button(window, text='C', padx=10, pady=10, bd=8, fg="black", font=('arial', 20, 'bold'), bg='powder blue'
                  , command=btnClearDisplay).grid(row=6, column=1)

eqlbtn = Button(window, text='=', padx=10, pady=10, bd=8, fg="black", font=('arial', 20, 'bold'), bg='powder blue'
                , command=btnEquallInput).grid(row=6, column=2)

addbtn = Button(window, text='+', padx=10, pady=10, bd=8, fg="black", font=('arial', 20, 'bold')
                , command=lambda: btnClick('+'), bg='powder blue').grid(row=6, column=3)

window.mainloop()

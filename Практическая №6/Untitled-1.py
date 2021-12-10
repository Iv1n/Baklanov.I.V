# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
def prgr1():
    a = txt1.get()
    i = 1
    N = int(a)
    result = ""
    while i ** 2 < N:
        result += str(i**2)
        i+=1
        result = result + " "
    vivod1.configure(text = result)
    
def prgr2():
    a = txt2.get()
    n = int(a)
    i = 2 
    while n % i !=0:
        i += 1
    vivod2.configure(text = i)
    
def prgr3():
    a = txt3.get()
    n = int(a)
    i = 2
    e = 1
    while i <= n:
        i*=2
        e+=1
    result="Показатель степени :" +str(e-1) +" "+"Степень :" +str(i//2)
    vivod3.configure(text=result)

def prgr4():
    x = int(txt4.get())
    y = int(txt4_1.get())
    n=1
    while x<y:
        x*=1.1
        n+=1
    n = "Потребуется" + str(n) + " дней"
    vivod4.configure(text=n)
    
k=0
def prgr5():
    global k
    a = txt5.get()
    print(a)
    if (a!="0"):
        k += 1
    else: 
        vivod5.configure(text=k)
    txt5.delete(0, END)
    
x=0
y=0
def prgr6():
    global y 
    a = txt6.get()
    print(a)
    global x
    if a !="0":
        y += 1
        x +=int(a)
    else:
        vivod6.configure(text=x/y)
    txt6.delete(0,END)
    
b=0
a=10000000
def prgr7():
    n=txt7.get()
    print(n)
    global b
    global a
    if(int(n) > a):
        b+=1
    a = int(n)
    if(n=="0"):
        vivod7.configure(text=b)
    txt7.delete(0, END)


window = Tk()
window.title("Практическая работа №6")
window.geometry('800x600')

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)
tab6 = ttk.Frame(tab_control)
tab7 = ttk.Frame(tab_control)

#вкладка1
tab_control.add(tab1, text='Первый номер')
lbl1 = Label(tab1, text='Введите значение n')
lbl1.grid(column=0, row=0)
txt1 = Entry(tab1, width=10)
txt1.grid(column=1, row=0)
btn1 = Button(tab1, text="Ввод", command=prgr1)
btn1.grid(column=2, row=0)
vvod1 = Label(tab1, text = 'Результат :')
vvod1.grid(column=3, row=0)
vivod1 = Label(tab1, text="")
vivod1.grid(column=4, row=0)

#вкладка2
tab_control.add(tab2, text='Второй номер') 
lbl2 = Label(tab2, text='Введите число')
lbl2.grid(column=0, row=1)
txt2 = Entry(tab2, width=10)
txt2.grid(column=1, row=1)
btn2 = Button(tab2, text="Ввод", command=prgr2)
btn2.grid(column=2,row=1)
vvod2 = Label(tab2, text="Результат :")
vvod2.grid(column=3,row=1)
vivod2 = Label(tab2, text="")
vivod2.grid(column=4,row=1)

#вкладка3
tab_control.add(tab3, text='Третий номер')
lbl3 = Label(tab3, text='Введите число')
lbl3.grid(column=0, row=2)
txt3 = Entry(tab3, width=10)
txt3.grid(column=1, row=2)
btn3 = Button(tab3, text="Ввод",command=prgr3)
btn3.grid(column=2,row=2)
vvod3 = Label(tab3,text="Результат :")
vvod3.grid(column=3,row=2)
vivod3 = Label(tab3, text="")
vivod3.grid(column=4, row=2)

#вкладка4
tab_control.add(tab4, text='Четвертый номер')
lbl4 = Label(tab4, text='Введите начальное расстояние и конечное')
lbl4.grid(column=0, row=3)
txt4 = Entry(tab4, width=10)
txt4.grid(column=1, row=3)
txt4_1 = Entry(tab4, width=10)
txt4_1.grid(column=2, row=3)
btn4 = Button(tab4, text = "Ввод", command=prgr4)
btn4.grid(column=3, row=3)
vvod4 = Label(tab4, text="Результат :")
vvod4.grid(column=4,row=3)
vivod4 = Label(tab4, text="")
vivod4.grid(column=5,row=3)

#вкладка5
tab_control.add(tab5, text='Пятый номер')
lbl5 = Label(tab5, text='Для вывода результата введите 0')
lbl5.grid(column=0, row=4)
txt5 = Entry(tab5, width=10)
txt5.grid(column=1, row=4)
btn5 = Button(tab5, text="Ввод", command=prgr5)
btn5.grid(column=2,row=4)
vvod5 = Label(tab5, text="Результат")
vvod5.grid(column=3, row=4)
vivod5 = Label(tab5, text="")
vivod5.grid(column=4, row=4)

#вкладка6
tab_control.add(tab6, text='Шестой номер')
lbl6 = Label(tab6, text='Введите последовательность. Для выполнения введите 0 :')
lbl6.grid(column=0, row=5)
txt6 = Entry(tab6, width=10)
txt6.grid(column=1, row=5)
btn6 = Button(tab6, text="Ввод", command=prgr6)
btn6.grid(column=2, row=5)
vvod6 = Label(tab6, text = "Результат :")
vvod6.grid(column=3, row=5)
vivod6 = Label(tab6, text= "")
vivod6.grid(column=4, row=5)

#вкладка7
tab_control.add(tab7, text='Седьмой номер')
lbl7 = Label(tab7, text='Для выполнения введите 0. Введите последовательность')
lbl7.grid(column=0, row=6)
txt7 = Entry(tab7, width=10)
txt7.grid(column=1, row=6)
btn7 = Button(tab7, text="Ввод", command=prgr7)
btn7.grid(column=2, row=6)
vvod7 = Label(tab7,text="")
vvod7.grid(column=3, row=6)
vivod7 = Label(tab7, text="")
vivod7.grid(column=4,row=6)


tab_control.pack(expand=1, fill='both')
window.mainloop()
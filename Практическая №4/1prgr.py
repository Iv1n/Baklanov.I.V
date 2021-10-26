# -*- coding: utf-8 -*-
def nomer1():
    str = input("Введите любую строку :")
    p1 = str[2]
    p2 = str[len(str) - 2]
    p3 = str[0:5]
    p4 = str[0:len(str)-3]
    p5 = str[0::2]
    p6 = str[1::2]
    p7 = str[::-1]
    p8 = p6[::2]
    p9 = len(str)
    print("1)" ,p1)
    print("2)" ,p2)
    print("3)" ,p3)
    print("4)" ,p4)
    print("5)" ,p5)
    print("6)" ,p6)
    print("7)" ,p7)
    print("8)" ,p8)
    print("Длина строки:",p9)
nomer1()
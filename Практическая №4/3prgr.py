# -*- coding: utf-8 -*-
def prgr3():
    str = input("Введите строку :")
    nz = len(str) // 2 + len(str) % 2
    x = str[0:nz]
    y = str[nz:]
    print(y + x)
prgr3()
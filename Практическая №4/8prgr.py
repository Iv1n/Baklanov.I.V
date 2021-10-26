# -*- coding: utf-8 -*-
def prgr7():
    str = input("Введите строку :")
    x = str.find("h")
    y = str.rfind("h")
    print(str[0:x +1] + str[x + 1:y][::-1] + str[y:])
prgr7()
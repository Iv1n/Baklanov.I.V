# -*- coding: utf-8 -*-
def prgr7():
    str = input("Введите строку :")
    str = str[:str.find('h')] + str[str.rfind('h') + 1:]
    print(str)
prgr7()
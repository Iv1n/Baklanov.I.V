# -*- coding: utf-8 -*-
def prgr6():
    str = input("Введите строку :")
    if (str.count("f") == 1):
        print(-1)
    elif (str.count("f") == 0):
        print(-2)
    else:
        print(str.count("f", str.find("f")+1))

prgr6()


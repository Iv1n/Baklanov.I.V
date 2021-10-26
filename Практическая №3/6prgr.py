# -*- coding: utf-8 -*-
def gh():
    n = int(input("Введите число :"))
    suma = 1
    for i in range(1, n + 1):
        suma *= i
    return suma
print(gh())

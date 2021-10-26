# -*- coding: utf-8 -*-

def gg():
    n = int(input("Введите от 1 до 9 : "))
    if(1 <= n <= 9):
        for i in range(1, n + 1):
            for k in range(1, i + 1):
                print(k, sep='', end='')
            print()
    else: return "Ошибка ввода"
    return
print(gg())


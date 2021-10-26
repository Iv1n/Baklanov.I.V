# -*- coding: utf-8 -*-
n = int(input("Введите число :"))
def prgr(n):
    a = n
    f = 1
    sum = 0
    for i in range(1, a + 1):
        f = f * i
        sum = sum + f
    else:
        print("Ответ :")
        return sum
print(prgr(n)) 

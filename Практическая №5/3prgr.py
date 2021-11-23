# -*- coding: utf-8 -*-
n = int(input("Введите n :"))
k = 2
i = 1
while k <= n:
    k *= 2
    i += 1
print("Показатель степени :", i - 1, "Степень :", k //2)

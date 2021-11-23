# -*- coding: utf-8 -*-
n = int(input("Введит n :"))
k = 2
while n % k != 0:
    k += 1
print("Наименьший натуральный делитель :",k)

# -*- coding: utf-8 -*-
def fib():
    n = int(input("Введеите число :"))
    per = 0
    sum = 1
    next = 1
    for i in range (2, n):
        pam = next
        next = per + next
        per = pam
        sum += next
    return sum 
print(fib())
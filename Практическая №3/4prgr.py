# -*- coding: utf-8 -*-
def s():
	sum = 0
	for i in range(int(input("Введите количество чисел :"))):
		sum += int(input("Введите число :"))
	return sum
print(s())

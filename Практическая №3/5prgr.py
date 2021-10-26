# -*- coding: utf-8 -*-
def sd():
	n = int(input("Введение число :"))
	suma = 0
	for i in range(n + 1):
		suma += i ** 3
	return suma
print(sd())

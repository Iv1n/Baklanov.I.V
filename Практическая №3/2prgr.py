# -*- coding: utf-8 -*-
def program2():
    x = int(input("Введите первое число :"))
    y = int(input("Введите второе число :"))
    if x < y:
     def schet():
	     print("Вывод :")
	     for i in range(x, y + 1):
		     print(i)
     print(schet())
    else:
	    def sh():
		    for i in range(x, y - 1, -1):
			    print(i)
	    print(sh())	
print(program2())
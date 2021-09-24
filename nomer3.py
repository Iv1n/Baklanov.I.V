# -*- coding: utf-8 -*-
age = int(input("Введите возраст:"))
ost = 16 - age
name = str(input("Укажите имя:"))
if (age > 0) and (age < 75):
    if (name != "Иван"):
        if (age >= 16):
            print('Поздарвялем вы поступили в ВГУИТ')
        else:
            print('Сначала нужно окончить школу \nосталось учиться:' + str(ost)+ ' года')
    else:
        print('Иванам вход запрещен')
else:
    print('Возраст неправлеен')

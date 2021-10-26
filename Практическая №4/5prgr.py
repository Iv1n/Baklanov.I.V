# -*- coding: utf-8 -*-
def progr5():
    string = input("Введите строку :")
    if (string.count("f") == 0):
        return
    if (string.count("f") == 1):
        print(string.find("f"))
    else:
        print("Первая f появилась в :" + str(string.find("f")))
        print("Последняя f появилась в :" + str(string.rfind("f")))

progr5()
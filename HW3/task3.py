'''
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

*Пример:*

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''
list = [1.1, 1.2, 3.1, 5, 10.01]
def calcDiffDec(l):
    dif = 0
    minD = 1
    maxD = 0
    for e in l:
        s = e%1
        if s == 0:
            continue
        if s < minD:
            minD = s
        if s > maxD:
            maxD = s
    dif = maxD - minD   
    return dif

print(calcDiffDec(list))

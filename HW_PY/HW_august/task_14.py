'''
Задача 14: Требуется вывести все целые степени двойки
 (т.е. числа вида 2**k),
 не превосходящие числа N.
'''
import math
n = int(input('Укажите число N '))
power = 1
k = 0
while power < n:
    print(f'{power:.0f}')
    k+=1
    power = math.pow(2,k)
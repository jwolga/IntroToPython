'''
Задача 14: Требуется вывести все целые степени двойки
 (т.е. числа вида 2**k),
 не превосходящие числа N.
'''
import math
n = int(input('Укажите число N '))
twoByCurrentPower = 1
countPower = 0
while twoByCurrentPower < n:
    print(f'{twoByCurrentPower:.0f}')
    countPower+=1
    twoByCurrentPower = math.pow(2,countPower)
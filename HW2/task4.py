'''
4'. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.(для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)
-2 -1 0 1 2
Позиции: 0,1 -> 2
'''
import random

N = int(input("Введите число N: "))
l = []
for i in range(-N, N+1):
    l.append(i)
lowBorder = random.randint(0, N-1)
hiBorder = random.randint(N, 2*N-1)
for p in l:
    print(p)
print(f"Произведение l[{lowBorder}] элемента ({l[lowBorder]}) на l[{hiBorder}] элемента ({l[hiBorder]}) равно {l[lowBorder] * l[hiBorder]}")


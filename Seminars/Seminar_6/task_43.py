'''
2) (пользовательский ввод можно заменить на рандомный)
Пользователь вводит  размер массива – N
и элементы массива (целые числа). 
нужно посчитать сколько повторений у каждого числа
посчитанные числа можно посчитать повторно в паре с другими числами

Ввод:			Вывод:
1 2 3 2 3 2			4
Пример решения на Python:

import random

n = int(input("Введите размер массива: "))
arr = []
for i in range(n):
    arr.append(random.randint(1, 10)) # генерируем случайные числа от 1 до 10

count_dict = {}
for num in arr:
    if num not in count_dict:
        count_dict[num] = arr.count(num)

total_count = 0
for count in count_dict.values():
    total_count += count * (count - 1) // 2 # формула для подсчета количества пар

print("Количество пар чисел с повторениями:", total_count)


'''
from random import randint

n = randint(5, 10)
list1 = [randint(1, 10) for num in range(n)]
print(list1)

count = 0

for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i] == list1[j]:
            count += list1.count(+1)
print(count)
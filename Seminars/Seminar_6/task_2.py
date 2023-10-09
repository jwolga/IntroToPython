'''
2) (пользовательский ввод можно заменить на рандомный)
Пользователь вводит  размер массива – N
и элементы массива (целые числа). 
нужно из этого массива вывести количество элементов, у которых ближайшие соседние элементы меньше самого элемента.

Ввод: 			Ввод:
5			5
1 2 3 4 5			1 5 1 5 1

Вывод:			Вывод:
0			2
'''
# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5               5
# 1 2 3 4 5       1 5 1 5 1
# Вывод: Вывод:
# 0 2
# (каждое число вводится с новой строки)

from random import randint

def create_list(n):
    new_list = [randint(0, 9) for _ in range(n)]
    return new_list

def count_elements(list1):
    count = 0
    for i in range(1, len(list1) - 1):
        if list1[i - 1] < list1[i] > list1[i + 1]:
            count += 1
    return count


n = randint(5, 10)
list1 = create_list(n)
print(n, ' -> ', list1)
print(count_elements(list1))
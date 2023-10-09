'''
Пользователь вводит  размер первого массива – N
и элементы первого массива. 
затем размер второго массива M  
и элементы второго массива
Нужно вывести те элементы первого массива, которых нет во втором массиве, при этом порядок последовательности сохранить исходный
Ввод: 			Вывод:
7			3 3 2 12
3 1 3 4 2 4 12
6
4 15 43 1 15 1

def getList():
    n = int(input('Укажите количество элементов массива'))
    list = []
    for i in range (0, n):
        list.append(int(input(f'Введите {i}-й элемент массива')))
        return list
'''
from random import randint


def create_list(n):
    new_list = [randint(0, 9) for _ in range(n)]
    return new_list


def get_diff_elements(list1, list2):
    list4 = [el for el in list1 if el not in list2]

    return list4

n = randint(5, 9)
m = randint(5, 9)
list1 = create_list(n)
list2 = create_list(m)
print(n, ' -> ', list1)
print(m, ' -> ', list2)
print(get_diff_elements(list1,list2))
# 
# list3 = []
# for el in list1:
#     if el not in list2:
#         list3.append(el)
# print(list3)
# 
# list4 = [el for el in list1 if el not in list2]
# 
# list5 = [el if el not in list2 else 0 for el in list1]
'''
Задача 22: Даны два неупорядоченных набора целых чисел 
(может быть, с повторениями). Выдать без повторений 
в порядке возрастания все те числа, 
которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во 
элементов первого множества. m — кол-во элементов 
второго множества. Затем пользователь вводит сами 
элементы множеств.
'''
n = int(input('Укажите количество элементов первого множества '))
m = int(input('Укажите количество элементов второго множества '))
list_1 = []
list_2 = []
for i in range(0,n):
    list_1.append(int(input(f'Введите {i + 1}-й элемент первого множества ')))
for i in range(0,m):   
    list_2.append(int(input(f'Введите {i + 1}-й элемент второго множества ')))
set_1 = set(list_1)
set_2 = set(list_2)
set_united = set_1.union(set_2)
list_sorted =  [item for item in set_united]
list_sorted.sort()
print(list_sorted)  
'''
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
Она растёт на круглой грядке, причём кусты высажены только 
по окружности. Таким образом, у каждого куста
 есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени
 сбора на них выросло различное число ягод — на i-ом кусте 
 выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического 
сбора черники. Эта система состоит из управляющего модуля 
и нескольких собирающих модулей. Собирающий модуль за один 
заход, находясь непосредственно перед некоторым кустом, 
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, 
которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки.
'''
import random
n = int(input('Укажите количество кустов на грядке '))
bush_bed = [random.randint(10,100) for i in range(0,n)]
print(bush_bed)
bush_groups = []
for index in range(0, n):
    prev_index = n - 1 if index == 0 else index - 1
    post_index = index + 1 if index < n - 1 else 0
    sum_group = bush_bed[index] + bush_bed[prev_index] + bush_bed[post_index]
    bush_groups.append(sum_group)
print(bush_groups)
max_group = 0
for item in bush_groups:
    max_group = item if item > max_group else max_group
print(f'Максимальное число ягод {max_group}')


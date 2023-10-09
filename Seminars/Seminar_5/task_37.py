'''
Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
'''
n = int(input('Укажите натуральное число N '))

def reverse_print(num, i):
    if i == num:
        return
    k = int(input('Укажите очередное число '))
    i += 1
    reverse_print(num, i)
    print(k)
   
reverse_print(n, 0)
'''
def num_revers(nat_num):
    if nat_num == 0:
        return ''
    k = input('Укажите очередное число: ')
    return num_revers(nat_num -1) + k + ' '

num = int(input('Введите натуральное число: '))
print(num_revers(num))
'''

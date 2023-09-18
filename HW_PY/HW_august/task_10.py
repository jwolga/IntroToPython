'''
Задача 10: На столе лежат n монеток. 
Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
'''
import random
n = int(input('Введите количество монет '))
countHaeds = 0
for i in range(1, n+1):
    isHead = random.randint(1, 100) <= 50
    message = f'{i}-я монета лежит орлом' if isHead else f'{i}-я монета лежит решкой'
    print(message)
    if isHead:
        countHaeds+=1
countTails = n - countHaeds
minCountSwap = countHaeds if countHaeds < countTails else countTails
print(f'Минимальное количество монет, которые нужно перевернуть {minCountSwap}')

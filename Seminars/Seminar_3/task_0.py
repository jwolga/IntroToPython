'''
На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть
'''
import random
n = int(input('Укажите количество монет '))
coins = [random.randrange(0, 2) for i in range(n)]
print(coins)
count_heads = 0
for coin in coins:
    if coin == 1:
        count_heads += 1
count_tails = n - count_heads
if count_heads > count_tails:
    print(count_tails)
else:
    print(count_heads)




# min_coins = 
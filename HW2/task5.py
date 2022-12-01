'''
 Реализуйте алгоритм перемешивания списка.
'''
import random

N = int(input("Введите размер списка: "))
l = []
for i in range(1,N+1):
    l.append(i)
print("Исходный список:")
for e in l:
    print(e)

for i in range(0, N):
    r = random.randint(0, N-1)
    t = l[i]
    l[i]=l[r]
    l[r]=t

print("Перемешанный список:")
for e in l:
    print(e)
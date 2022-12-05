'''
Напишите программу, которая будет преобразовывать десятичное число в двоичное.

*Пример:*

- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''
n = int(input("Введите число: "))
def toBinary(n):
    res = []
    while n > 0:
        res.append(n%2)
        n = n//2
    return list(reversed(res))

print(toBinary(n))
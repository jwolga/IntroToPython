'''
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Дополнительно)

*Пример:*

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
'''
n = int(input("Введите число: "))

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def negafibonacci(n):
    if n == -1:
        return 1
    if n == -2:
        return -1
    return negafibonacci(n+2) - negafibonacci(n+1)    
print(fibonacci(n))
print(negafibonacci(-n))

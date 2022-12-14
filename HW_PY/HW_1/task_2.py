'''
Найдите сумму цифр трехзначного числа.
Пример:
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
'''
number = int(input('Введите трехзначное число: '))
first_dig = number // 100
value = number % 100
second_dig = value // 10
third_dig = value % 10
print(f'Сумма цифр числа {number}: {first_dig + second_dig + third_dig}')


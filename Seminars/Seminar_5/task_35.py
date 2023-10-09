'''
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes 


n = int(input('Введите число '))
is_simple = True
for i in range(2, n):
    if n % i == 0:
        is_simple = False
        break
result = 'Yes' if is_simple else 'No'
print(result)
'''
def is_simple(num):
    result = True
    for div in range(2, num):
        if num % div == 0:
            result = False
            break
    return 'Yes' if result else 'No'
    
print(is_simple(int(input('Укажите число '))))
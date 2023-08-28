'''
Найдите сумму цифр трехзначного числа.
Пример:
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)

number = int(input('Введите трехзначное число: '))
first_dig = number // 100
value = number % 100
second_dig = value // 10
third_dig = value % 10
print(f'Сумма цифр числа {number}: {first_dig + second_dig + third_dig}')
'''
a = {0: "Л", 1: "Н", 2: "Р", 3: "Т"}
k = 0
for i in range(0, len(a)):
    for j in range(0, len(a)):
        for g in range(0, len(a)):
            for m in range(0, len(a)):
                for n in range(0, len(a)):
                    k += 1 # k = k + 1
                    if k == 150:
                        print(a[i], a[j], a[g], a[m], a[n], end=" ")


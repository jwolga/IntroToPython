'''
Задача 12: Петя и Катя – брат и сестра. Петя – студент,
 а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000),
 а Катя должна их отгадать. Для этого Петя делает две подсказки.
   Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.. 
  '''   
import math      
sum = int(input('Укажите сумму двух задуманных чисел ')) 
mult = int(input('Укажите произведение двух задуманных чисел '))
D = sum * sum - 4 * mult  # вычисление дискриминанта
if D < 0:
    print('Не существует таких чисел ')
else:
    y = (sum + math.sqrt(D))/2  # вычисление первого корня
    if y < 0:
        y = (sum - math.sqrt(D))/2  # вычисление второго корня
    x = sum - y
    print(f'Петя загадал числа {x:.0f} и {y:.0f}')
                                                               
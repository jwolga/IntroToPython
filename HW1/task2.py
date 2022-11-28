'''
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. ¬ - Отрицание ⋁ - логическое "Или" ⋀ - логическое "И"
'''
print("x y z")
for x in range(0,2):
    for y in range(0, 2):
        for z in range(0, 2):
            if (not (x or y or z)) == (not(x) and not(y) and not(z)):
                print(x,y,z)

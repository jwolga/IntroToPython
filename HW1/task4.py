'''
Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
'''
quarter = int(input("Введите номер четверти: "))
if quarter < 1 or  quarter > 4:
    print("Невалидное значение")
elif quarter == 1:
    print("x ϵ (0; +∞) y ϵ (0; +∞)")
elif quarter == 2:
    print("x ϵ (-∞; 0) y ϵ (0; +∞)")
elif quarter == 3:
    print("x ϵ (-∞; 0) y ϵ (-∞; 0)")
elif quarter == 4:
    print("x ϵ (0; +∞) y ϵ (-∞; 0)")
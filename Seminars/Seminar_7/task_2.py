'''
2) - Дан список размеров(длина, ширина) эллипсов 
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
Напишите функцию find_farthest_orbit(list_of_orbits), 
которая находит площадь самого большого эллипса 
и возвращает кортеж с его размерами.
Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b – длины и ширина осей эллипса
-   Площадь кругов учитывать не нужно, т.е если у эллипса a == b, то это круг.
При решении задачи используйте списочные выражения.
Гарантируется, что самый большой эллипс всего один.
'''
import math
def find_farthest_orbit(list_of_orbits):
    res = filter(lambda el : el[0] != el[1], list_of_orbits)
    max_s = 0
    max_orbit = list_of_orbits[0]
    for el in res:
        s = math.pi*el[0] * el[1]
        if s > max_s:
            max_s = s
            max_orbit = el
    return max_orbit 
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
orbit = find_farthest_orbit(orbits)   
print(orbit)

def find_farthest_orbit(list_of_orbits):
    sizes = list(filter(lambda item : item[0] != item[1], list_of_orbits))
    areas = list(map(lambda item : 3.14 * item[0] * item[1], sizes))
    maximum = areas[0]
    imax = 0
    for i, area in enumerate(areas[1:], 1):
        if area > maximum:
            maximum = area
            imax = i
        # maximum = max(maximum, area)
    return sizes[imax]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits))


# find_farthest_orbit(orbits)
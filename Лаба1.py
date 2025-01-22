from math import *

def s(x, y, z):
    return fabs(pow(x, (y/z)) - cbrt((y/x))) + (y - x) * (cos(y) - pow(z, 2)) / (1 + pow((y - x), 2))

x = float(input('Введите значение x -> '))
y = float(input('Введите значение y -> '))
z = float(input('Введите значение z -> '))
print('Вы ввели значение: x = ', x)
print('Вы ввели значение: y = ', y)
print('Вы ввели значение: z = ', z)
print('S = ', s(x, y, z))
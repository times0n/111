from math import *
import numpy as np

def cicle_for(x1, xn, delta, a, b):
    results = []  # Список для хранения результатов
    for x in np.arange(x1, xn, delta):
        y = b * log((a * x**2), exp(1)) + b * pow(log(x, exp(1)), 2)
        results.append(y)  # Добавляем результат в список
    return results

def cicle_while(x1, xn, delta, a, b):
    results = []  # Список для хранения результатов
    while x1 < xn - 0.3:
        y = b * log((a * x1**2), exp(1)) + b * pow(log(x1, exp(1)), 2)
        results.append(y)  # Добавляем результат в список
        x1 += delta
    return results

def main():
    x1 = 1.0
    xn = 4.0
    delta = 0.3
    a = 4.3
    b = 5.4
    print('Результаты для цикла for: ', cicle_for(x1, xn, delta, a, b))
    print('Результаты для цикла while: ', cicle_while(x1, xn, delta, a, b))

if __name__ == '__main__':
    main()  # Запуск основной функции
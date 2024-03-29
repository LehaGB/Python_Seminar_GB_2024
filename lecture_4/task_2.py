"""
Решение через Lambda.
Задача для самостоятельной работы
1.В списке хранятся числа.Нужно выбрать только четные числа и составить 
список пар
(число, квадрат числа)
Пример 1 2 3 5 8 15 23 38
На выходе: [(2, 4)(8, 64)(38, 1444)]
"""


data = [1, 2, 3, 5, 8, 15, 23, 38]

res = map(int, data)
print(res)

res = filter(lambda x: x % 2 == 0, res)
print(res)

res = list(map(lambda x: (x, x ** 2), res))
print(res)

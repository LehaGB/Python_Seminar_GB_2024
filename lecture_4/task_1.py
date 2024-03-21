"""
Задача для самостоятельной работы
1.В списке хранятся числа.Нужно выбрать только четные числа и составить 
список пар
(число, квадрат числа)
Пример 1 2 3 5 8 15 23 38
На выходе: [(2, 4)(8, 64)(38, 1444)]
"""
from typing import List
list_1 = [1, 2, 3, 5, 8, 15, 23, 38]
res = list()


def square_number(list_1: List[int]) -> tuple:
    for i in list_1:
        if i % 2 == 0:
            res.append((i, i ** 2))
    return res


if __name__ == '__main__':
    print(square_number(list_1))

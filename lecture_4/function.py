"""
Работа с функциями.
"""


def calc_plus(a, b):
    return a + b


def calk_multiplication(a, b):
    return a * b


# Аргумент op - это ссылка на мутоды, а x, y на переменные
def math(op, x, y):
    print(op(x, y))


math(calc_plus, 8, 7)
math(calk_multiplication, 7, 7)

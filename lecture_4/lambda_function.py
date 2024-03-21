"""
Лямбда функции.
"""


def calk_multiplication(a, b):
    return a * b


# Аргумент op - это ссылка на мутоды, а x, y на переменные
def math(op, x, y):
    print(op(x, y))


math(lambda a, b: a + b, 8, 7)
math(calk_multiplication, 7, 7)

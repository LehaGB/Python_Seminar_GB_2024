"""
Кортежи - это неизменяемый список.
"""

t = ()
print(type(t))  # Класс 'tuple' - кортеж.

t = (1, 3, 6, 4,)  # При инициализации котрежа в конце должна стоять запятая, ОБЯЗАТЕЛЬНО!
print(type(t))

v = [1, 3, 8]
print(v)
print(type(v))  # Список.

v = tuple(v)
print(v)
print(type(v))  # Явное приведение списка в кортеж.

a, b, c = v  # Множестаенное присваивание.(распаковка кортежа)
print(a, b, c)

"""
Операции со множеством в Python.

"""
# Инициализация множества.
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}

c = a.copy()
print(c)                      # {1, 2, 3, 5, 8} - Копируем

u = a.union(b)
print(u)                      # {1, 2, 3, 5, 8, 13, 21} - Объединение двух множеств.

i = a.intersection(b)
print(i)                      # {8, 2, 5} - Выводим из двух множеств повторяющиеся элементы.(пересечение)

d1 = a.difference(b) 
print(d1)                     # Разность множества а с b

br = b.difference(a)
print(br)                     # Разность множества b с a

q = a.union(b).difference(a.intersection(b))
print(q)
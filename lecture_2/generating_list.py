"""
Генерирующий список
"""

# Список
# list_1 = []
# for i in range(1, 31):
#     list_1.append(i)
# print(list_1, end=" ")

# print('------------------------------')
# # Генерирующий список
# list_2 = [i for i in range(1, 31)]
# print(list_2, end=" ")


# Только четные числа.
list_1 = [i for i in range(1,31) if i % 2 == 0]
print(list_1)

print()

# Решили создать пары каждому из чисел(кортежи).
# Квадрат числа.
list_2 = [(i, i * i) for i in range(1, 11) if i % 2 == 0]
print(*list_2)

print()

# также можно умножать, делить , прибавлять, вычитать.Например, умножить значение на 2.
list_3 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_3)

"""
Функция filter.
"""

data = [15, 65, 36, 175, 29, 45, 8]
res = list(filter(lambda x: x % 10 == 5, data))
print(sorted(res))

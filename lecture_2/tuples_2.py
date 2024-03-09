"""
Разница между списками и кортежами.
"""
# Кортеж.
t = (1, 3, 5, 6,)

for i in range(len(t)):
    print(f'{t[i]}')
# t[0] = 2  # TypeError: 'tuple' object does not support item assignment
    
# Список.
t_1 = [1, 3, 5, 6]
print(f'{t_1} -> список')
t_1[0] = 3
print(f'{t_1} -> измененный список')
"""
Срезы в списке.
"""
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Создаем список и инициализируем.

print(list_1[0])                          # Выводим первый эелемент -> 1
print(list_1[1])                          # Выводим второй эелемент -> 2
print(list_1[-1])                         # Выводим последний элемент -> 10
print(list_1[-5])                         # Выводим 5-ый элемент с конца -> 6
print(list_1[:])                          # Выводим список польностью -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[:2])                         # Выводи первых два элемента включительно -> [1, 2]
print(list_1[-2:])                        # Выводим два элемента с конца -> [9, 10]
print(list_1[2:9])                        # Выводим от 2-го до 9-го элемента -> [3, 4, 5, 6, 7, 8, 9]
print(list_1[6:-18])                      # Иакого элемента нету, пустой список -> []
print(list_1[::6])                        # От начало до конца с шагом 6 -> [1, 7]
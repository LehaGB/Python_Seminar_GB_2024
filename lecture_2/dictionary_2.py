dictionary = {}
dictionary = {'up': '^', 'left' : '<-', 'down' : '|', 'right' : '->'}
print(dictionary)                         # {'up': '^', 'left': '<-', 'down': '|', 'right': '->'}
dictionary[123] = 789
print(dictionary)
print(dictionary['left'])                 # <-
# типы ключей могут отличаться

print(dictionary['up'])                    # ^
# типы ключей могут отличаться
dictionary['left'] = '<='                  # заменили значение у ключа left -> '<='
print(dictionary['left'])

#print(dictionary['type'])                  # KeyError 'type'
del dictionary['left']                     # Удаление элемента.

# 1-ый способ.
for item in dictionary:
    print('{}: {}' .format(item, dictionary[item]))

print('=====================================')
# 2-ый способ.(можно и так)
for (v, k) in dictionary.items():  # dictionary.items - это список содержащий кортежи по парам(ключ: значение).
    print(f'{v}: {k}')
"""
Множества - содержат в себе уникальные элементы, не обязательно упорядочные.
"""
colors = {'red', 'green', 'blue'}
print(*colors)                    # {'red', 'blue', 'green'}
colors.add('red') 
print(colors)                     # {'red', 'blue', 'green'}
colors.add('gray')
print(colors)                     # {'gray', 'blue', 'red', 'green'}
colors.remove('red')
print(colors)                     # {'green', 'gray', 'blue'}
#colors.remove('red')
#print(colors)                    # KeyError: 'red'
colors.discard                    # ok - если есть , то удаляет , если нет , то пропускает.
print(colors)                     # {'green', 'gray', 'blue'}
colors.clear()                     # {}
print(colors)                     # set


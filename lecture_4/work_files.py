"""
Работа с файлами.
"""

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors)
# data.close()

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 5\n')
# print(56)

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

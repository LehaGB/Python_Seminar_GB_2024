# Цикл for и метод Range.
# Вложенные циклы.

a = 'qwerty'

for i in a:
    print(i, end=" ")
print(' ')

line = ""
for a in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)
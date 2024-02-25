# Привидение типов.
c = 5.98
print(c)
print(type(c))

c = int(c)
print(c)
print(type(c))

c = str(c)
print(c + '467')
print(type(c))

# Так делать нельзя.Это ошибка.
str1 = 'fjfj'
str1 = int(str1)
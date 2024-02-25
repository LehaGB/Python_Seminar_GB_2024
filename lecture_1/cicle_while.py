# Цикл while и выход из него (break).
# break - не рекомендуется использовать.
i = 0
while i < 5:
    if i == 3:
        break 
    i = i + 1
else:
    print('Пожалуй')
    print('Хватит')
print(i)
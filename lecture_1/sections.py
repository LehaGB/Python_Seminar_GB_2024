text = 'съешь ещё этих мягких французких булок'
print(text[0])                               # первый элемет -> c
print(text[1])                               # второй элемент -> ъ
print(text[len(text) - 1])                   # последний элемент -> к
print(text[-5])                              # Пятый элеметн с конца строки -> б
print(text[:])                               # Полностью строка -> 'съешь ещё этих мягких французких булок'
print(text[:2])                              # Печатаем первые две буквы -> съ
print(text[len(text) - 2:])                  # Печатаем последние две буквы -> ок
print(text[2:9])                             # Срез от второго символа(включительно), по 9 символ(не включительно) -> ешь ещё
print(text[6:-18])                           # Срез от 6 по -18 символы -> ещё этих мягких
print(text[0:len(text):6])                   # Начинаем с нулевого и каждый 6(с шагом 6) элемент строки -> сеикаио
print(text[::6])                             # Начиная с начала и до конца с шагом 6 -> сеикаио
print(text[10:])                             # Печатаем от 10 символа и до конца строки -> этих мягких французких булок
text = text[2:9] + text[-5] + text[:2]       # Начинаем с 2 по 9, потом -5 элемент и первые две буквы -> ешь ещёбсъ
print(text)   
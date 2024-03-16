# * означает, что неограниченное количество аргументов.
def sum_str(*args):
    res = ''
    for i in args:
        res += i
    return res
print(sum_str('q', 'e', 'f', 'g'))
print(sum_str(1, 3, 5, 8))
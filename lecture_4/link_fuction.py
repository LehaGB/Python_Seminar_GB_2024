"""
Ссылка на функцию.
"""


def link_f(x):
    return x * x


link = link_f
print(link_f(5))
print(link(6))

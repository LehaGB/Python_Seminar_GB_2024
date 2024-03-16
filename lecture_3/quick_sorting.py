"""
Быстрая сортировака.
"""
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greator = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greator)

print(quick_sort([1, 5 ,2, 8, 14, 54, 7, 96, 12, 23, 65, 11]))
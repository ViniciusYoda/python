def quickSort(array):
    length = len(array)
    if length <= 1:
        return array
    else:
        pivot = array.pop()

    items_greater = []
    items_lower = []

    for item in array:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quickSort(items_lower) + [pivot] + quickSort(items_greater)

array = [8, 7, 5, 3, 1, 2, 9, 6, 4]
qs = quickSort(array)
print(qs)
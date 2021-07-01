def merge(a: list, b: list) -> list[int]:
    length = len(a) + len(b)
    merged = []
    a_index, b_index = 0, 0

    # Add positive infinity to both lists as a guard, for convenience
    a.append(float('inf'))
    b.append(float('inf'))

    while a_index + b_index < length:
        if a[a_index] <= b[b_index]:
            merged.append(a[a_index])
            a_index += 1
        else:
            merged.append(b[b_index])
            b_index += 1

    return merged


def merge_sort(arr: list) -> list[int]:
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2

    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)


print(merge_sort([9, 2, 5, 6, 4, 3, 10]))

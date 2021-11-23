from random import randint

def bubble_sort(a: list) -> list:
    len_a = len(a)
    while len_a > 0:
        for i in range(len_a - 1):
            if a[i] > a[i + 1]:
                a[i + 1], a[i] = a[i], a[i + 1]

        len_a -= 1

    return a


def selection_sort(a: list) -> list:
    len_a = len(a)
    for i in range(len_a):
        min = i
        for j in range(i+1, len_a):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]
    
    return a


def insert_sort(a: list) -> list:
    len_a = len(a)
    for i in range(len_a):
        j = i
        for j in range(i, 0, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
    
    return a


def shell_sort(a: list) -> list:
    # every h, insert sort
    len_a = len(a)
    h = 1
    while(h < len_a//3):
        h = 3*h + 1

    while(h >= 1):
        for i in range(h, len_a):
            for j in range(i, h - 1, -h):
                if a[j] < a[j-h]:
                    a[j], a[j-h] = a[j-h], a[j]
        h = h//3
    
    return a

# merge sort
def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    # the left values，append to the results
    result += left
    result += right
    return result


def merge_sort(a: list) -> list:
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]

    return merge(merge_sort(left), merge_sort(right))


# quick sort
def partition(a, low, hi):
    i = low + 1
    j = hi
    
    v = a[randint(low, hi)]

    while(True):
        while(a[i] < v):
            i += 1
            if i == hi:
                break
        while(a[j] > v):
            j -= 1
            if j == low:
                break
        if i >= j:
            break

        a[i], a[j] = a[j], a[i]

    a[low], a[j] = a[j], a[low]
    return j

def q_sort(a, low, hi):
    if low >= hi:
        return
    j = partition(a, low, hi)
    q_sort(a, low, j-1)
    q_sort(a, j+1, hi)

# partition(list('kratelepuimqcxos'), 0, 15)
def quick_sort(a: list) -> list:
    if len(a) <= 1:
        return a
    hi = len(a) - 1
    q_sort(a, 0, hi)

    return a

# print(quick_sort(list('kratelepuimqcxos')))
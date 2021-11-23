

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

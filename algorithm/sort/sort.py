

def bubble_sort(a: list) -> list:
    len_a = len(a)
    while len_a > 0:
        for i in range(len_a - 1):
            if a[i] > a[i + 1]:
                a[i + 1], a[i] = a[i], a[i + 1]

        len_a -= 1

    return a


def insert_sort(a: list) -> list:
    len_a = len(a)
    for i in range(len_a):
        for j in range(i+1, len_a):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    
    return a
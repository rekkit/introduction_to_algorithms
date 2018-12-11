import numpy as np

v = [10, 200, 6, 1000, 5, 7, 30, 1, -1]


def partition(a, p, r):
    if p == r:
        return p

    x = a[r]
    i = p - 1
    for j in range(p, r):
        if x >= a[j]:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]

    return i + 1

def random_partition(a, p, r):
    if p == r:
        return p

    rand_i = np.random.randint(p, r + 1)
    a[r], a[rand_i] = a[rand_i], a[r]
    x = a[r]
    i = p - 1

    for j in range(p, r):
        if x >= a[j]:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]

    return i + 1


def quicksort(v, p, r):
    if p < r:
        q = partition(v, p, r)
        if q - 1 > p:
            quicksort(v, p, q - 1)
        if r > q:
            quicksort(v, q, r)


quicksort(v, 0, len(v) - 1)
v

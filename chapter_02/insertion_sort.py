v = [1, -1, 2, 3, -5, 0, 1]


def insertion_sort(v):
    w = v[:]

    for i in range(len(w) - 1):
        j = i
        x = w[j + 1]

        while w[j] > x and j >= 0:
            w[j + 1] = w[j]
            j -= 1

        w[j + 1] = x

    return w


insertion_sort(v)

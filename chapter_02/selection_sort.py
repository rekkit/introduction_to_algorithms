v = [1, -1, 2, 3, -5, 0, 1]


def selection_sort(v):
    w = v[:]

    for i in range(len(w) - 1):
        current_extreme = w[i]
        extreme_index = i

        for j in range(i + 1, len(w)):
            if current_extreme > w[j]:
                current_extreme = w[j]
                extreme_index = j

        w[i], w[extreme_index] = current_extreme, w[i]

    return w


selection_sort(v)

w = [1, -1, 2, 3, -5, 0, 1]


def selection_sort(v):
    for i in range(len(v) - 1):
        current_extreme = v[i]
        extreme_index = i

        for j in range(i, len(v)):
            if current_extreme > v[j]:
                current_extreme = v[j]
                extreme_index = j

        v[extreme_index], v[i] = v[i], current_extreme


selection_sort(w)

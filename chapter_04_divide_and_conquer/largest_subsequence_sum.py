import numpy as np
v = [-10, -200, -6, -1000, -5, -7, -30]


def find_max_crossing_subarray(a, low, mid, high):
    l_sum = -np.inf
    max_left_i = mid
    s = 0
    for i in range(mid, low - 1, -1):
        s += a[i]
        if s > l_sum:
            l_sum = s
            max_left_i = i

    r_sum = -np.inf
    max_right_i = mid + 1
    s = 0
    for i in range(mid + 1, high):
        s += a[i]
        if s > r_sum:
            r_sum = s
            max_right_i = i

    return max_left_i, max_right_i, l_sum + r_sum


def find_max_subarray(a, low, high):
    if low + 1 == high:
        return low, high, a[low]
    else:
        mid = (high + low) // 2

        l_low, l_high, l_sum = find_max_subarray(a, low, mid)
        r_low, r_high, r_sum = find_max_subarray(a, mid, high)
        c_low, c_high, c_sum = find_max_crossing_subarray(a, low, mid, high)

        if l_sum >= r_sum and l_sum >= c_sum:
            return l_low, l_high, l_sum
        elif r_sum >= l_sum and r_sum >= c_sum:
            return r_low, r_high, r_sum
        else:
            return c_low, c_high, c_sum


find_max_subarray(v, 0, len(v))

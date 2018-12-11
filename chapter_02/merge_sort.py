t = [1, -2, 1, -3, -1, 2, 5, 10, -30]


def merge(a, p, q, r):
    v = a[p: q]
    w = a[q: r]
    n1 = q - p - 1
    n2 = r - q - 1

    if p == q:
        a[p:r] = w
        return None
    elif q == r:
        a[p:r] = v
        return None

    i = 0
    j = 0
    k = 0
    while i <= n1 and j <= n2:
        if v[i] < w[j]:
            a[p + k] = v[i]
            i += 1
        else:
            a[p + k] = w[j]
            j += 1
        k += 1

    if i > n1:
        a[p + k:r] = w[j:]
    else:
        a[p + k:r] = v[i:]


def merge_sort(a, p, r):
    if p < r - 1:
        q = (p + r) // 2
        merge_sort(a, p, q)
        merge_sort(a, q, r)
        return merge(a, p, q, r)


merge_sort(t, 0, len(t))

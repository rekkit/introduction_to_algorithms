t = [1, -2, 1, -3, -1, 2, 5, 10, -30]


class MergeSort:
    @staticmethod
    def _merge(a, p, q, r):
        v = a[p: q]
        w = a[q: r]

        i = 0  # used for iterating through v
        j = 0  # -/- w
        k = p  # -/- a[p: r]

        while i < len(v) or j < len(w):
            if i == len(v):
                a[k: r] = w[j:]
                break
            elif j == len(w):
                a[k: r] = v[i:]
                break

            if v[i] < w[j]:
                a[k] = v[i]
                i += 1
            else:
                a[k] = w[j]
                j += 1

            k += 1

    def _merge_sort(self, a, p, r):
        q = (r + p) // 2
        if p < q < r:
            self._merge_sort(a, p, q)
            self._merge_sort(a, q, r)
            self._merge(a, p, q, r)

    def merge_sort(self, v, copy=False):
        if copy:
            v = v[:]
        self._merge_sort(v, 0, len(v))

        return v if copy else None


ms = MergeSort()
ms.merge_sort(t, copy=True)

import numpy as np

w = [10, 200, 6, 1000, 5, 7, 30, 1, -1]


class QuickSort:
    @staticmethod
    def _partition(v, p, r):
        x = v[r - 1]
        i = p - 1

        for j in range(p, r):
            if x > v[j]:
                i += 1
                v[i], v[j] = v[j], v[i]
        v[i + 1], v[r - 1] = v[r - 1], v[i + 1]

        return i + 1

    def _quick_sort(self, v, p, r):
        q = self._partition(v, p, r)

        if p < q - 1:
            self._quick_sort(v, p, q)

        if q < r - 1:
            self._quick_sort(v, q, r)

    def sort(self, v):
        self._quick_sort(v, 0, len(v))


qs = QuickSort()
qs.sort(w)

import numpy as np

h = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
w = [10, 200, 6, 1000, 5, 7, 30, 1, -1]


class Heap:
    def __init__(self, a, comparison_f):
        self._a = a[:]
        self._heap_size = len(a)
        self._comparison_f = comparison_f

    @staticmethod
    def _parent(i):
        return (i - 1) // 2

    @staticmethod
    def _left(i):
        return 2*i + 1

    @staticmethod
    def _right(i):
        return 2*i + 2

    def _heapify(self, i):
        if i >= self._heap_size or i < 0:
            return None

        l_child = self._left(i)
        r_child = self._right(i)
        extreme_index = i

        if l_child < self._heap_size and self._comparison_f(self._a[l_child], self._a[i]):
            extreme_index = l_child

        if r_child < self._heap_size and self._comparison_f(self._a[r_child], self._a[extreme_index]):
            extreme_index = r_child

        if extreme_index != i:
            self._a[i], self._a[extreme_index] = self._a[extreme_index], self._a[i]
            self._heapify(extreme_index)

    def _create_heap(self):
        for i in range(self._heap_size // 2 - 1, 0, -1):
            self._heapify(i)


class MaxHeap(Heap):
    def __init__(self, a):
        super().__init__(a, lambda x, y: x > y)
        self._create_heap()

    def _increase_key(self, i, v):
        if i >= self._heap_size:
            raise ValueError(
                'You tried to increase the value of element {i} but there are {self._heap_size} elements in the heap.'
            )

        if self._a[i] > v:
            raise ValueError(
                'The provided value for element {i} of the heap is less that its current value.'
            )

        self._a[i] = v
        parent_i = self._parent(i)
        while parent_i >= 0 and v > self._a[parent_i]:
            self._a[parent_i], self._a[i] = v, self._a[parent_i]
            i = parent_i
            parent_i = self._parent(i)

    def insert(self, x):
        if self._heap_size + 1 > len(self._a):
            raise ValueError(
                'Heap overflow!'
            )

        self._heap_size += 1
        self._a[self._heap_size - 1] = -np.inf
        self._increase_key(self._heap_size - 1, x)

    def max(self):
        return self._a[0]

    def extract_max(self):
        self._a[0], self._a[-1] = self._a[-1], self._a[0]
        self._heap_size -= 1
        self._heapify(0)
        return self._a[-1]

    def sort(self):
        while self._heap_size > 0:
            self._a[0], self._a[self._heap_size - 1] = self._a[self._heap_size - 1], self._a[0]
            self._heap_size -= 1
            self._heapify(0)


mh = MaxHeap(h)

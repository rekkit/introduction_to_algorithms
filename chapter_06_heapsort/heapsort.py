import numpy as np

h = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
v = [10, 200, 6, 1000, 5, 7, 30, 1, -1]


class Heap:
    def __init__(self, a):
        self.a = a[:]
        self.heap_size = len(a)

    @staticmethod
    def left_child(i):
        return 2 * i + 1

    @staticmethod
    def right_child(i):
        return 2 * i + 2

    @staticmethod
    def parent(i):
        return (i - 1) // 2


class MaxHeap(Heap):
    def __init__(self, a):
        Heap.__init__(self, a)
        self.build_heap()

    def heapify(self, i):
        if i >= self.heap_size:
            return None

        l = self.left_child(i)
        r = self.right_child(i)

        if l <= self.heap_size - 1 and self.a[i] <= self.a[l]:
            max_index = l
        else:
            max_index = i
        if r <= self.heap_size - 1 and self.a[max_index] <= self.a[r]:
            max_index = r

        self.a[i], self.a[max_index] = self.a[max_index], self.a[i]
        if i != max_index:
            self.heapify(max_index)

    def build_heap(self):
        for i in range(self.heap_size // 2, 0 - 1, - 1):
            self.heapify(i)

    def sort_array(self):
        for i in range(self.heap_size):
            self.a[0], self.a[self.heap_size - 1] = self.a[self.heap_size - 1], self.a[0]
            self.heap_size -= 1
            self.heapify(0)

    def maximum(self):
        return self.a[0]

    def extract_maximum(self):
        if self.heap_size < 1:
            raise ValueError(
                "Heap size is less than 1."
            )

        mx = self.a[0]
        self.a[0], self.a[self.heap_size - 1] = self.a[self.heap_size - 1], self.a[0]
        self.heap_size -= 1
        del self.a[-1]
        self.heapify(0)

        return mx

    def increase_key(self, i, k):
        if self.a[i] > k:
            raise ValueError(
                "The value of the key 'k' is less than the current value of the key, which is %d." % self.a[i]
            )

        self.a[i] = k
        parent_idx = self.parent(i)

        while parent_idx >= 0 and self.a[parent_idx] < k:
            self.a[parent_idx], self.a[i] = k, self.a[parent_idx]
            i = parent_idx
            parent_idx = self.parent(i)

    def insert(self, val):
        self.heap_size += 1
        self.a.append(-np.inf)
        self.increase_key(self.heap_size - 1, val)


max_heap = MaxHeap(v)
max_heap.build_heap()
print(max_heap.a)
max_heap.extract_maximum()
print(max_heap.a)
max_heap.increase_key(2, 300)
print(max_heap.a)
max_heap.insert(11)
print(max_heap.a)

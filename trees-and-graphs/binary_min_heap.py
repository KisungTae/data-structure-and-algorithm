import math

class MinHeap:

    def __init__(self):
        self.heap = []

    def insert(self, data):
        self.heap.append(data)
        current = len(self.heap) - 1

        while self.heap[current] < self.heap[self.__parent(current)]:
            self.__swap(current, self.__parent(current))
            current = self.__parent(current)
    
    def pop(self):
        min = self.heap.pop(0)
        last = self.heap.pop(len(self.heap) - 1)
        self.heap.insert(0, last)
        self.__minify(0)
        return min
    
    def __minify(self, pos):
        if not self.__is_leaf(pos):

            current = self.heap[pos]
            size = len(self.heap)
            
            left = self.heap[self.__left_child(pos)]
            right = self.heap[self.__right_child(pos)]

            if left < current or right < current:
                if left < right:
                    self.__swap(pos, self.__left_child(pos))
                    self.__minify(self.__left_child(pos))
                else:
                    self.__swap(pos, self.__right_child(pos))
                    self.__minify(self.__right_child(pos))

            
    
    def __is_leaf(self, pos):
        size = len(self.heap)
        if pos >= math.trunc((size / 2)) and pos <= size:
            return True
        else:
            return False

    def __swap(self, l_pos, r_pos):
        self.heap[l_pos], self.heap[r_pos] = self.heap[r_pos], self.heap[l_pos]

    def __parent(self, pos):
        if pos == 0: return 0
        return math.trunc(pos / 2) 

    def __left_child(self, pos):
        return pos * 2

    def __right_child(self, pos):
        return pos * 2 + 1

    def print(self):
        print(self.heap)

min_heap = MinHeap()


min_heap.insert(7)
min_heap.insert(4)
min_heap.insert(6)
min_heap.insert(41)
min_heap.insert(8)
min_heap.insert(42)
min_heap.insert(5)


min_heap.print()
print(min_heap.pop())
min_heap.print()

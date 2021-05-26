# 3.5 Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
# an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array). The stack supports the following operations: push, pop, peek, and is Empty.

import sys

class Stack:

    def __init__(self):
        self.stack = []
    
    def add(self, data):
        self.stack.insert(0, data)

    def pop(self):
        return self.stack.pop(0)
    
    def is_empty(self):
        return len(self.stack) <= 0

    def peek(self):
        return self.stack[0]

    def print(self):
        print(self.stack)

    # def sort(self):
    #     buffer = Stack()
    #     max = None
    #     count = 0
    #     while not self.is_empty():
    #         data = self.pop()
    #         if max == None or data > max:
    #             max = data
    #         else:
    #             buffer.add(data)
    #         count += 1
        
    #     self.add(max)
        
    #     bigger = None
    #     smaller = None
    #     count -= 1

    #     self.print()
    #     buffer.print()
    #     print("count: " + str(count))

    #     while count >= 0:
            
    #         for i in range(count):
    #             data = buffer.pop()
    #             if bigger == None:
    #                 bigger = data
    #             elif data > bigger:
    #                 self.add(bigger)
    #                 bigger = data
    #             else:
    #                 self.add(data)

    #         for i in range(count - 1):
    #             data = self.pop()
    #             if smaller == None:
    #                 smaller = data
    #             if data > smaller:
    #                 buffer.add(smaller)
    #                 smaller = data
    #             else:
    #                 buffer.add(data)
            
    #         if not bigger == None: 
    #             self.add(bigger)
    #             bigger = None
            
    #         if not smaller == None:
    #             self.add(smaller)
    #             smaller = None
    #         count -= 2
    
        



stack = Stack()
stack.add(65)
stack.add(23)
stack.add(164)
stack.add(343)
stack.add(1)
stack.add(43)
stack.add(432)

def sort_answer():
    buffer = Stack()
    while not stack.is_empty():
        data = stack.pop()
        while not buffer.is_empty() and data < buffer.peek():
            stack.add(buffer.pop())
    
        buffer.add(data)
    
    while not buffer.is_empty():
        stack.add(buffer.pop())


sort_answer()
stack.print()
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

    def print(self):
        print(self.stack)

    def sort(self):
        buffer = Stack()
        max = None
        count = 0
        while not self.is_empty():
            data = self.pop()
            if max == None or data > max:
                max = data
            else:
                buffer.add(data)
            count += 1
        
        

        while count >= 0:
            

            count -= 1
        

        
    

        




stack = Stack()
stack.add(65)
stack.add(23)
stack.add(164)
stack.add(343)
stack.add(1)
stack.add(43)
stack.add(432)
stack.print()
stack.sort()


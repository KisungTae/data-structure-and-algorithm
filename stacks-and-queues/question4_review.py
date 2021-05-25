# 3.4 Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.


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



# class Queue:

#     def __init__(self):
#         self.stack = Stack()
#         self.buffer = Stack()
    
#     def add(self, data):
#         while not self.stack.is_empty():
#             self.buffer.add(self.stack.pop())
        
#         self.stack.add(data)

#         while not self.buffer.is_empty():
#             self.stack.add(self.buffer.pop())
    
#     def pop(self):
#         return self.stack.pop()

#     def print(self):
#         self.stack.print()


class Queue:

    def __init__(self):
        self.new_stack = Stack()
        self.old_stack = Stack()
    
    def add(self, data):
        self.new_stack.add(data)
    
    def shift_stack(self):
        if self.old_stack.is_empty():
            while not self.new_stack.is_empty():
                self.old_stack.add(self.new_stack.pop())

    def pop(self):
        self.shift_stack()
        return self.old_stack.pop()

    def print(self):
        self.new_stack.print()

queue = Queue()
queue.add(0)
queue.add(1)
queue.add(2)
queue.add(3)
queue.add(4)
queue.add(5)
queue.add(6)

print("pop: " + str(queue.pop()))







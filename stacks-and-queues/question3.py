import math

# 3.3 Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
# (that is, pop () should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt(int index) which performs a pop operation on a specific substack.

# class SetOfStack:

#     THRESHOLD = 3

#     def __init__(self):
#         self.stacks = []
#         self.size = 0

    
#     def add(self, data):
#         if self.size == 0:
#             self.stacks.append([None] * self.THRESHOLD)
#             self.stacks[0][0] = data
#             self.size += 1
#         else:
#             stack_index = math.trunc(self.size / self.THRESHOLD)
#             data_index = self.size % self.THRESHOLD
            
#             if stack_index >= len(self.stacks):
#                 self.stacks.append([None] * self.THRESHOLD)
#                 self.stacks[stack_index][0] = data
#             else:
#                 self.stacks[stack_index][data_index] = data
            
#             self.size += 1
    
#     def pop(self):
#         if self.size == 0:
#             return None
#         else:
#             self.size -= 1
#             stack = self.stacks[math.trunc(self.size / self.THRESHOLD)]
#             data = stack.pop()
#             if len(stack) == 0:
#                 self.stacks.pop()
#             return data

#     def pop_at(self, index):
#         print()
    

class SetOfStack:

    THRESHOLD = 3

    def __init__(self):
        self.stacks = []
    
    def add(self, data):
        stack = self.get_last_stack()
        if stack == None or len(stack) == self.THRESHOLD:
            stack = [data]
            self.stacks.append(stack)
        else:
            stack.append(data)

    def get_last_stack(self):
        if len(self.stacks) <= 0:
            return None
        else:
            return self.stacks[len(self.stacks) - 1]
    
    def pop(self):
        stack = self.get_last_stack()
        if stack != None:
            data = stack.pop()
            if len(stack) == 0:
                self.stacks.pop()
        
        return data
    
    def pop_at(self, index):
        stack = self.stacks[index]
        if stack != None:
            data = stack.pop()
            self.shift(index)

    def shift(self, start_index):
        for i in range(start_index, len(self.stacks) - 1):
            left = self.stacks[i]
            right = self.stacks[i + 1]

            while len(left) < self.THRESHOLD:
                left.append(right.pop(0))

        last_stack = self.get_last_stack()
        if len(last_stack) == 0:
            self.stacks.pop()
        
        



set_stack = SetOfStack()
set_stack.add(1)
set_stack.add(2)
set_stack.add(3)
set_stack.add(4)
set_stack.add(5)
set_stack.add(6)
set_stack.add(6)
set_stack.add(6)
set_stack.add(6)

print(set_stack.stacks)
set_stack.pop_at(0)
set_stack.pop_at(0)
set_stack.pop_at(0)
print(set_stack.stacks)
# set_stack.shift(1)

# set_stack.pop()
# set_stack.pop()
# set_stack.pop()
# set_stack.pop()


# print(set_stack.stacks)

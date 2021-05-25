# 3.2 Stack Min: How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.


# class MinStack:

#     def __init__(self):
#         self.stack = []
#         self.min_stack = []

#     def add(self, data):
#         self.stack.append(data)
#         self.min_stack.insert(self.min_index(data), data)
    
#     def pop(self):
#         data = self.stack.pop()
#         self.min_stack.remove(data)
#         return data

#     def min(self):
#         return self.min_stack[len(self.min_stack) - 1]

#     def min_index(self, data):
#         for i in range(len(self.min_stack)):
#             if data > self.min_stack[i]:
#                 return i
#         return len(self.min_stack) 



# min_stack = MinStack()
# min_stack.add(3)
# min_stack.add(4)
# min_stack.add(5)
# min_stack.add(6)
# min_stack.add(7)
# min_stack.add(8)
# min_stack.add(9)
# min_stack.add(9)


# print(min_stack.stack)

# print(min_stack.min_stack)

# print("pop: " + str(min_stack.pop()))

# print(min_stack.min_stack)

# print("min: " + str(min_stack.min()))





class MinStack:
    
    def __init__(self):
        self.stack = []
        self.min = []
    
    def add(self, data):
        self.stack.append(data)
        min = self.peek_min()
        if min < 0 or data <= min:
            self.min.append(data)

    def pop(self):
        if len(self.stack) <= 0:
            return None
        else:
            data = self.stack.pop()
            min = self.peek_min()
            if data == min:
                self.min.pop()
            return data


    def peek_min(self):
        if len(self.min) <= 0:
            return -1
        else:
            return self.min[len(self.min) - 1]



min_stack = MinStack()
min_stack.add(3)
min_stack.add(4)
min_stack.add(5)
min_stack.add(6)
min_stack.add(2)
min_stack.add(8)
min_stack.add(1)
min_stack.add(1)
min_stack.add(1)

print(min_stack.stack)
print(min_stack.min)

min_stack.pop()
min_stack.pop()
min_stack.pop()


print(min_stack.stack)
print(min_stack.min)

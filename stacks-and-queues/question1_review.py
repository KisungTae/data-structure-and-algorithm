# 3.1 Three in One: Describe how you could use a single array to implement three stacks.


class ArrStack:
    
    STACK_COUNT = 3

    def __init__(self):
        self.stack_infos = [StackInfo(), StackInfo(), StackInfo()]
        self.stack = []
    
    def add(self, index, data):
        stack_info = self.stack_infos[index]
        if stack_info.head < 0:
            new_head = len(self.stack)
            stack_info.head = new_head
            stack_info.size = stack_info.size + 1
            self.stack.insert(new_head, data)
        else:
            self.stack.insert(stack_info.head, data)
            stack_info.size = stack_info.size + 1
        
        self.update_head(stack_info.head, 1)
        
    def pop(self, index):
        stack_info = self.stack_infos[index]
        if stack_info.size <= 0:
            return None
        else:
            data = self.stack.pop(stack_info.head)
            self.update_head(stack_info.head, -1)
            stack_info.size = stack_info.size - 1
            return data

    def update_head(self, head, mask):
        for stack_info in self.stack_infos:
            if stack_info.head > head:
                stack_info.head = stack_info.head + mask

        
class StackInfo:

    def __init__(self):
        self.head = -1
        self.size = 0

    
arr_stack = ArrStack()
arr_stack.add(0, 'a1')
arr_stack.add(0, 'a2')
arr_stack.add(0, 'a3')
arr_stack.add(1, 'b1')
arr_stack.add(1, 'b2')
arr_stack.add(2, 'c1')
arr_stack.add(2, 'c2')


print(arr_stack.pop(0))
print(arr_stack.pop(1))
print(arr_stack.pop(2))
print(arr_stack.pop(2))
print(arr_stack.pop(2))
print(arr_stack.stack)


 
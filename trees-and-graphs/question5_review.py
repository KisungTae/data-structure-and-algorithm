from node import Node

# Validate BST: Implement a function to check if a binary tree is a binary search tree.


root = Node(10)
root.add(3)
root.add(14)
root.add(1)
root.add(2)
root.add(6)
root.add(8)
root.add(9)
root.add(20)
root.add(12)
root.add(7)


# arr = []

# def check(root):
#     if root is not None:
#         check(root.left)
#         arr.append(root.data)
#         check(root.right)


last_data = -10000

class Check:

    def __init__(self):
        self.last_data = None
        print()

    def check_answer(self, root):
        if root is None:
            return True

        if not self.check_answer(root.left):
            return False
        
        if self.last_data is not None and self.last_data > root.data:
            return False
        else:
            last_data = root.data

        if not self.check_answer(root.right):
            return False
        
        return True

print(str(Check().check_answer(root)))



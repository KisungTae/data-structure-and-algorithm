from node import Node

# First Common Ancestor: Design an algorithm and write code to find the first common ancestor
# of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
# necessarily a binary search tree.


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
root.print()

l_node = root.left.right.right
r_node = root.right.left

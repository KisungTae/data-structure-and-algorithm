from node import Node

# 4.6 Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
# binary search tree. You may assume that each node has a link to its parent.


root = Node(10)
root.add(3)
root.add(14)
root.add(1)
# root.add(2)
root.add(6)
root.add(8)
root.add(9)
root.add(20)
root.add(12)
root.add(7)


root.print()


given = root.right.right

def next_node(given):
    if given.right:
        return left_most(given.right)
    else: 
        return next_parent(given)


def left_most(root):
    while root.left is not None:
        root = root.left
    return root

def next_parent(root):
    while root is not None and root.parent is not None and root.parent.data < root.data:
        root = root.parent
    return root.parent

print("given: " + str(given.data))
next_node = next_node(given)
if next_node is None:
    print("no more next node")
else:
    print("next: " + str(next_node.data))

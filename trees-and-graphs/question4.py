from node import Node
import math
# Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
# this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
# node never differ by more than one.

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


def check(root):
    if root is None:
        return 0, False
    
    l_level, l_found = check(root.left)
    
    if l_found:
        return 0, True

    r_level, r_found = check(root.right)

    if r_found:
        return 0, True
    
    diff = abs(l_level - r_level)
    if diff > 1:
        return 0, True
    
    return max(l_level, r_level) + 1, False

MIN = -10

def check_answer(root):
    if root is None: 
        return -1
    
    l_height = check_answer(root.left)
    if l_height == MIN:
        return l_height

    r_height = check_answer(root.right)
    if r_height == MIN:
        return r_height
    
    diff = abs(l_height - r_height)
    if diff > 1:
        return MIN
    else:
        return max(l_height, r_height) + 1

root.print()
print(str(check_answer(root) != MIN))


import math
from node import Node
# Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an
# algorithm to create a binary search tree with minimal height.


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def make_binary(strt, end):
    if strt > end:
        return None

    mid = math.trunc((strt + end) / 2)
    root = Node(arr[mid])
    root.left = make_binary(strt, mid - 1)
    root.right = make_binary(mid + 1, end)
    return root


root = make_binary(0, len(arr) - 1)
root.display()


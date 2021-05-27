from node import Node
from linked_list import LinkedList
import math
# 4.3 List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
# at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

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

dic = {}

def travel(root, index):
    if not root == None:

        if index in dic:
            dic[index].add(root.data)
        else:
            dic[index] = LinkedList()
            dic[index].add(root.data)

        travel(root.left, index + 1)
        travel(root.right, index + 1)

root.print()
travel(root, 0)

for key in dic:
    dic[key].print_nodes()


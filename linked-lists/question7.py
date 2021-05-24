from linked_list import LinkedList
from linked_list import Node


# Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting
# node. Note that the intersection is defined based on reference, not value. That is, if the kth
# node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.


intersect = LinkedList()
intersect.add('q')
intersect.add('r')
intersect.add('s')
intersect.add('t')


left = LinkedList()
left.add('a')
left.add('b')
left.add('c')
left.add('d')
left.add('1')
left.add('2')
left.add('3')
left.add('4')
left.last.next = intersect.head

right = LinkedList()
right.add('g')
right.add('h')
right.add('i')
right.add('j')
right.last.next = intersect.head



left.print_nodes()
right.print_nodes()


def intersect():
    left_count = 0
    right_count = 0

    left_itr = left.head
    right_itr = right.head

    while left_itr != None:
        left_count += 1
        left_itr = left_itr.next

    while right_itr != None:
        right_count += 1
        right_itr = right_itr.next
    
    left_loop_count = left_count - right_count
    left_itr = left.head
    if left_loop_count > 0:
        for i in range (left_loop_count):
            left_itr = left_itr.next
    
    right_loop_count = right_count - left_count
    right_itr = right.head
    if right_loop_count > 0:
        for i in range (right_loop_count):
            right_itr = right_itr.next

    while left_itr != None and right_itr != None:
        if left_itr == right_itr:
            break
        left_itr = left_itr.next
        right_itr = right_itr.next
    
    return left_itr

intersect().print_nodes()

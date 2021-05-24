from linked_list import LinkedList
from linked_list import Node
import math
# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
# Output: 9 -> 1 -> 2. That is, 912.


first_number = LinkedList()
first_number.add(9)
first_number.add(9)
first_number.add(9)
first_number.print_nodes()

second_number = LinkedList()
second_number.add(1)
second_number.add(1)
second_number.add(1)
second_number.print_nodes()


def add(first_number, second_number):
    first_itr = first_number.head
    second_itr = second_number.head
    sum_head = None
    sum_tail = None

    regroup = 0
    while first_itr != None and second_itr != None:
        sum = first_itr.data + second_itr.data
        sum += regroup
        regroup = math.trunc(sum / 10)
        digit = sum % 10

        if sum_head == None:
            sum_head = Node(digit)
            sum_tail = sum_head
        else:
            new_node = Node(digit)
            sum_tail.next = new_node
            sum_tail = new_node

        first_itr = first_itr.next
        second_itr = second_itr.next

    while first_itr != None:
        sum = first_itr.data + regroup
        regroup = math.trunc(sum / 10)
        digit = sum % 10

        if sum_head == None:
            sum_head = Node(digit)
            sum_tail = sum_head
        else:
            new_node = Node(digit)
            sum_tail.next = new_node
            sum_tail = new_node
        first_itr = first_itr.next

    while second_itr != None:
        sum = second_itr.data + regroup
        regroup = math.trunc(sum / 10)
        digit = sum % 10

        if sum_head == None:
            sum_head = Node(digit)
            sum_tail = sum_head
        else:
            new_node = Node(digit)
            sum_tail.next = new_node
            sum_tail = new_node
        second_itr = second_itr.next
    
    if regroup > 0:
        new_node = Node(regroup)
        sum_tail.next = new_node
        sum_tail = new_node

    sum_head.print_nodes()

add(first_number, second_number)




l_num = LinkedList()
l_num.add(9)
l_num.add(9)
l_num.add(9)
l_num.print_nodes()

r_num = LinkedList()
r_num.add(1)
r_num.add(1)
r_num.add(1)
r_num.print_nodes()

def add_forward(l_num, r_num):
    l_head = l_num.head
    r_head = r_num.head

    regroup_head = None
    sum_head = None

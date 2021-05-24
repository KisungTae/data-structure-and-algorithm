from linked_list import LinkedList

# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8


linked_list = LinkedList()
linked_list.add(90)
linked_list.add(2)
linked_list.add(31)
linked_list.add(7)
linked_list.add(8)
linked_list.add(9)
linked_list.add(55)
linked_list.add(12)
linked_list.add(4)
linked_list.print_nodes()


def partition(k):
    left_head = None
    left_tail = None
    right_head = None
    right_tail = None

    head = linked_list.head

    while head != None:
        next_node = head.next

        if head.data < k:
            if left_head == None:
                left_head = head
                left_tail = left_head
            else:
                left_tail.next = head
                left_tail = head
        else:
            if right_head == None:
                right_head = head
                right_tail = right_head
            else:
                right_tail.next = head
                right_tail = head

        head = next_node
    
    linked_list.head = left_head
    left_tail.next = right_head
    right_tail.next = None    

partition(6)
linked_list.print_nodes()

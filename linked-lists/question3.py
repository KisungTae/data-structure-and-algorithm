from linked_list import LinkedList

# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.
# EXAMPLE
# lnput:the node c from the linked list a->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like a ->b->d- >e- >f

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


def remove_middle(middle_node):
    while middle_node.next.next != None:
        middle_node.data = middle_node.next.data
        middle_node = middle_node.next

    if middle_node.next != None:
        middle_node.data = middle_node.next.data
        middle_node.next = None

    

middle_node = linked_list.head.next.next.next.next
print("middle_node: " + str(middle_node.data))
remove_middle(middle_node)
linked_list.print_nodes()

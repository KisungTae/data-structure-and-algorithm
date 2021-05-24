from linked_list import LinkedList

# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.


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


def kthToTheLast(k):
    head = linked_list.head
    tail = linked_list.head

    count = 1
    while head != None and count < k:
        count += 1
        head = head.next

    if (head == None):
        return None

    print("head: " + str(head.data))
    print("tail: " + str(tail.data))
    
    while head.next != None:
        head = head.next
        tail = tail.next
    
    return tail


k = 0
node = kthToTheLast(k)

linked_list.print_nodes()

if node == None: 
    print("there is no " + str(k) + "th node")
else: 
    print(str(k) + "th node is " + str(node.data))






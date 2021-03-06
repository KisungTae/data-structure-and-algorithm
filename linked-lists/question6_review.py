from linked_list import LinkedList

# 2.6 Palindrome: Implement a function to check if a linked list is a palindrome.



palindrome = LinkedList()
palindrome.add('a')
palindrome.add('b')
palindrome.add('c')
palindrome.add('h')
palindrome.add('c')
palindrome.add('b')
palindrome.add('a')
palindrome.print_nodes()


def checkIfPalindrome():
    head = palindrome.head
    runner = head.next

    left = []
    isOdd = True

    while runner != None:
        left.append(head.data)
        head = head.next

        runner = runner.next
        if (runner != None):
            isOdd = True
            runner = runner.next
        else:
            isOdd = False
    
    left_index = len(left) - 1
    if isOdd:
        head = head.next
    
    while head != None and left_index >= 0:
        if left[left_index] != head.data:
            return False
        
        head = head.next
        left_index -= 1
    
    return True


def answer():

    left = []

    fast = palindrome.head
    slow = palindrome.head

    while fast != None and fast.next != None:
        left.append(slow.data)
        fast = fast.next
        slow = slow.next
    
    if fast != None:
        slow = slow.next
    
    while slow != None:
        left_pop = left.pop()
        print("left_pop: " + left_pop)
        if left_pop != slow.data:
            return False
        slow = slow.next
    
    return True



print("is palindrome: " + str(answer()))
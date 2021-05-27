class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    def print_nodes(self):
        iterator = self
        data = []
        while iterator != None:
            data.append(str(iterator.data))
            if (iterator.next != None):
                data.append(" --> ")
            iterator = iterator.next
        print("".join(data))


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def add(self, data):
        new_node = Node(data)
        if (self.head == None):
            self.head = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            new_node.prev = self.last
            self.last = new_node

    def print_nodes(self):
        iterator = self.head
        data = []
        while iterator != None:
            data.append(str(iterator.data))
            if (iterator.next != None):
                data.append(" --> ")
            iterator = iterator.next
        print("".join(data))


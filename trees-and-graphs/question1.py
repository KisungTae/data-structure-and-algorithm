# Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
# route between two nodes.


class Node:

    def __init__(self, data):
        self.data = data
        self.children = []
        self.visited = False
    

class Graph:

    def __init__(self):
        self.nodes = []
    
    def print(self):
        data = []
        for node in self.nodes:
            data.append(node.data)
            data.append(" --> ")
            for child in node.children:
                data.append(child.data)
                data.append(' ')
            
            print("".join(data))
            data.clear()




graph = Graph()
node_1 = Node('a')
node_2 = Node('b')
node_3 = Node('c')
node_4 = Node('d')
node_5 = Node('e')
node_6 = Node('f')

node_1.children.append(node_2)
node_1.children.append(node_3)
node_2.children.append(node_3)
node_3.children.append(node_1)
node_3.children.append(node_4)
node_3.children.append(node_5)
node_4.children.append(node_2)
node_5.children.append(node_1)
node_5.children.append(node_6)


graph.nodes.append(node_1)
graph.nodes.append(node_2)
graph.nodes.append(node_3)
graph.nodes.append(node_4)
graph.nodes.append(node_5)
graph.nodes.append(node_6)

graph.print()


def find_route(s_data, e_data):
    start = get_node(s_data)
    end = get_node(e_data)

    if start == None or end == None:
        return False
    else:
        queue = [start]

        while len(queue) > 0:
            curr = queue.pop(0)
            if curr.data == e_data:
                return True

            curr.visited = True
            
            for child in curr.children:
                if not child.visited:
                    queue.append(child)
         
        return False

    
def get_node(data):
    for node in graph.nodes:
        if node.data == data:
            return node
    
    return None

s_data = 'b'
e_data = 'd'
print("is there a route between " + s_data + " and " + e_data + " : " + str(find_route(s_data, e_data)))
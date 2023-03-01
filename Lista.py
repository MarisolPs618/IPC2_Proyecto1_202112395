class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Clase LinkedList para manejar la lógica de la lista
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def traverse(self):
        current_node = self.head
        while current_node is not None:
            yield current_node
            current_node = current_node.next
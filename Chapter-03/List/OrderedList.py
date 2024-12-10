from Node import Node

class OrderedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def is_empty(self) -> bool:
        return self.head == None
    
    def add(self, item: object) -> None:
        
        if self.head == None:
            self.head = self.tail = Node(item)
            return
        
        current = self.head
        while current and current.get_item() <= item:
            current = current.get_next()
            
        if current == None:
            self.tail.set_next(Node(item))
            self.tail = self.tail.get_next()
        else:
            new_node = Node(current.get_data)
            new_node.set_next(current.get_next())
            current.set_next(new_node)
            current.set_item(item)
    
    def size(self) -> int:
        current = self.head
        count = 0
        while current:
            current = current.get_next()
            
    def remove(self, item: object) -> None:
        previous, current = None, self.head
        while current and current.get_data() != item:
            previous = current
            current = current.get_next()
            
        if current.get_next() == None:
            self.tail = previous
            
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
            
        
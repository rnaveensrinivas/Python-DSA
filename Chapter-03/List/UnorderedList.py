from Node import Node

class UnorderedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def is_empy(self):
        return self.head == None
    
    def add(self, data: object) -> None:
        new_node = Node(object)
        if self.tail == None:
            self.tail = new_node
        new_node.set_next(self.head)
        self.head = new_node
        
    def size(self) -> int:
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.get_next
        return count
    
    def search(self, item: object) -> bool:
        current = self.head
        while current:
            if current.get_data() == item:
                return True
            elif current.get_data() > item:
                return False
            current = current.get_next()
            
        return False
    
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
            
    def append(self, item: object) -> None:
        
        # O(n)
        # current = self.head
        # while current.get_next():
        #     current = current.get_next()
        
        # current.set_next(Node(item))
        
        # O(1)
        self.tail.set_next(Node(item))
        self.tail = self.tail.get_next
        
    
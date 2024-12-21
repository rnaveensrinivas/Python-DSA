# The linked list implementation given above is called a singly linked list 
# because each node has a single reference to the next node in sequence. 
# An alternative implementation  is known as a doubly linked list. In this 
# implementation, each node has a reference  to the next node 
# (commonly called next) as well as a reference to the preceding node 
# (commonly called back). The head reference also contains two references, 
# one to the first node in the linked list and one to the last. Code this 
# implementation in Python.

class Node: 
    def __init__(self, data: object = None, 
                 prev: 'Node' = None, 
                 next: 'Node' = None):
        self.data = data
        self.prev= prev
        self.next = next
        
class DoublyLinkedList:
    def __init__(self): 
        self.head = None
        self.tail = None
        self.size_count = 0
    
    def append(self, data: object) -> None:
        if not self.head:
            self.head = self.tail = Node(data)
        else:
            self.tail.next = Node(data=data, prev=self.tail)
            self.tail = self.tail.next
        self.size_count += 1
    
    def extend(self, l: list[object]) -> None:
        
        for data in l: 
            self.append(data)
    
    def clear(self) -> None:
        self.head = self.tail = None
        self.size_count = 0
        
    def count(self, x: object) -> int:
        counter = 0
        current = self.head
        while current:
            if current.data == x:
                counter += 1
            current = current.next
        return counter
    
    def reverse(self) -> None:
        
        if self.__len__() == 1:
            return

        previous = None
        current = self.head
        upcoming = self.head.next
        
        while current:
            current.next = previous
            current.prev = upcoming
            previous = current
            current = upcoming
            upcoming = upcoming.next
        
        self.head, self.tail = self.tail, self.head
    
    def copy(self) -> 'DoublyLinkedList':
        ret = DoublyLinkedList()
        current = self.head
        while current:
            ret.append(current.data)
            current = current.next
        return ret
    
    def __len__(self) -> int:
        return self.size_count
    
    def pop_end(self) -> object:
        if self.__len__() == 1:
            ret = self.tail.data
            self.head = self.tail = None
        else:
            ret = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None
        
        self.size_count -= 1
        return ret
    
    def pop_start(self) -> object:
        
        if self.__len__() == 1: 
            ret = self.head.data
            self.head = self.tail = None
        else:
            ret = self.head.data
            self.head = self.head.next
            self.head.prev = None
        
        self.size_count -= 1
        return ret
    
    def pop(self, i: int = None) -> object:
        if self.__len__() == 0:
            raise IndexError("Cannot pop() from empty DoublyLinkedList")
        
        if i is None:
            return self.pop_end()
        
        if i < 0: 
            i = self.__len__() + i
            if i < 0:
                raise IndexError("pop() index out of range")
        elif i >= self.__len__(): 
            raise IndexError("pop() index out of range")
        
        if i == 0:
            return self.pop_start()
        elif i == self.__len__() - 1:
            return self.pop_end()
        else:
            current = self.head
            while current and i > 1:
                current = current.next
                i -= 1
            ret = current.next.data
            current.next = current.next.next
            if current.next: 
                current.next.prev = current
            self.size_count -= 1
        
        return ret
    
    def remove(self, x: object) -> None:
        if self.__len__() == 0: 
            raise IndexError("Cannot remove from empty list")
        
        current = self.head
        previous = None
        while current and current.data != x:
            previous = current
            current = current.next
            
        if not current: 
            raise ValueError("Element not found in list")
        
        if not previous:
            if self.__len__() == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        elif current == self.tail:
            self.tail = previous
            previous.next = None
        else:
            previous.next = current.next
            if previous.next:
                previous.next.prev = previous
        
        self.size_count -= 1
    
    def insert_head(self, data: object) -> None:
        if self.head == None:
            self.head = self.tail = Node(data)
        else:
            self.head = Node(data, next=self.head)
            self.head.next.prev = self.head
            
        self.size_count += 1
        
    def insert(self, i: int, data: object) -> None:
        if i is None or data is None:
            raise ValueError("Invalid argument passed")
        
        if i < 0: 
            i = self.__len__() + i
            if i < 0:
                self.insert_head(data)
        elif i >= self.__len__(): 
            self.append(data)
        
        if i == 0:
            return self.insert_head()
        elif i == self.__len__() - 1:
            return self.append(data)
        else: 
            current = self.head
            while current and i > 1:
                current = current.next
                i -= 1
            new_node = Node(data, current, current.next)
            current.next = new_node
            if new_node.next:
                new_node.next.prev = new_node
            
            self.size_count += 1
        
    def get_list(self) -> list[object]:
        ret = []
        current = self.head
        while current: 
            ret.append(current.data)
            
        return ret
    
    def __str__(self) -> str:
        return str(self.get_list())
    
    def index(self, data, start=None, end=None):
        
        counter = 0
        if not start or start <= 0:
            start = 0
            
        current = self.head
        while current and counter <= start:
            counter += 1
            current = current.next
        
        if not current:
            return -1
        
        if not end or end >= self.__len__(): 
            end = self.__len__()-1
        
        while current and counter <= end and current.data != data:
            counter += 1
            current = current.next
        
        if not current: 
            return -1
        elif counter > end: 
            return -1
        else:
            return counter

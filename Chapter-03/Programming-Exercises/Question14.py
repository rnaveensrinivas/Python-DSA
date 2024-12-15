# Modify the list classes to allow duplicates. Which methods will be 
# impacted by this change?

class Node: 
    def __init__(self, data: object = None, next: 'Node' = None):
        self.data = data
        self.next = next
        
class List:
    def __init__(self): 
        self.head = None
        self.tail = None
        self.size_count = 0
    
    def append(self, data: object) -> None:
        if not self.head:
            self.head = self.tail = Node(data)
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        self.size_count += 1
    
    def extend(self, l: list[object]) -> None:
        
        for data in l: 
            self.append(data)
    
    def clear (self) -> None:
        self.head = self.tail = None
        
    def count(self, x: object) -> None:
        counter = 0
        current = self.head
        while current:
            if current.data == x:
                counter += 1
            current = current.next
        return counter
    
    def reverse(self) -> None:
        self.head, self.tail = self.tail, self.head
    
    def copy(self) -> 'List':
        ret = List()
        current = self.head()
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
            current = self.head
            while current and current.next != self.tail:
                current = current.next
            ret = self.tail.data
            current.next = None
            self.tail = current
        
        self.size_count -= 1
        return ret
    
    def pop_start(self) -> object:
        if self.__len__() == 1: 
            ret = self.head.data
            self.head = self.tail = None
        else:
            ret = self.head.data
            self.head = self.head.next
        
        self.size_count -= 1
        return ret
    
    def pop(self, i: int = None) -> object:
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
            self.head = self.head.next
        elif current == self.tail:
            self.tail = previous
            previous.next = None
        else:
            current.next = current.next.next
        
        self.size_count -= 1
    
    def insert_head(self, data: object) -> None:
        if self.head == None:
            self.head = self.tail = Node(data)
        else:
            self.head = Node(data, self.head)
            
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
            current.next = Node(data, current.next)
            self.size_count += 1
        
    def get_list(self) -> list[object]:
        ret = []
        current = self.head
        while current: 
            ret.append(self.head.data)
            
        return ret
    
    def __str__(self) -> str:
        return str(self.get_list())
    
    def index(self, data, start=None, end=None):
        
        counter = 0
        if not start:
            start = 0
            
        current = self.head
        while current and counter <= start:
            counter += 1
            current = current.next
        
        if not current:
            return -1
        
        if not end: 
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

# Question 22. Implement a deque using linked lists.

class Node:
    def __init__(self, data: object = None, next: 'Node' = None):
        # 'Node' is called forward reference
        # tells Python to treat it as a string and resolve the type later.
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        """Linked list with two pointers"""
        self.head = None
        self.tail = None
        self.count = 0
        
    def is_empty(self) -> bool:
        return self.count == 0
    
    def size(self) -> int:
        return self.count
    
    def add_left(self, data: object) -> None:
        """Time complexity is O(1) since we have head pointer"""
        new_node = Node(object)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.count += 1
        
    def add_right(self, data: object) -> None:
        """Time complexity is O(1) since we have tail pointer"""
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1
            
    def remove_left(self) -> object:
        """Time complexity is O(1) since we have head pointer"""
        if self.is_empty():
            raise IndexError("Removal from an empty list")
        
        data = self.head.data
        
        if self.size() == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        
        self.count -= 1
        
        return data
    
    def remove_right(self) -> object:
        """Time complexity is O(n)"""
        if self.is_empty():
            raise IndexError("Removal from an empty list")
        
        data = self.tail.data
        
        if self.size() == 1:
            self.head = self.tail = None
        else:
            previous = None
            current = self.head
            # INCH WORMING
            while current != self.tail:
                previous = current
                current = current.next
            
            previous.next = None
            self.tail = previous
        self.count -= 1
        
        return data
            
class Deque:
    def __init__(self):
        self.items = LinkedList()
    
    def is_empty(self) -> bool:
        return self.items.is_empty()
    
    def size(self) -> int:
        return self.items.size()
    
    def add_right(self, item: object) -> None:
        self.items.add_right(item)
    
    def add_left(self, item: object) -> None:
        self.items.add_left(item)
    
    def remove_left(self) -> object:
        try:
            item = self.items.remove_left()
        except IndexError:
            raise IndexError("Cannot remove from empty Deque")
        return item
    
    def remove_right(self) -> object:
        try:
            item = self.items.remove_right()
        except IndexError:
            raise IndexError("Cannot remove from empty Deque")
        return item

# Testing Deque Implementation

print("Test 1: Add and Remove from Left and Right")
d = Deque()
d.add_left(10)
d.add_right(20)
d.add_left(5)
d.add_right(25)
print(d.remove_left())  # Expected: 5
print(d.remove_right())  # Expected: 25
print(d.remove_left())  # Expected: 10
print(d.remove_right())  # Expected: 20
print(d.is_empty())  # Expected: True (all items removed)
print()

print("Test 2: Add and Remove Multiple Times")
d = Deque()
d.add_left(1)
d.add_right(2)
d.add_left(0)
d.add_right(3)
print(d.remove_left())  # Expected: 0
print(d.remove_right())  # Expected: 3
print(d.remove_left())  # Expected: 1
print(d.remove_right())  # Expected: 2
print(d.is_empty())  # Expected: True
print()

print("Test 3: Size after operations")
d = Deque()
print(d.size())  # Expected: 0 (initially empty)
d.add_right(10)
d.add_left(20)
print(d.size())  # Expected: 2
d.remove_left()
print(d.size())  # Expected: 1
d.remove_right()
print(d.size())  # Expected: 0 (empty after all removals)
print()

print("Test 4: Remove from an empty Deque")
d = Deque()
try:
    d.remove_left()
except IndexError as e:
    print(e)  # Expected: "Cannot remove from empty Deque"
try:
    d.remove_right()
except IndexError as e:
    print(e)  # Expected: "Cannot remove from empty Deque"
print()

print("Test 5: Check is_empty")
d = Deque()
print(d.is_empty())  # Expected: True (initially empty)
d.add_right(100)
print(d.is_empty())  # Expected: False (after adding an item)
d.remove_right()
print(d.is_empty())  # Expected: True (empty after removal)
print()

print("Test 6: Mixed data types")
d = Deque()
d.add_right(42)       # Integer
d.add_left("hello")  # String
d.add_right([1, 2])   # List
print(d.remove_left())  # Expected: "hello"
print(d.remove_right())  # Expected: [1, 2]
print(d.remove_left())  # Expected: 42
print(d.is_empty())  # Expected: True
print()

print("Test 7: Large number of operations")
d = Deque()
for i in range(1000):
    d.add_right(i)
for i in range(500):
    d.remove_left()
print(d.size())  # Expected: 500
print(d.items.tail.data)
for i in range(500):
    d.remove_right()
print(d.size())  # Expected: 0
print(d.is_empty())  # Expected: True
print()

print("Test 8: Alternating left and right operations")
d = Deque()
d.add_left(1)
d.add_right(2)
d.add_left(0)
d.add_right(3)
print(d.remove_right())  # Expected: 3
print(d.remove_left())  # Expected: 0
print(d.remove_right())  # Expected: 2
print(d.remove_left())  # Expected: 1
print(d.is_empty())  # Expected: True
print()

print("Test 9: Edge cases with one item")
d = Deque()
d.add_left(10)
print(d.remove_left())  # Expected: 10
d.add_right(20)
print(d.remove_right())  # Expected: 20
print(d.is_empty())  # Expected: True

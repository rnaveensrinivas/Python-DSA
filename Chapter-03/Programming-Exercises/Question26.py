# Question 26. Create an implementation of a queue that would have an 
# average performance of O(1)  for enqueue and dequeue operations.

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
            
class Queue:
    def __init__(self):
        self.items = LinkedList()
    
    def is_empty(self) -> bool:
        return self.items.is_empty()
    
    def size(self) -> int:
        return self.items.size()
    
    def enqueue(self, item: object) -> None:
        self.items.add_right(item)
    
    def dequeue(self) -> object:
        try:
            item = self.items.remove_left()
        except IndexError:
            raise IndexError("Cannot remove from empty queue")
        return item

# Testing
# Test cases for Queue implementation

print("Test 1: Enqueue and Dequeue basic functionality")
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())  # Expected: 10
print(q.dequeue())  # Expected: 20
print(q.dequeue())  # Expected: 30
print()

print("Test 2: Enqueue after dequeue")
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Expected: 1
q.enqueue(3)
print(q.dequeue())  # Expected: 2
print(q.dequeue())  # Expected: 3
print()

print("Test 3: Check size after operations")
q = Queue()
print(q.size())  # Expected: 0 (initial size)
q.enqueue(5)
q.enqueue(6)
print(q.size())  # Expected: 2
q.dequeue()
print(q.size())  # Expected: 1
print()

print("Test 4: Dequeue from an empty queue")
q = Queue()
try:
    q.dequeue()
except IndexError as e:
    print(e)  # Expected: "Cannot remove from empty queue"
print()

print("Test 5: Check is_empty after operations")
q = Queue()
print(q.is_empty())  # Expected: True (initially empty)
q.enqueue(7)
print(q.is_empty())  # Expected: False
q.dequeue()
print(q.is_empty())  # Expected: True (empty after dequeuing)
print()

print("Test 6: Enqueue a mix of data types")
q = Queue()
q.enqueue(42)       # Integer
q.enqueue("hello")  # String
q.enqueue([1, 2])   # List
print(q.dequeue())  # Expected: 42
print(q.dequeue())  # Expected: "hello"
print(q.dequeue())  # Expected: [1, 2]
print()

print("Test 7: Dequeue all items and check behavior after")
q = Queue()
q.enqueue("A")
q.enqueue("B")
print(q.dequeue())  # Expected: "A"
print(q.dequeue())  # Expected: "B"
print(q.is_empty())  # Expected: True
try:
    q.dequeue()
except IndexError as e:
    print(e)  # Expected: "Cannot remove from empty queue"
print()

print("Test 8: Large number of operations")
q = Queue()
for i in range(1000):
    q.enqueue(i)
for i in range(500):
    q.dequeue() 
print(q.size())        # Expected: 500

        
        
        
        
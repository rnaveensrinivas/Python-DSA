# Question 20. Implement a stack using linked lists.
class Node:
    def __init__(self, data: object = None, next: "Node" = None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
        
    def is_empty(self) -> bool:
        return self.count == 0
    
    def size(self) -> int:
        return self.count
    
    def add_left(self, data: object) -> None:
        new_node = Node(data, self.head)
        self.head = new_node
        self.count += 1
        
    def remove_left(self) -> object:
        if self.is_empty():
            raise IndexError("Cannot remove from an empty list")
        
        data = self.head.data
        self.head = self.head.next
        self.count -= 1
        return data
    
    def peek_left(self) -> object:
        if self.is_empty():
            raise IndexError("Cannot peak from an empty list")
        
        data = self.head.data
        return data    
    
class Stack:
    def __init__(self):
        self.items = LinkedList()
    
    def is_empty(self) -> bool:
        return self.items.is_empty()
    
    def size(self) -> int:
        return self.items.size()
    
    def push(self, item: object) -> None:
        self.items.add_left(item)
        
    def pop(self) -> object:
        try: 
            item = self.items.remove_left()
        except:
            raise IndexError("Cannot pop from an empty stack")
        
        return item
    
    def peek(self) -> object:
        try: 
            item = self.items.peek_left()
        except:
            raise IndexError("Cannot peak from an empty stack")
        
        return item

print("Test Case 1: Basic Push and Pop")
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())  # Expected: 30
print(stack.pop())  # Expected: 20
print(stack.pop())  # Expected: 10
print()

print("Test Case 2: Pop from Empty Stack")
stack = Stack()
try:
    stack.pop()
except IndexError as e:
    print(e)  # Expected: "Cannot pop from an empty stack"
print()

print("Case 3: Peek on Non-Empty Stack")
stack = Stack()
stack.push(5)
stack.push(15)
print(stack.peek())  # Expected: 15
stack.pop()
print(stack.peek())  # Expected: 5
print()

print("Test Case 4: Peek on Empty Stack")
stack = Stack()
try:
    stack.peek()
except IndexError as e:
    print(e)  # Expected: "Cannot peak from an empty stack"
print()

print("Test Case 5: Interleaved Push, Pop, and Peek:")
stack = Stack()
stack.push(1)
print(stack.peek())  # Expected: 1
stack.push(2)
print(stack.pop())   # Expected: 2
stack.push(3)
print(stack.pop())   # Expected: 3
print(stack.pop())   # Expected: 1
print()

print("Test Case 6: Check Size of the Stack")
stack = Stack()
print(stack.size())  # Expected: 0 (initial size)
stack.push(42)
stack.push(43)
print(stack.size())  # Expected: 2
stack.pop()
print(stack.size())  # Expected: 1
print()

print("Test Case 7: Push and Pop with Multiple Data Types")
stack = Stack()
stack.push(10)         # Integer
stack.push("hello")    # String
stack.push([1, 2, 3])  # List
print(stack.pop())     # Expected: [1, 2, 3]
print(stack.pop())     # Expected: "hello"
print(stack.pop())     # Expected: 10
print()

print("Test Case 8: Push Many Items and Verify")
stack = Stack()
for i in range(1, 11):  # Push 1 to 10
    stack.push(i)
for i in range(10, 0, -1):  # Pop 10 to 1
    print(stack.pop())  # Expected: 10, 9, 8, ..., 1
print()

print("Test Case 9: Check is_empty")
stack = Stack()
print(stack.is_empty())  # Expected: True
stack.push(99)
print(stack.is_empty())  # Expected: False
stack.pop()
print(stack.is_empty())  # Expected: True
print()

print("Test Case 10: Handling Large Number of Items")
stack = Stack()
for i in range(1000):
    stack.push(i)
for i in range(999, -1, -1):
    stack.pop() # Expected: 999, 998, ..., 0
print(stack.size())
print()
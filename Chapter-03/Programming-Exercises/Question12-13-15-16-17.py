# To implement the length method, we counted the number of nodes in the list. 
# An alter native strategy would be to store the number of nodes in the list 
# as an additional piece of  data in the head of the list. Modify the 
# UnorderedList class to include this information  and rewrite the length 
# method.

# 0 based index
class Node: 
    def __init__(self, data: object = None, next: 'Node' = None):
        self.data = data
        self.next = next

class UnorderedList:
    def __init__(self): 
        self.head = None
        self.tail = None
        self.count = 0
    
    def size(self) -> int:
        return self.count
    
    def is_empty(self) -> bool:
        return self.size() == 0
    
    def add(self, data: object) -> None:
        if not self.head:
            self.head = self.tail = Node(data)
        else:
            self.head = Node(data, self.head)
            
        self.count += 1
    
    def remove(self, data: object) -> None:
        if self.is_empty(): 
            raise IndexError("Trying to remove from empty list.")
        
        # inch worming
        current = self.head
        previous = None
        while current and current.data != data:
            previous = current
            current = current.next
        
        if not current:
            # Question 13.  Implement the remove method so that it works 
            # correctly in the case where the item is not  in the list.
            raise IndexError("Item doens't exist in list.")
        elif previous == None:
            # removing head
            if self.size() == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.next
        elif not current.next:
            # removing tail
            self.tail = previous
            previous.next = None
        else:
            # somewhere in the middle
            previous.next = current.next
            
        self.count -= 1
        
    
    def index(self, data: object) -> int:

        index = 0
        current = self.head
        while current and current.data != data:
            index += 1
            current = current.next
        
        return index if current else -1
    
    def search(self, data: object) -> bool:
        return False if self.index(data) == -1 else True
        
    def append(self, data: object) -> None:
        
        if self.is_empty():
            self.head = self.tail = Node(data)
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
            
        self.count += 1
    
    def pop_end(self) -> object:
        if self.is_empty():
            raise IndexError("Cannot pop from empty list.")
        
        if self.size() == 1:
            ret = self.head.data
            self.head = self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            ret = current.next.data
            current.next = None
            self.tail = current
            
        self.count -= 1
        return ret
    
    def pop(self, pos: int = None) -> object:
        
        if pos == None or pos == self.size() - 1:
            return self.pop_end()
        
        if pos >= self.size() or pos < 0:
            raise IndexError(f"Given pos={pos} is invalid")
        
        
        if pos == 0:
            ret = self.head.data
            if self.size() == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.next
        else:
            current = self.head
            while pos >= 1:
                current = current.next
            
            ret = current.next.data
            current.next = current.next.next
            
        self.count -= 1
        return ret
        
    def insert(self, pos: int, data: object) -> None:
        
        if pos >= self.size() or pos < 0:
            raise IndexError(f"Given pos={pos} is invalid")
        
        if pos == self.size() - 1:
            self.append(data)
        elif pos == 0:
            self.add(data)
        else:
            current = self.head
            while pos >= 1:
                current = current.next
            
            current.next = Node(data, current.next)
            self.count += 1
        
    def get_list(self) -> list[object]:
        current = self.head
        ret = []
        while current: 
            ret.append(current.data)
            current = current.next
        return ret
        
    def __str__(self) -> str:
        # Question 15. Implement the __str__ method in the OrderedList class. 
        # What would be a good string representation for a list?
        # Question 16. Implement __str__ method so that lists are displayed 
        # the Python way (with square brackets)
        return str(self.get_list())
        
    
    def __getitem__(self, val):
        l = self.get_list()
        return l[val]

# Testing:
print("1----")
# 1. **Empty List Operations**

# Remove from Empty List:
try:
    ul = UnorderedList()
    ul.remove(10)  # Should raise IndexError
except Exception as e:
    print(e)
    

# Pop from Empty List:
try:
    ul = UnorderedList()
    ul.pop()  # Should raise IndexError
except Exception as e:
    print(e)

# Pop by Position from Empty List:
try: 
    ul = UnorderedList()
    ul.pop(0)  # Should raise IndexError
except Exception as e:
    print(e)
    
# Index of Non-Existent Element:
ul = UnorderedList()
print(ul.index(10))  # Should return -1

# Search for Non-Existent Element:
ul = UnorderedList()
print(ul.search(10))  # Should return False

print()

print("2----")
# 2. **Single Element List**

# Remove the Only Element:
ul = UnorderedList()
ul.add(10)
ul.remove(10)  # Should leave the list empty
print(ul.size()) # should be 0

# Pop the Only Element:
ul = UnorderedList()
ul.add(10)
ul.pop()  # Should return 10 and leave the list empty
print(ul.size()) # should be 0

# Add and Then Pop by Position (0):

ul = UnorderedList()
ul.add(10)
ul.pop(0)  # Should return 10 and leave the list empty
print(ul.size()) # should be 0

# Insert at Position 0 in a Single Element List:

ul = UnorderedList()
ul.add(10)
ul.insert(0, 20)  # Should make the list [20, 10]
print(ul.size()) # should be 2
print()

print("3----")
# 3. **Two Element List**

# Remove Head (First Element):
ul = UnorderedList()
ul.add(10)
ul.add(20)  # List is now [20, 10]
ul.remove(20)
print(ul)# Should remove 20, leaving [10]
print(ul.size()) # should be 1

# Remove Tail (Last Element):
ul = UnorderedList()
ul.add(10)
ul.add(20)  # List is now [20, 10]
ul.remove(10)
print(ul) # Should remove 10, leaving [20]
print(ul.size()) # should be 1

# Pop Last Element in a Two-Element List:
ul = UnorderedList()
ul.add(10)
ul.add(20)  # List is now [20, 10]
print(ul.pop())  # Should return 10 and leave [20]
print(ul.size())

# Insert at Position 1 in a Two-Element List:
ul = UnorderedList()
ul.add(10)
ul.add(20)  # List is now [20, 10]
ul.insert(1, 30)  # Should make the list [20, 30, 10]
print(ul)
print(ul.size()) # 3
print()

print("4----")
# 4. **Out-of-Range Operations**
# Insert at an Invalid Position (Negative Index):
try:
    ul = UnorderedList()
    ul.insert(-1, 10)  # Should raise IndexError
except Exception as e:
    print(e)

# Insert at an Invalid Position (Greater than Size):
try: 
    ul = UnorderedList()
    ul.insert(1, 10)  # Should raise IndexError if size is less than 2
except Exception as e:
    print(e)
    
# Pop with Invalid Position:
try:
    ul = UnorderedList()
    ul.pop(2)  # Should raise IndexError if size is less than 3
except Exception as e:
    print(e)
print()

print("5----")
# 5. **List with Duplicates**

# Remove First Occurrence of Duplicate:
ul = UnorderedList()
ul.add(10)
ul.add(20)
ul.add(10)  # List is now [10, 20, 10]
ul.remove(10)  # Should remove the first 10, leaving [20, 10]
print(ul) 

# Index of Duplicate Element:
ul = UnorderedList()
ul.add(10)
ul.add(20)
ul.add(10)  # List is now [10, 20, 10]
print(ul)
print(ul.index(10))  # Should return 0 (index of the first 10)

# Remove First Occurrence of Duplicate:
ul = UnorderedList()
ul.add(10)
ul.add(20)
ul.add(10)  # List is now [10, 20, 10]
try:
    ul.remove(100)  # raise index error
except Exception as e:
    print(e)

print(ul) 

# # Search for Duplicate Element:
ul = UnorderedList()
ul.add(10)
ul.add(20)
ul.add(10)  # List is now [10, 20, 10]
print(ul)
print(ul.search(10))  # Should return True
print()

print("6----")
# 6. **Appending and Adding Multiple Elements**
# # Append Multiple Elements and Verify Order:
ul = UnorderedList()
ul.append(10)
ul.append(20)
ul.append(30)  # List should now be [10, 20, 30]
print(ul)

# # Remove from Middle in Multiple Elements List:
ul = UnorderedList()
ul.add(10)
ul.add(20)
ul.add(30)  # List is now [30, 20, 10]
ul.remove(20)  # Should remove 20, leaving [30, 10]
print(ul)
print()

# 7. **Multiple `pop()` Operations**
print("7----")
ul = UnorderedList()
ul.add(10)
ul.add(20)
ul.add(30)  # List is now [30, 20, 10]
ul.pop()  # Should return 10 and leave [30, 20]
ul.pop()  # Should return 20 and leave [30]
ul.pop()  # Should return 30 and leave the list empty
print(ul)

# 8. slicing
print("8----")
ul = UnorderedList()
import random
for i in range(10, -1, -1):
    ul.add(i)
print(ul)
print(f"ul[3]: {ul[3]}")
print(f"ul[3:6]: {ul[3:6]}")
print(f"ul[-1]: {ul[-1]}")
print(f"ul[::-1]: {ul[::-1]}")
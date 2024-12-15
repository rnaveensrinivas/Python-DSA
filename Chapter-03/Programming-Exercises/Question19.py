#  Implement the remaining operations defined in the OrderedList ADT

# 0 based index
class Node: 
    def __init__(self, data: object = None, next: 'Node' = None):
        self.data = data
        self.next = next

class OrderedList:
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
            current = self.head
            previous = None
            while current and current.data <= data:
                previous = current
                current = current.next
            
            if not previous: 
                # inserting at head
                self.head = Node(data, self.head)
                
            elif not current:
                # inserting at tail
                self.tail.next = Node(data)
                self.tail = self.tail.next
            else:
                previous.next = Node(data, current)
            
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
    ol = OrderedList()
    ol.remove(10)  # Should raise IndexError
except Exception as e:
    print(e)
    

# Pop from Empty List:
try:
    ol = OrderedList()
    ol.pop()  # Should raise IndexError
except Exception as e:
    print(e)

# Pop by Position from Empty List:
try: 
    ol = OrderedList()
    ol.pop(0)  # Should raise IndexError
except Exception as e:
    print(e)
    
# Index of Non-Existent Element:
ol = OrderedList()
print(ol.index(10))  # Should return -1

# Search for Non-Existent Element:
ol = OrderedList()
print(ol.search(10))  # Should return False

print()

print("2----")
# 2. **Single Element List**

# Remove the Only Element:
ol = OrderedList()
ol.add(10)
ol.remove(10)  # Should leave the list empty
print(ol.size()) # should be 0

# Pop the Only Element:
ol = OrderedList()
ol.add(10)
ol.pop()  # Should return 10 and leave the list empty
print(ol.size()) # should be 0

# Add and Then Pop by Position (0):

ol = OrderedList()
ol.add(10)
ol.pop(0)  # Should return 10 and leave the list empty
print(ol.size()) # should be 0

# Insert at Position 0 in a Single Element List:

ol = OrderedList()
ol.add(10)
ol.add(20)  # Should make the list [20, 10]
print(ol.size()) # should be 2
print()

print("3----")
# 3. **Two Element List**

# Remove Head (First Element):
ol = OrderedList()
ol.add(10)
ol.add(20)  # List is now [20, 10]
ol.remove(20)
print(ol)# Should remove 20, leaving [10]
print(ol.size()) # should be 1

# Remove Tail (Last Element):
ol = OrderedList()
ol.add(10)
ol.add(20)  # List is now [20, 10]
ol.remove(10)
print(ol) # Should remove 10, leaving [20]
print(ol.size()) # should be 1

# Pop Last Element in a Two-Element List:
ol = OrderedList()
ol.add(10)
ol.add(20)  # List is now [20, 10]
print(ol.pop())  # Should return 10 and leave [20]
print(ol.size())

# Insert at Position 1 in a Two-Element List:
ol = OrderedList()
ol.add(10)
ol.add(20)  # List is now [20, 10]
ol.add(30)  # Should make the list [20, 30, 10]
print(ol)
print(ol.size()) # 3
print()

print("4----")
# 4. **Out-of-Range Operations**
# Insert at an Invalid Position (Negative Index):
try:
    ol = OrderedList()
    ol.add(10)  # Should raise IndexError
except Exception as e:
    print(e)

# Insert at an Invalid Position (Greater than Size):
try: 
    ol = OrderedList()
    ol.add(10)  # Should raise IndexError if size is less than 2
except Exception as e:
    print(e)
    
# Pop with Invalid Position:
try:
    ol = OrderedList()
    ol.pop(2)  # Should raise IndexError if size is less than 3
except Exception as e:
    print(e)
print()

print("5----")
# 5. **List with Duplicates**

# Remove First Occurrence of Duplicate:
ol = OrderedList()
ol.add(10)
ol.add(20)
ol.add(10)  # List is now [10, 20, 10]
ol.remove(10)  # Should remove the first 10, leaving [20, 10]
print(ol) 

# Index of Duplicate Element:
ol = OrderedList()
ol.add(10)
ol.add(20)
ol.add(10)  # List is now [10, 20, 10]
print(ol)
print(ol.index(10))  # Should return 0 (index of the first 10)

# Remove First Occurrence of Duplicate:
ol = OrderedList()
ol.add(10)
ol.add(20)
ol.add(10)  # List is now [10, 20, 10]
try:
    ol.remove(100)  # raise index error
except Exception as e:
    print(e)

print(ol) 

# # Search for Duplicate Element:
ol = OrderedList()
ol.add(10)
ol.add(20)
ol.add(10)  # List is now [10, 20, 10]
print(ol)
print(ol.search(10))  # Should return True
print()

print("6----")
# 6. **Appending and Adding Multiple Elements**
# # Append Multiple Elements and Verify Order:
ol = OrderedList()
ol.add(10)
ol.add(20)
ol.add(30)  # List should now be [10, 20, 30]
print(ol)

# # Remove from Middle in Multiple Elements List:
ol = OrderedList()
ol.add(10)
ol.add(20)
ol.add(30)  # List is now [30, 20, 10]
ol.remove(20)  # Should remove 20, leaving [30, 10]
print(ol)
print()

# 7. **Multiple `pop()` Operations**
print("7----")
ol = OrderedList()
ol.add(10)
ol.add(20)
ol.add(30)  # List is now [30, 20, 10]
ol.pop()  # Should return 10 and leave [30, 20]
ol.pop()  # Should return 20 and leave [30]
ol.pop()  # Should return 30 and leave the list empty
print(ol)

# 8. Check
print("8----")
ol = OrderedList()
import random
for i in range(10, -1, -1):
    ol.add(i)
print(ol)
ol.pop()
ol.remove(0)
print(ol)
ol.remove(5)
print(ol)

# 9. slicing
print("9----")
ol = OrderedList()
import random
for i in range(10, -1, -1):
    ol.add(i)
print(ol)
print(f"ol[3]: {ol[3]}")
print(f"ol[3:6]: {ol[3:6]}")
print(f"ol[-1]: {ol[-1]}")
print(f"ol[::-1]: {ol[::-1]}")


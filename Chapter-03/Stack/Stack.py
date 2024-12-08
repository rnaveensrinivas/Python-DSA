class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item: object) -> None:
        self.items.append(item)
        
    def pop(self) -> object:
        return self.items.pop()

    def peek(self) -> object:
        return self.items[-1]
    
    def size(self) -> int:
        return len(self.items)
    
    def is_empty(self) -> bool:
        return len(self.items) == 0
class Deque:
    def __init__(self):
        self.items = []
        
    def add_front(self, item: object) -> None:
        self.items.insert(0, item)
    
    def add_rear(self, item: object) -> None:
        self.items.append(item)
        
    def remove_front(self) -> object:
        return self.items.pop(0)
    
    def remove_rear(self) -> object:
        return self.items.pop()
    
    def size(self) -> int:
        return len(self.items)
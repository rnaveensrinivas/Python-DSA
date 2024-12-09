class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, item: object) -> None:
        self.items.insert(0, item)
    
    def dequeue(self) -> object:
        return self.items.pop()
    
    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)
    
# q = Queue()
# q.enqueue("hello")
# q.enqueue("dog")
# q.enqueue(3)
# print(q.dequeue())
        
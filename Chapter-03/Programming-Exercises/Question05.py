# Implement the Queue ADT, using a list such that the rear of the queue is 
# at the end of the list.
class Queue:
    def __init__(self):
        self.items = []
        
    def size(self) -> int:
        return len(self.items)
    
    def is_empty(self) -> bool:
        return self.size() == 0
    
    def enqueue(self, item: object) -> None:
        self.items.append(item)
        
    def dequeue(self) -> object:
        return self.items.pop(0)

q = Queue()
q.enqueue("hello")
q.enqueue("dog")
q.enqueue(3)
print(q.dequeue())
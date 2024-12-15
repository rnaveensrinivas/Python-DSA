# Modify the Hot Potato simulation to allow for a randomly chosen counting 
# value so that each pass is not predictable from the previous one.
import random

class Queue:
    def __init__(self, l: list[object] = None):
        self.items = []
        if l: 
            self.items.extend(l)
    
    def size(self) -> int:
        return len(self.items)
    
    def is_empty(self) -> bool:
        return self.size() == 0
    
    def enqueue(self, item: object) -> None:
        self.items.append(item)
        
    def dequeue(self) -> object:
        return self.items.pop(0)
    
    def __str__(self):
        return f"front -> {self.items} <- rear"
    
def hot_potato(people: list[str]):
    
    queue = Queue(people)
    while queue.size() != 1:
        counter = random.randint(1, 3*len(people))
        while counter > 0:
            queue.enqueue(queue.dequeue())
            counter -= 1
        queue.dequeue()
    return queue.dequeue()

last_person = hot_potato(["Bill", "David", "Susan", 
                          "Jane", "Kent", "Brad"])  

print(f"Last person is {last_person}")  
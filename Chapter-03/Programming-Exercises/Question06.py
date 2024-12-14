# Design and implement an experiment to do benchmark comparisons of the 
# two queue  implementations. What can you learn from such an experiment?
class QueueRearBack:
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

class QueueRearFront:
    def __init__(self): 
        self.items = []
        
    def size(self) -> int:
        return len(self.items)
    
    def is_empty(self) -> bool:
        return self.size() == 0
    
    def enqueue(self, item: object) -> None:
        self.items.insert(0, item)
        
    def dequeue(self) -> object:
        return self.items.pop()
    
import timeit
NUMBER_OF_EXEC = 1_000

qrb = QueueRearBack()
qrf = QueueRearFront()

tqrb = timeit.Timer("qrb.enqueue(None)", 
                    "from __main__ import qrb")
tqrf = timeit.Timer("qrf.enqueue(None)", 
                    "from __main__ import qrf")

print("Enqueque Time in Seconds.")
print("Size\tRear Back\tRear Front")
for i in range(100_000, 1_000_001, 100_000):
    qrb.items = [0] * i
    qrf.items = [0] * i
    
    time_qrb = tqrb.timeit(NUMBER_OF_EXEC)
    time_qrf = tqrf.timeit(NUMBER_OF_EXEC)
    print("%d\t%2.10f\t%2.10f"%(i, time_qrb, time_qrf))
    
    
tqrb = timeit.Timer("qrb.dequeue()", 
                    "from __main__ import qrb")
tqrf = timeit.Timer("qrf.dequeue()", 
                    "from __main__ import qrf")

print("\nDequeue Time in Seconds.")
print("Size\tRear Back\tRear Front")
for i in range(100_000, 1_000_001, 100_000):
    qrb.items = [0] * i
    qrf.items = [0] * i
    
    time_qrb = tqrb.timeit(NUMBER_OF_EXEC)
    time_qrf = tqrf.timeit(NUMBER_OF_EXEC)
    print("%d\t%2.10f\t%2.10f"%(i, time_qrb, time_qrf))
    
_ = """
Enqueque Time in Seconds.
Size    Rear Back       Rear Front
100000  0.0002399710    0.0613385480
200000  0.0001220200    0.1051775350
300000  0.0001034900    0.2241239590
400000  0.0001044800    0.3339014780
500000  0.0001072000    0.4081496280
600000  0.0001114990    0.6767942680
700000  0.0001077140    0.8120393040
800000  0.0001559640    0.9017951410
900000  0.0001029860    1.0318642910
1000000 0.0001026640    1.1444017160

Dequeue Time in Seconds.
Size    Rear Back       Rear Front
100000  0.0361640080    0.0000945590
200000  0.0711022330    0.0001237540
300000  0.1164940620    0.0000881150
400000  0.1510734310    0.0000878350
500000  0.2497553580    0.0000881450
600000  0.3873152330    0.0000883810
700000  0.6035419390    0.0000885510
800000  0.7343273360    0.0000885850
900000  0.8687094310    0.0001724570
1000000 0.9924300310    0.0000901100
"""

    
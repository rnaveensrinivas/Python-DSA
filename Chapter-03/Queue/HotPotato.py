from Queue import Queue

def hot_potato(name_list: list[str], num: int) -> str:
    q = Queue()
    for name in name_list:
        q.enqueue(name)
    print(q.size())
    i = 0
    while q.size() != 1:
        for _ in range(num):
            q.enqueue(q.dequeue())
        q.dequeue() # eliminating
    
    return q.dequeue()

print(hot_potato(["Bill", "David", "Susan", 
                  "Jane", "Kent", "Brad"], 7))
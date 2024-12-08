from timeit import Timer
import random

NUMBER_OF_EXEC=1_000
print("Size\tList (secs)\tDictionary (secs)")
for i in range(10_000, 100_001, 10_000):
    t = Timer(f"random.randrange({i}) in x", "from __main__ import random, x")
    x = [1] * i
    lst_time = t.timeit(number=NUMBER_OF_EXEC)

    x = {j: None for j in range(i)}
    d_time = t.timeit(number=NUMBER_OF_EXEC)

    print("%d\t%2.10f\t%2.10f"%(i, lst_time, d_time))
    
_ = """
Size    List (secs)     Dictionary (secs)
10000   0.1650856390    0.0008572660
20000   0.3562527280    0.0009177710
30000   0.5096667150    0.0009484560
40000   0.6450595310    0.0009731560
50000   0.7962693220    0.0013460860
60000   0.9794412810    0.0009915300
70000   1.1070882910    0.0012538130
80000   1.3241610860    0.0012795720
90000   1.4871159330    0.0012611560
100000  1.6007421800    0.0011424550
"""
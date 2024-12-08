# Devise an experiment to verify that get item and set item are O(1) 
# for dictionaries.
from timeit import Timer
import random

NUMBER_OF_EXEC=1_000
print("Size\t\tGet (Secs)\tSet (Secs)")
for i in range(1_000_000, 10_000_001, 1_000_000):
    a_dict = {j: None for j in range(i)}
    
    t_get = Timer("a_dict[random.randrange(%d)]"%i, 
                  "from __main__ import random, a_dict")
    t_set = Timer("a_dict[random.randrange(%d)] = -1"%i, 
                  "from __main__ import random, a_dict")
    
    print("%d\t\t%2.10f\t%2.10f"%(i,
                                t_get.timeit(number=NUMBER_OF_EXEC), 
                                t_set.timeit(number=NUMBER_OF_EXEC)))

output = """
Size            Get (Secs)      Set (Secs)
1000000         0.0019440370    0.0017559590
2000000         0.0021702500    0.0021020970
3000000         0.0021878500    0.0018188530
4000000         0.0016204320    0.0014772490
5000000         0.0016972440    0.0015448730
6000000         0.0017174620    0.0015337510
7000000         0.0027063000    0.0016491610
8000000         0.0016761800    0.0015647790
9000000         0.0018029620    0.0017256300
10000000        0.0018329270    0.0016770090
"""
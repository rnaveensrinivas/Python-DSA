# Devise an experiment to verify that get item and set item are O(1) for dictionaries.
from timeit import Timer
import random

print("Size\t\tTime [Get]\tTime [Set]")
for i in range(10_000_000, 100_000_001, 10_000_000):
    a_dict = {j: None for j in range(i)}
    
    t_get = Timer("a_dict[random.randrange(%d)]"%i, 
                  "from __main__ import random, a_dict")
    t_set = Timer("a_dict[random.randrange(%d)] = 8"%i, 
                  "from __main__ import random, a_dict")
    
    print("%d\t%0.8f\t%0.8f"%(i,
                              t_get.timeit(number=1000), 
                              t_set.timeit(number=1000)))

output = """
Size            Time [Get]      Time [Set]
10000000        0.00096930      0.00095580
20000000        0.00137230      0.00117900
30000000        0.00128200      0.00116860
40000000        0.00140270      0.00137060
50000000        0.00791560      0.00600140
60000000        0.00779850      0.00602800
70000000        0.01679080      0.01593040
80000000        0.02147660      0.01877770
90000000        0.12573570      0.10824190
100000000       0.17229280      0.11840070

This is not bad, since we are dealing with dictionary of size 100M.
"""
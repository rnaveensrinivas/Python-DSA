# Devise an experiment that compares the performance of the del operator on lists and  dictionaries.
from timeit import Timer
import random

print("Size\t\tDictionary\tList")
for i in range(1_000_000, 10_000_001, 1_000_000):
    a_dict = {j: None for j in range(i)}
    a_list = list(range(i))
    
    # for sake of indentation
    t_dict = Timer("""
i = random.randrange(%d)
if i in a_dict: 
    del a_dict[i]"""%i,
                   "from __main__ import random, a_dict")
    
    t_list = Timer("""
i = random.randrange(%d)
if i < len(a_list):
    del a_list[i]"""%i, 
                   "from __main__ import random, a_list"
                   )
    
    print("%d\t\t%0.8f\t%0.8f"%(i,
                              t_dict.timeit(number=1000), 
                              t_list.timeit(number=1000)))

output = """
Size            Dictionary      List
1000000         0.00089620      0.33642450
2000000         0.00099050      0.66674300
3000000         0.00109180      1.06692520
4000000         0.00111400      1.41516550
5000000         0.00127840      1.70489550
6000000         0.00120830      2.10117020
7000000         0.00117420      2.41082670
8000000         0.00116030      2.69877070
9000000         0.00121180      3.15980360
10000000        0.00133050      3.77158430
"""
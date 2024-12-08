# Devise an experiment that compares the performance of the del operator on 
# lists and  dictionaries.
from timeit import Timer
import random

NUMBER_OF_EXEC=1_000
print("Size\t\tList (Secs)\tDictionary (Secs)")
for i in range(1_000_000, 10_000_001, 1_000_000):
    a_dict = {j: None for j in range(i)}
    a_list = [1] * i
    
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
    
    print("%d\t\t%2.10f\t%2.10f"%(i,
                              t_list.timeit(number=NUMBER_OF_EXEC), 
                              t_dict.timeit(number=NUMBER_OF_EXEC)))

output = """
Size            List (Secs)     Dictionary (Secs)
1000000         0.4504866390    0.0015981050
2000000         1.0059817320    0.0023635040
3000000         1.6665535320    0.0023362540
4000000         2.1174818860    0.0028721050
5000000         2.8092048620    0.0021187240
6000000         3.6960583760    0.0021808650
7000000         3.7442723290    0.0022156240
8000000         4.3271200970    0.0021564220
9000000         4.9006598880    0.0025574550
10000000        5.9322355820    0.0023417500
"""
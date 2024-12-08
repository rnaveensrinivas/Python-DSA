# Devise an experiment to verify that the list index operator is O(1).
from timeit import Timer
import random
NUMBER_OF_EXEC=1_000

print("Size\t\tTime (Secs)")
for i in range(1_000_000, 10_000_001, 1_000_000):
    a_list = [1] * i
    t1 = Timer("a_list[random.randrange(%d)]"%i, 
               "from __main__ import random, a_list")
    print(f"%d\t\t%2.10f"%(i, t1.timeit(number=NUMBER_OF_EXEC)))

output = """
Size            Time (Secs)
1000000         0.0010589920
2000000         0.0010426140
3000000         0.0010325370
4000000         0.0015727720
5000000         0.0011209170
6000000         0.0011126440
7000000         0.0012687110
8000000         0.0013130280
9000000         0.0013872810
10000000        0.0012588040
"""
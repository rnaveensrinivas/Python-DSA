# Devise an experiment to verify that the list index operator is O(1).
from timeit import Timer
import random

print("Size\t\tTime")
for i in range(10_000_000, 100_000_001, 10_000_000):
    a_list = list(range(i))
    t1 = Timer("a_list[random.randrange(%d)]"%i, "from __main__ import random, a_list")
    print(f"{i}\t{t1.timeit(number=1000)}")

output = """
Size            Time
10000000        0.0007727000047452748
20000000        0.0008559999987483025
30000000        0.000762699986808002
40000000        0.0008993999799713492
50000000        0.0011965999729000032
60000000        0.0010864000068977475
70000000        0.000944900035392493
80000000        0.0020558999967761338
90000000        0.004302299988921732
100000000       0.02330389997223392
"""
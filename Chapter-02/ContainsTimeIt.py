from timeit import Timer

for i in range(10_000, 1_000_001, 20_000):
    t = Timer(f"random.randrange({i}) in x", "from __main__ import random, x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)

    x = {j: None for j in range(i)}
    d_time = t.timeit(number=1000)

    print("%d, %10.3f, %10.3f"%(i, lst_time, d_time))
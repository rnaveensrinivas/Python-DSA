from timeit import Timer

NUMBER_OF_EXEC=1_000
pop_zero = Timer("x.pop(0)", "from __main__ import x")
pop_end = Timer("x.pop()", "from __main__ import x")

print("Size\t\tpop(0) (secs)\tpop() (secs)")
for i in range(1_000_000, 10_000_001, 1_000_000):
    x = [1] * i
    pz = pop_zero.timeit(number=NUMBER_OF_EXEC)
    x = [1] * i 
    pe = pop_end.timeit(number=NUMBER_OF_EXEC)
    
    print("%d\t\t%2.10f\t%2.10f"%(i,pz, pe))

_ = """
Size            pop(0) (secs)   pop() (secs)
1000000         1.8404606120    0.0000460580
2000000         2.3603357670    0.0000440230
3000000         3.2072512060    0.0000432170
4000000         4.2885564860    0.0000434520
5000000         5.3589443200    0.0000448660
6000000         6.4324326840    0.0000525360
7000000         7.5005521330    0.0000435500
8000000         8.5349381580    0.0000442250
9000000         9.5938281240    0.0000437510
10000000        10.7083845250   0.0000435840
"""
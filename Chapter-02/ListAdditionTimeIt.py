from timeit import Timer
NUMBER_OF_EXEC = 1000

# accounting for the overhead of method invocation
t0 = Timer("overhead()", "from ListAddition import overhead")
overhead_time = t0.timeit(number=NUMBER_OF_EXEC)

t1 = Timer("test1()", "from ListAddition import test1")
print("concat", t1.timeit(number=NUMBER_OF_EXEC) - overhead_time, "seconds", flush=True)

t2 = Timer("test2()", "from ListAddition import test2")
print("append", t2.timeit(number=NUMBER_OF_EXEC) - overhead_time, "seconds", flush=True)

t3 = Timer("test3()", "from ListAddition import test3")
print("comprehension", t3.timeit(number=NUMBER_OF_EXEC) - overhead_time, "sseconds", flush=True)

t4 = Timer("test4()", "from ListAddition import test4")
print("range", t4.timeit(number=NUMBER_OF_EXEC) - overhead_time, "seconds", flush=True)
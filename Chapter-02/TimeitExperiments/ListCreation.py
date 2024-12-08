from timeit import Timer
NUMBER_OF_EXEC = 10_000

_ = """
We are going to compare 5 ways of creating a list. 
1. Loop and Concatenation operator
2. Loop and Append method
3. List comprehension
4. list() and range() methods
5. Reptition operator
"""

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

def test5():
    l = [0] * 1000

def overhead():
    pass

print("Creation\t Time (Seconds)")

# accounting for the overhead of method invocation
t0 = Timer("overhead()", "from __main__ import overhead")
overhead_time = t0.timeit(number=NUMBER_OF_EXEC)

t1 = Timer("test1()", "from __main__ import test1")
print("concat\t\t", 
      "%2.10f"%(t1.timeit(number=NUMBER_OF_EXEC) - overhead_time), flush=True)

t2 = Timer("test2()", "from __main__ import test2")
print("append\t\t", 
      "%2.10f"%(t2.timeit(number=NUMBER_OF_EXEC) - overhead_time), flush=True)

t3 = Timer("test3()", "from __main__ import test3")
print("comprehension\t", 
      "%2.10f"%(t3.timeit(number=NUMBER_OF_EXEC) - overhead_time), flush=True)

t4 = Timer("test4()", "from __main__ import test4")
print("range\t\t", 
      "%2.10f"%(t4.timeit(number=NUMBER_OF_EXEC) - overhead_time), flush=True)

t5 = Timer("test5()", "from __main__ import test5")
print("repetition\t", 
      "%2.10f"%(t5.timeit(number=NUMBER_OF_EXEC) - overhead_time), flush=True)

# Output - for number=10_000 
# Creation         Time (Seconds)
# concat           22.2902233780
# append           0.5496055400
# comprehension    0.4100013100
# range            0.2474477550
# repetition       0.0195660530

# Hence, repetition is the fastest way to create a list. 

_ = """

print(__name__) # outputs "__main__"

"from __main__ import test1": This is the setup code that is run before 
measuring the execution time. 
The Timer object will import the test1 function from the __main__ module 
(i.e., the current script) before running the timed code. 
This ensures that the test1 function is available for execution.

from __main__ import test1 imports the function test1 from the __main__ 
namespace into the namespace that timeit sets up for the timing experiment. 
The timeit module does this because it wants to run the timing tests in an 
environment that is uncluttered by any stray variables you may have created, 
that may interfere with your function's performance in some unforeseen way.
"""
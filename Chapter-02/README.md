## Difference Between Algorithm and Programming Language

- **Algorithm**: A step-by-step procedure or formula for solving a problem or performing a task. It is independent of any programming language and focuses solely on the logic of the solution.
- **Programming Language**: A set of rules and syntax used to write code that implements an algorithm. Programming languages provide the necessary constructs to translate the logic of an algorithm into executable code.

## Accumulator Variable

- An **accumulator variable** is used to collect or accumulate results through repetitive operations.
- Typically, an accumulator is initialized to a neutral value (like 0 for sums) and then updated during each iteration of a loop or recursion.
- Example:
  ```python
  total = 0
  for i in range(1, 6):
      total += i  # Accumulating the sum of integers 1 to 5
  ```

## What Is Algorithmic Analysis?

- **Algorithmic analysis** involves evaluating and comparing algorithms to determine which one is more efficient in terms of computing resources like time and space.
- It helps in understanding the performance of an algorithm, which is crucial for making decisions about which algorithm to choose based on the problem at hand.
- The goal is to find algorithms that use resources optimally and scale well as input sizes increase.

## Computing Resources
 ### Time
- **Time** refers to the execution or running time of an algorithm.
- It measures how long an algorithm takes to complete its task, typically expressed as a function of input size (`n`).
- The **execution time** can vary depending on factors like hardware, operating system, and specific implementation.
- A way to measure execution time in Python:
  ```python
  import time
  start = time.time()  # Start time
  # operation
  end = time.time()    # End time
  elapsed_time = end - start  # Total time taken
  ```

#### Time Measurement Issues

- `time.time()` returns the current system clock time in seconds since the epoch (i.e., a point in time).
- The issue with using **benchmarking techniques** like this is that the time measurement can be influenced by several external factors:
  - The specific machine used for execution.
  - The time of day (due to varying system load).
  - The compiler and programming language optimizations.
  - The number of processes running on the machine.
- This makes time measurement unreliable for comparing algorithms in a consistent manner.

### Space

- **Space** refers to the amount of memory required by an algorithm to execute.
- It includes both the space for the input data and any additional memory used by the algorithm during execution (like variables, data structures, etc.).
- Space complexity helps in understanding how well an algorithm scales with larger inputs in terms of memory usage.

## Purely Algorithmic Characterization

- To truly compare algorithms, we need a characterization that is independent of specific programs or computers used, focusing purely on the algorithm's inherent efficiency.
- This is done through **Big-O notation**, which expresses an algorithm's time and space complexity in terms of the input size, abstracting away machine-specific details.


## Big-O Notation

Big-O notation is used to analyze and quantify the efficiency of algorithms by focusing on the number of operations required as the problem size increases.

### Basic Unit of Computation
- A basic unit of computation represents a fundamental operation (e.g., an assignment statement).
- For example, in the `sum_of_n` function, the number of operations is `1 + n`, where `n` is the problem size.

### Analyzing Execution Time
- The goal is to examine how the execution time changes as the problem size increases.
- **Dominant Term**: As the problem size (`n`) grows, the dominant term in the function `T(n)` becomes more significant.
- Big-O notation captures the dominant term and ignores less significant terms.

### Big-O Notation
- Big-O notation is written as `O(f(n))`, where `f(n)` represents the dominant term of `T(n)`.
- Example: For `T(n) = 1 + n`, as `n` grows large, the constant `1` becomes negligible, so the time complexity is approximated as `O(n)`.

### Example of Dominant Terms
- For `T(n) = 5n² + 27n + 1005`, as `n` grows large, the `n²` term dominates, and the function simplifies to `O(n²)`.

### Worst Case, Best Case, and Average Case
- Some algorithms’ performance depends on specific data sets, which are analyzed in terms of:
  - **Worst Case**: The algorithm performs poorly with a specific dataset.
  - **Best Case**: The algorithm performs exceptionally well with a specific dataset.
  - **Average Case**: The general performance of the algorithm.
  
### Common Big-O Functions
- Common functions include:
  - **Constant (O(1))**: The running time or space does not change with the input size.
  - **Logarithmic (O(log n))**: The running time or space grows logarithmically as the input size increases.
  - **Linear (O(n))**: The running time or space grows linearly with the input size.
  - **Log-linear (O(n log n))**: The running time or space grows in proportion to `n log n`.
  - **Quadratic (O(n²))**: The running time or space grows quadratically with the input size.
  - **Cubic (O(n³))**: The running time or space grows cubically with the input size.
  - **Exponential (O(2^n))**: The running time or space doubles with each additional element in the input.
  - **Factorial (O(n!))**: The running time or space grows factorially with the input size.
  - **Polynomial (O(n^k))**: General form for powers of `n`, where `k` is a constant greater than 1.
  - **Root (O(√n))**: The running time grows with the square root of the input size.
  - **Double Exponential (O(2^(2^n)))**: The running time or space grows at an extremely fast rate.
  - **Log-Quadratic (O(n log n²))**: A combination of logarithmic and quadratic growth.
  - **Cubic Log (O(n³ log n))**: A combination of cubic and logarithmic growth.
  - **Triangular (O(n(n-1)/2))**: Seen in problems that involve selecting pairs or subsets of items.

### Example Code Analysis
- Consider the following Python fragment:
  ```python
  a = 5
  b = 6
  c = 10
  for i in range(n):
      for j in range(n):
          x = i * i
          y = j * j
          z = i * j
  for k in range(n):
      w = a * k + 45
      v = b * b
      d = 33
  ```
  - The total number of assignment operations is: `T(n) = 3n² + 2n + 4`.
  - As `n` grows, the `n²` term dominates, so the time complexity is `O(n²)`.


## **Amortized analysis** 
It is a technique used in algorithm analysis to determine the average performance (cost) of an operation over a sequence of operations, rather than analyzing each operation in isolation. It gives a more realistic measure of an algorithm's performance when operations vary in cost but occur in predictable patterns.

### Key Concepts in Amortized Analysis:
1. **Sequence of Operations**: Amortized analysis considers the total cost of performing a series of operations rather than individual operations.
2. **Amortized Cost**: It is the average cost of each operation in the sequence when spread evenly over all operations.

### Why Use Amortized Analysis?
- Some algorithms have occasional operations that are expensive (high cost), but the majority of operations are cheap (low cost). Instead of focusing on the worst-case cost of a single operation, amortized analysis spreads the cost over many operations to provide a better sense of the overall efficiency.

### Techniques of Amortized Analysis:
1. **Aggregate Method**:
   - Compute the total cost of a sequence of \( n \) operations.
   - Divide the total cost by \( n \) to get the average (amortized) cost per operation.
   - Example: Inserting \( n \) elements into a stack where resizing the array doubles its size occurs occasionally.

2. **Accounting Method**:
   - Assign a fixed "amortized cost" to each operation.
   - Charge more than the actual cost for cheap operations and save the excess as a "credit."
   - Use the saved credit to pay for expensive operations.
   - Example: Charging each insertion in a dynamic array extra to account for the cost of resizing when needed.

3. **Potential Method**:
   - Define a potential function \( \Phi \) that represents the "stored energy" of the data structure.
   - The amortized cost is the actual cost plus the change in potential (\( \Delta \Phi \)).
   - Example: Growing or shrinking a dynamic array by adjusting the potential to reflect the current size.

### Example: Amortized Analysis of Dynamic Arrays
Consider a dynamic array that doubles its size when full:
- Inserting elements costs \( O(1) \) most of the time.
- When resizing is needed, it involves copying all current elements to the new array, which costs \( O(n) \) for \( n \) elements.

For \( n \) insertions:
- Total cost: \( O(1 + 2 + 4 + \dots + n) = O(2n - 1) = O(n) \).
- Amortized cost per insertion: \( O(n) / n = O(1) \).

### Benefits of Amortized Analysis:
- Provides a realistic average-case performance.
- Useful for data structures like dynamic arrays, hash tables, splay trees, etc.
- Helps in understanding how occasional high-cost operations are offset by a large number of low-cost operations.

## `timeit` module

The `Timer()` class in the `timeit` module allows more control over benchmarking, especially if you want to run a function multiple times or time specific code snippets in different environments. It provides a way to specify the code to be tested and the setup code that prepares the environment before the test runs.

### Syntax:
```python
timeit.Timer(stmt, setup)
```
- `stmt`: The code you want to time (as a string).
- `setup`: The setup code that runs before the statement (`stmt`) (as a string).
- `Timer()` is often used in conjunction with the `timeit()` method to run the timing code.

### Example:
```python
import timeit

# Define the function to be tested
def test1():
    return sum(range(100))

# Create a Timer object
t1 = timeit.Timer("test1()", "from __main__ import test1")

# Run the timer for a specified number of executions (e.g., 1000 times)
execution_time = t1.timeit(number=1000)

print(f"Execution time: {execution_time:.10f} seconds")
```

### Explanation:
- **`"test1()"`**: The statement to execute, which calls the `test1()` function.
- **`"from __main__ import test1"`**: This setup code imports `test1` from the current module (useful when testing functions).
- **`t1.timeit(number=1000)`**: This method runs the code `test1()` 1000 times and returns the total execution time.

### Output:
This will print the total time it took for the `test1()` function to run 1000 times.

```plaintext
Execution time: 0.0012345678 seconds
```

### Key Points:
- `Timer()` allows precise control over the setup and execution of the timed code.
- `number=1000` specifies that the code will be executed 1000 times. The `timeit()` method returns the total time for all executions.
- This method is useful for more complex timing needs, such as testing functions with specific setups or multiple code snippets. 


## List Methods and Operators 

| **Operation/Method**      | **Description**                                             | **Time Complexity** | **Space Complexity** | **Notes**                                                                                   |
|----------------------------|-------------------------------------------------------------|----------------------|----------------------|---------------------------------------------------------------------------------------------|
| `append(x)`               | Add an item to the end of the list.                         | O(1)                | O(1)                | Amortized time. Occasional resizing costs O(n).                                             |
| `extend(iterable)`        | Extend list by appending elements from iterable.            | O(k)                | O(k)                | k = len(iterable).                                                                          |
| `insert(i, x)`            | Insert an item at a given position.                         | O(n)                | O(1)                | Moves elements to make space.                                                              |
| `remove(x)`               | Remove first occurrence of value.                           | O(n)                | O(1)                | Scans the list for the element.                                                            |
| `pop([i])`                | Remove and return item at index (or last if not provided).  | O(1)                | O(1)                | O(n) when popping from the middle.                                                         |
| `clear()`                 | Remove all items from the list.                             | O(n)                | O(1)                | Clears references but does not shrink capacity.                                            |
| `index(x, [start], [end])`| Return first index of value.                                | O(n)                | O(1)                | Searches through the list.                                                                 |
| `count(x)`                | Return number of occurrences of value.                     | O(n)                | O(1)                | Traverses the list fully.                                                                  |
| `sort()`                  | Sort the list in place.                                     | O(n log n)          | O(n)                | Timsort algorithm. Stable and fast for most cases.                                         |
| `reverse()`               | Reverse the list in place.                                  | O(n)                | O(1)                |                                                                                             |
| `copy()`                  | Return a shallow copy of the list.                          | O(n)                | O(n)                | Creates a new list.                                                                        |
| Slicing (`list[start:end]`)| Create a sublist from start to end-1.                      | O(k)                | O(k)                | k = size of the slice.                                                                     |
| `+` (concatenation)        | Combine two lists into a new one.                          | O(n + k)            | O(n + k)            | Creates a new list.                                                                        |
| `*` (repetition)           | Repeat list elements multiple times.                      | O(n*k)              | O(n*k)              | Allocates memory for new list.                                                             |
| `==`, `!=`                | Compare element-wise equality.                             | O(n)                | O(1)                | Stops as soon as a difference is found.                                                   |
| `in`, `not in`            | Check membership.                                          | O(n)                | O(1)                | Traverses the list.                                                                        |
| `len()`                   | Return number of items in the list.                        | O(1)                | O(1)                |                                                                                             |
| `min()`, `max()`          | Return smallest or largest item.                           | O(n)                | O(1)                | Traverses the list.                                                                        |
| `sum()`                   | Return sum of all elements.                                | O(n)                | O(1)                | Traverses the list.                                                                        |
| Iteration (`for x in list`)| Iterate over the list.                                     | O(n)                | O(1)                |                                                                                             |
| Deletion (`del list[i]`)   | Remove an item by index.                                   | O(n)                | O(1)                | Elements are shifted.                                                                      |
| `del list[start:end]`      | Delete a slice of elements.                                | O(n)                | O(1)                |                                                                                             |
| `list[i] = x`             | Set the value of an element at index.                      | O(1)                | O(1)                |                                                                                             |
| `list[start:end] = seq`    | Assign a sequence to a slice.                              | O(k + n)            | O(k)                | k = len(seq). Moves elements to fit new sequence.                                          |
| `*=`, `+=` (in-place ops)  | Modify the list in place.                                  | O(k)                | O(k)                | Does not create a new list.                                                                |

## Notes:
1. **n** = Current size of the list.
2. **k** = Size of the additional elements (e.g., for `extend` or slicing).
3. Methods like `append` have an **amortized** complexity due to occasional resizing costs.
4. For slicing and copying, memory usage scales with the size of the resulting list.


## Set Methods and Operators 

| **Operation/Method**        | **Description**                                             | **Average Case**      | **Worst Case**       | **Space Complexity** | **Notes**                                                                                   |
|------------------------------|-------------------------------------------------------------|-----------------------|----------------------|-----------------------|---------------------------------------------------------------------------------------------|
| `add(x)`                    | Add an element to the set.                                  | O(1)                 | O(n)                | O(1)                 | Amortized O(1). Rehashing can occur when resizing.                                          |
| `remove(x)`                 | Remove element x from the set.                              | O(1)                 | O(n)                | O(1)                 | Raises `KeyError` if x is not present.                                                     |
| `discard(x)`                | Remove element x if it exists.                             | O(1)                 | O(n)                | O(1)                 | Does not raise an error if x is missing.                                                   |
| `pop()`                     | Remove and return an arbitrary element.                    | O(1)                 | O(1)                | O(1)                 | Raises `KeyError` if set is empty.                                                         |
| `clear()`                   | Remove all elements from the set.                          | O(n)                 | O(n)                | O(1)                 |                                                                                             |
| `copy()`                    | Return a shallow copy of the set.                          | O(n)                 | O(n)                | O(n)                 | Creates a new set.                                                                          |
| `union(s)`                  | Return a new set with elements from both sets.             | O(len(s) + len(t))   | O(len(s) + len(t))  | O(len(s) + len(t))   | `|` operator can also be used.                                                             |
| `intersection(s)`           | Return a new set with elements common to both sets.        | O(min(len(s), len(t))) | O(len(s) * len(t))  | O(min(len(s), len(t))) | `&` operator can also be used. Replace `min` with `max` if t is not a set.                 |
| `difference(s)`             | Return a new set with elements in this set but not in s.   | O(len(s))            | O(len(s))           | O(len(s))            | `-` operator can also be used.                                                             |
| `symmetric_difference(s)`   | Return a new set with elements in either set but not both. | O(len(s))            | O(len(s) * len(t))  | O(len(s))            | `^` operator can also be used.                                                             |
| `update(s)`                 | Add all elements from s to the set.                        | O(len(s))            | O(len(s))           | O(len(s))            | `|=` operator can also be used.                                                            |
| `intersection_update(s)`    | Update set with intersection of sets.                      | O(len(s))            | O(len(s) * len(t))  | O(len(s))            | `&=` operator can also be used.                                                            |
| `difference_update(s)`      | Update set by removing elements found in s.                | O(len(s))            | O(len(s))           | O(len(s))            | `-=` operator can also be used.                                                            |
| `symmetric_difference_update(s)` | Update set with symmetric difference.                 | O(len(s))            | O(len(s) * len(t))  | O(len(s))            | `^=` operator can also be used.                                                            |
| `issubset(s)`               | Return True if all elements are in s.                      | O(len(s))            | O(len(s))           | O(1)                 | `<=` operator can also be used.                                                           |
| `issuperset(s)`             | Return True if all elements of s are in the set.           | O(len(s))            | O(len(s))           | O(1)                 | `>=` operator can also be used.                                                           |
| `isdisjoint(s)`             | Return True if sets have no elements in common.            | O(min(len(s), len(t))) | O(len(s) * len(t))  | O(1)                 |                                                                                             |
| Iteration (`for x in s`)     | Iterate over the elements of a set.                        | O(n)                 | O(n)                | O(1)                 | Iteration order is arbitrary.                                                              |
| `len(s)`                    | Return the number of elements in the set.                  | O(1)                 | O(1)                | O(1)                 |                                                                                             |
| `x in s`, `x not in s`      | Check membership of an element in the set.                 | O(1)                 | O(n)                | O(1)                 |                                                                                             |

### Notes:
1. **n** = Number of elements in the set.
2. **t** = Size of the other set or iterable.
3. Methods like `add` have amortized O(1) due to occasional resizing during rehashing.

## Dictionary Methods and Operators 

| **Operation/Method**       | **Description**                                             | **Average Case**      | **Worst Case**       | **Space Complexity** | **Notes**                                                                                   |
|-----------------------------|-------------------------------------------------------------|-----------------------|----------------------|-----------------------|---------------------------------------------------------------------------------------------|
| `d[key]`                   | Access the value associated with a key.                     | O(1)                 | O(n)                | O(1)                 | Raises `KeyError` if the key does not exist.                                               |
| `d[key] = value`           | Set or update the value for a key.                          | O(1)                 | O(n)                | O(1)                 | Amortized O(1) due to possible resizing.                                                   |
| `del d[key]`               | Remove a key-value pair by key.                             | O(1)                 | O(n)                | O(1)                 | Raises `KeyError` if the key does not exist.                                               |
| `len(d)`                   | Return the number of items in the dictionary.               | O(1)                 | O(1)                | O(1)                 |                                                                                             |
| `key in d` / `key not in d`| Check if a key exists in the dictionary.                    | O(1)                 | O(n)                | O(1)                 |                                                                                             |
| `d.clear()`                | Remove all key-value pairs from the dictionary.             | O(n)                 | O(n)                | O(1)                 |                                                                                             |
| `d.copy()`                 | Return a shallow copy of the dictionary.                   | O(n)                 | O(n)                | O(n)                 | Creates a new dictionary.                                                                  |
| `d.get(key, default=None)` | Return the value for a key if it exists, otherwise default. | O(1)                 | O(n)                | O(1)                 |                                                                                             |
| `d.setdefault(key, default=None)` | Return the value of a key, setting it to default if not present. | O(1)      | O(n)                | O(1)                 |                                                                                             |
| `d.pop(key)`               | Remove a key and return its value.                          | O(1)                 | O(n)                | O(1)                 | Raises `KeyError` if the key does not exist.                                               |
| `d.popitem()`              | Remove and return an arbitrary key-value pair.              | O(1)                 | O(1)                | O(1)                 | Raises `KeyError` if the dictionary is empty.                                              |
| `d.update([other])`        | Update dictionary with key-value pairs from `other`.        | O(len(other))        | O(len(other))       | O(len(other))        |                                                                                             |
| `d.keys()`                 | Return a view object of dictionary keys.                   | O(1)                 | O(1)                | O(n)                 |                                                                                             |
| `d.values()`               | Return a view object of dictionary values.                 | O(1)                 | O(1)                | O(n)                 |                                                                                             |
| `d.items()`                | Return a view object of dictionary key-value pairs.         | O(1)                 | O(1)                | O(n)                 |                                                                                             |
| Iteration (`for k in d`)   | Iterate over keys.                                          | O(n)                 | O(n)                | O(1)                 | Iteration order matches insertion order (Python 3.7+).                                     |
| `dict.fromkeys(seq, value)`| Create a new dictionary with keys from `seq` and set values to `value`. | O(len(seq)) | O(len(seq))       | O(len(seq))          |                                                                                             |

### Notes:
1. **n** = Number of elements in the dictionary.
2. Operations like `set`, `del`, and `get` are O(1) on average but can degrade to O(n) during collisions or resizing.
3. Iteration and space complexities depend on the number of elements.

## `defaultdict` Methods and Operators 

| **Operation/Method**               | **Description**                                                | **Average Case**      | **Worst Case**       | **Space Complexity** | **Notes**                                                                                   |
|-------------------------------------|----------------------------------------------------------------|-----------------------|----------------------|-----------------------|---------------------------------------------------------------------------------------------|
| `d[key]`                           | Access the value associated with a key, creating a default if it does not exist. | O(1)                 | O(n)                | O(1)                 | If the key is missing, `default_factory` is called to create a default value.              |
| `d[key] = value`                   | Set or update the value for a key.                             | O(1)                 | O(n)                | O(1)                 | Amortized O(1) due to possible resizing.                                                   |
| `del d[key]`                       | Remove a key-value pair by key.                                | O(1)                 | O(n)                | O(1)                 | Raises `KeyError` if the key does not exist.                                               |
| `len(d)`                           | Return the number of items in the dictionary.                  | O(1)                 | O(1)                | O(1)                 |                                                                                             |
| `key in d` / `key not in d`        | Check if a key exists in the dictionary.                       | O(1)                 | O(n)                | O(1)                 |                                                                                             |
| `d.clear()`                        | Remove all key-value pairs from the dictionary.                | O(n)                 | O(n)                | O(1)                 |                                                                                             |
| `d.copy()`                         | Return a shallow copy of the `defaultdict`.                    | O(n)                 | O(n)                | O(n)                 |                                                                                             |
| `d.get(key, default=None)`         | Return the value for a key if it exists, otherwise default.     | O(1)                 | O(n)                | O(1)                 |                                                                                             |
| `d.setdefault(key, default=None)`  | Return the value of a key, setting it to default if not present.| O(1)                | O(n)                | O(1)                 | Uses the `default_factory` if key does not exist and no default is provided.               |
| `d.pop(key)`                       | Remove a key and return its value.                             | O(1)                 | O(n)                | O(1)                 | Raises `KeyError` if the key does not exist.                                               |
| `d.popitem()`                      | Remove and return an arbitrary key-value pair.                 | O(1)                 | O(1)                | O(1)                 | Raises `KeyError` if the dictionary is empty.                                              |
| `d.update([other])`                | Update dictionary with key-value pairs from `other`.           | O(len(other))        | O(len(other))       | O(len(other))        |                                                                                             |
| `d.keys()`                         | Return a view object of dictionary keys.                      | O(1)                 | O(1)                | O(n)                 |                                                                                             |
| `d.values()`                       | Return a view object of dictionary values.                    | O(1)                 | O(1)                | O(n)                 |                                                                                             |
| `d.items()`                        | Return a view object of dictionary key-value pairs.            | O(1)                 | O(1)                | O(n)                 |                                                                                             |
| Iteration (`for k in d`)           | Iterate over keys.                                             | O(n)                 | O(n)                | O(1)                 | Iteration order matches insertion order (Python 3.7+).                                     |
| `defaultdict(default_factory)`     | Initialize a `defaultdict` with a callable `default_factory`.  | O(1)                 | O(1)                | O(1)                 | Default values are created lazily when missing keys are accessed.                          |

### Notes:
1. `defaultdict` inherits most of its behavior and performance from `dict`.
2. **n** = Number of elements in the dictionary.
3. Operations like `set`, `del`, and `get` are O(1) on average but can degrade to O(n) during collisions or resizing.
4. The `default_factory` can be any callable (e.g., `int`, `list`, `lambda: 0`), and it is only called when a missing key is accessed.

---

## `Counter` Methods and Operations 

| **Operation/Method**               | **Description**                                                | **Average Case**      | **Worst Case**       | **Space Complexity** | **Notes**                                                                                   |
|-------------------------------------|----------------------------------------------------------------|-----------------------|----------------------|-----------------------|---------------------------------------------------------------------------------------------|
| `c[key]`                           | Access the count of `key`, returns `0` if `key` is missing.    | O(1)                 | O(n)                | O(1)                 | Key lookup behaves like a dictionary.                                                      |
| `c[key] = value`                   | Set the count for `key`.                                       | O(1)                 | O(n)                | O(1)                 | Setting a count to `0` does not remove the key.                                            |
| `del c[key]`                       | Remove a key from the `Counter`.                               | O(1)                 | O(n)                | O(1)                 |                                                                                             |
| `key in c`                         | Check if a key exists in the `Counter`.                        | O(1)                 | O(n)                | O(1)                 | Returns `True` even if the count is `0`.                                                   |
| `len(c)`                           | Return the number of unique elements in the `Counter`.         | O(1)                 | O(1)                | O(1)                 | Does not consider counts.                                                                  |
| `c.clear()`                        | Remove all elements from the `Counter`.                        | O(n)                 | O(n)                | O(1)                 |                                                                                             |
| `c.copy()`                         | Return a shallow copy of the `Counter`.                        | O(n)                 | O(n)                | O(n)                 |                                                                                             |
| `c.most_common([n])`               | Return the `n` most common elements and their counts.          | O(n log n)           | O(n log n)          | O(n)                 | If `n` is omitted, returns all elements in descending order of count.                      |
| `c.elements()`                     | Return an iterator over elements repeated as per their counts. | O(sum(c.values()))   | O(sum(c.values()))  | O(sum(c.values()))   | Does not include elements with counts ≤ 0.                                                |
| `c.subtract(iterable_or_mapping)`  | Subtract counts from `iterable_or_mapping`.                    | O(len(iterable))     | O(len(iterable))    | O(len(iterable))     | Counts can go negative.                                                                    |
| `c.update(iterable_or_mapping)`    | Add counts from `iterable_or_mapping`.                         | O(len(iterable))     | O(len(iterable))    | O(len(iterable))     |                                                                                             |
| `c + other`                        | Add two `Counter` objects.                                     | O(len(c) + len(other))| O(len(c) + len(other)) | O(len(c) + len(other)) | Elements with zero or negative counts are not included.                                    |
| `c - other`                        | Subtract counts, keeping only positive counts.                 | O(len(c) + len(other))| O(len(c) + len(other)) | O(len(c) + len(other)) |                                                                                             |
| `c & other`                        | Return minimum of corresponding counts.                        | O(len(c) + len(other))| O(len(c) + len(other)) | O(len(c) + len(other)) | Equivalent to intersection on counts.                                                     |
| `c | other`                        | Return maximum of corresponding counts.                        | O(len(c) + len(other))| O(len(c) + len(other)) | O(len(c) + len(other)) | Equivalent to union on counts.                                                             |
| Iteration (`for k in c`)           | Iterate over keys with non-zero counts.                        | O(n)                 | O(n)                | O(1)                 |                                                                                             |
| `sum(c.values())`                  | Return the total of all counts.                                | O(n)                 | O(n)                | O(1)                 |                                                                                             |
| `dict(c)`                          | Convert `Counter` to a regular dictionary.                     | O(n)                 | O(n)                | O(n)                 |                                                                                             |
| `+` / `-` / `&` / `\|`              | Operators for addition, subtraction, intersection, and union.  | O(n)                 | O(n)                | O(n)                 |                                                                                             |

### Notes:
1. **n** = Number of unique elements in the `Counter`.
2. Operations like `set`, `del`, `get`, and `len` behave like dictionary operations.
3. Negative and zero counts are valid but may not appear in certain operations like `elements()` or arithmetic results.
4. The `most_common()` method uses sorting, which contributes to its O(n log n) complexity.


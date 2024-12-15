# What is Computer Science?

- **Definition and Scope:**
  - Computer science studies problems, problem-solving, and solutions.
  - It is not just about computers; they are tools to implement solutions.
  - Focuses on algorithms—step-by-step instructions for solving problems.

- **Nature of Problems:**
  - Includes both computable (solvable) and non-computable (unsolvable) problems.
  - Computable problems have algorithms; non-computable problems lack them.

- **Abstraction in Problem-Solving:**
  - Separates logical (interface) and physical (implementation) perspectives.
  - Logical view: Focus on functionality without knowing the underlying details.
  - Physical view: In-depth understanding of system mechanics (e.g., programming, system operations).

- **Black Box Concept:**
  - Interfaces provide functionality without exposing implementation details.
  - Users need to know how to interact with the interface, not how it works internally.

- **Examples of Abstraction:**
  - Using a car (logical: driving; physical: engine mechanics).
  - Using Python's `math.sqrt()` function (logical: call and input; physical: hidden computation).

- **Practical Application:**
  - Users interact with systems at a high level (e.g., apps, email, web).
  - Professionals handle low-level complexities (e.g., coding, system configurations).

---

# What Is Programming?
- **Definition:**
  - Programming encodes algorithms into a programming language for execution by a computer.
  - Requires an algorithm; without it, programming is impossible.

- **Relation to Computer Science:**
  - Computer science is not the study of programming. Programming, however, is an important part of what a computer scientist does. 
  - Programming is often the way that we create a representation for our solutions. Therefore, this language representation and the process of creating it becomes a fundamental part of the discipline.

- **Key Components of Programming:**
  - **Algorithms:** Describe the problem and steps for solving it, including data representation and control structures.
  - **Control Constructs:** Allow representation of algorithmic steps (e.g., sequence, selection, iteration statements).
  - **Data Types:** Interpret binary data meaningfully(abstraction on binary string and also enabling operations on them), enabling operations like arithmetic on integers.

- **Challenges:**
  - Problems and solutions can be highly complex.
  - Programming tools like basic constructs and data types, while adequate, often require additional methods to manage complexity. Hence we require Abstract Data Type on top of these. 

---

# Why Study Data Structures and Abstract Data Types? 

- **Purpose of Abstraction:**
  - Helps manage problem complexity by focusing on the "big picture."
  - Models data consistently, aligning algorithms with the problem domain.

- **Abstract Data Types (ADTs):**
  - Provide a logical description of data and its operations without focusing on implementation.
  - Emphasize **what** the data represents, not **how** it is built.
  - Enable **information hiding** by encapsulating implementation details.

- **User Interaction:**
  - Users interact with ADTs via an interface, unaware of implementation details hidden beneath.

- **Implementation:**
  - ADTs are implemented using data structures, primitive data types, and programming constructs.
  - The separation of abstract and physical views ensures implementation independence.

- **Benefits:**
  - Allows flexibility in switching implementations without affecting user interaction.
  - Keeps users focused on solving problems rather than implementation specifics.

---

# Why Study Algorithms? 

- **Learning Through Practice:**
  - Exposure to diverse algorithms improves problem-solving skills and pattern recognition for tackling new challenges.

- **Diversity in Algorithms:**
  - Algorithms can differ significantly in resource usage, speed, and efficiency.
  - Comparing algorithms helps identify the "better" solution based on characteristics like time or memory usage.

- **Algorithm Analysis:**
  - Enables evaluation of solutions independently of programming or hardware constraints.
  - Helps distinguish between solvable problems, unsolvable ones, and those with impractical solutions (intractable problems).

- **Trade-offs and Evaluation:**
  - Understanding trade-offs is essential in selecting the most suitable algorithm.
  - Evaluating and optimizing solutions is a recurring task for computer scientists.
  
---

# Python Keywords

Below is a list of all Python keywords as of Python 3.10.

| **Keyword**     | **Description**                                                                 |
|------------------|---------------------------------------------------------------------------------|
| `False`         | Boolean value representing false.                                              |
| `None`          | Represents the absence of a value.                                             |
| `True`          | Boolean value representing true.                                               |
| `and`           | Logical AND operator.                                                          |
| `as`            | Used to create an alias (e.g., for modules or exceptions).                     |
| `assert`        | Used for debugging; tests a condition.                                         |
| `async`         | Defines asynchronous functions or behavior.                                    |
| `await`         | Used within `async` functions to pause execution until a task is completed.    |
| `break`         | Exits a loop prematurely.                                                      |
| `class`         | Used to define a class.                                                        |
| `continue`      | Skips the rest of the loop's current iteration.                                |
| `def`           | Used to define a function.                                                     |
| `del`           | Deletes an object.                                                            |
| `elif`          | Else if; conditional statement.                                                |
| `else`          | Defines the block of code to execute if no `if` or `elif` condition is met.    |
| `except`        | Defines a block of code to handle exceptions.                                  |
| `finally`       | Defines a block of code that executes after `try` and `except` blocks.         |
| `for`           | Starts a for loop.                                                            |
| `from`          | Used to import specific parts of a module.                                     |
| `global`        | Declares a global variable.                                                    |
| `if`            | Starts a conditional statement.                                                |
| `import`        | Imports a module.                                                             |
| `in`            | Tests for membership in a sequence.                                            |
| `is`            | Tests for object identity.                                                     |
| `lambda`        | Defines an anonymous function.                                                |
| `nonlocal`      | Declares a non-local variable in a nested function.                            |
| `not`           | Logical NOT operator.                                                         |
| `or`            | Logical OR operator.                                                          |
| `pass`          | A null statement; does nothing.                                                |
| `raise`         | Raises an exception.                                                          |
| `return`        | Exits a function and optionally returns a value.                              |
| `try`           | Defines a block of code to test for exceptions.                                |
| `while`         | Starts a while loop.                                                          |
| `with`          | Simplifies exception handling for resources like file handling.               |
| `yield`         | Pauses a generator function and returns a value to the caller.                |



### Notes:
- Keywords are case-sensitive.
- For an up-to-date list of Python keywords, use the command:
  ```python
  import keyword
  print(keyword.kwlist)
  ```
---

# Python Operators

Below is a categorized list of all Python operators.

| **Category**          | **Operator**      | **Description**                                                                                   | **Example**               |
|------------------------|-------------------|---------------------------------------------------------------------------------------------------|---------------------------|
| **Arithmetic**        | `+`              | Addition                                                                                        | `5 + 3` → `8`             |
|                        | `-`              | Subtraction                                                                                     | `5 - 3` → `2`             |
|                        | `*`              | Multiplication                                                                                  | `5 * 3` → `15`            |
|                        | `/`              | Division                                                                                        | `5 / 3` → `1.666...`      |
|                        | `//`             | Floor Division                                                                                  | `5 // 3` → `1`            |
|                        | `%`              | Modulus (remainder)                                                                             | `5 % 3` → `2`             |
|                        | `**`             | Exponentiation                                                                                  | `5 ** 3` → `125`          |
| **Comparison**         | `==`             | Equal to                                                                                        | `5 == 3` → `False`        |
|                        | `!=`             | Not equal to                                                                                    | `5 != 3` → `True`         |
|                        | `>`              | Greater than                                                                                    | `5 > 3` → `True`          |
|                        | `<`              | Less than                                                                                       | `5 < 3` → `False`         |
|                        | `>=`             | Greater than or equal to                                                                        | `5 >= 3` → `True`         |
|                        | `<=`             | Less than or equal to                                                                           | `5 <= 3` → `False`        |
| **Logical**            | `and`            | Logical AND                                                                                     | `True and False` → `False`|
|                        | `or`             | Logical OR                                                                                      | `True or False` → `True`  |
|                        | `not`            | Logical NOT                                                                                     | `not True` → `False`      |
| **Bitwise**            | `&`              | Bitwise AND                                                                                     | `5 & 3` → `1`             |
|                        | `|`              | Bitwise OR                                                                                      | `5 | 3` → `7`             |
|                        | `^`              | Bitwise XOR                                                                                     | `5 ^ 3` → `6`             |
|                        | `~`              | Bitwise NOT                                                                                     | `~5` → `-6`              |
|                        | `<<`             | Left Shift                                                                                      | `5 << 1` → `10`           |
|                        | `>>`             | Right Shift                                                                                     | `5 >> 1` → `2`            |
| **Assignment**         | `=`              | Assigns value to a variable                                                                     | `x = 5`                   |
|                        | `+=`             | Adds and assigns value                                                                          | `x += 3`                  |
|                        | `-=`             | Subtracts and assigns value                                                                     | `x -= 3`                  |
|                        | `*=`             | Multiplies and assigns value                                                                    | `x *= 3`                  |
|                        | `/=`             | Divides and assigns value                                                                       | `x /= 3`                  |
|                        | `//=`            | Floor divides and assigns value                                                                 | `x //= 3`                 |
|                        | `%=`             | Modulus and assigns value                                                                       | `x %= 3`                  |
|                        | `**=`            | Exponentiates and assigns value                                                                 | `x **= 3`                 |
|                        | `&=`             | Bitwise AND and assigns value                                                                   | `x &= 3`                  |
|                        | `|=`             | Bitwise OR and assigns value                                                                    | `x |= 3`                  |
|                        | `^=`             | Bitwise XOR and assigns value                                                                   | `x ^= 3`                  |
|                        | `<<=`            | Left shift and assigns value                                                                    | `x <<= 1`                 |
|                        | `>>=`            | Right shift and assigns value                                                                   | `x >>= 1`                 |
| **Membership**         | `in`             | Checks if a value is in a sequence                                                              | `'a' in 'apple'` → `True`|
|                        | `not in`         | Checks if a value is not in a sequence                                                         | `'b' not in 'apple'` → `True` |
| **Identity**           | `is`             | Checks if two objects are the same                                                              | `x is y`                  |
|                        | `is not`         | Checks if two objects are not the same                                                         | `x is not y`              |


### Notes:
- Operators like `and`, `or`, and `not` are logical operators and cannot be overloaded.
- Python also supports operator overloading for custom classes via magic methods like `__add__`, `__sub__`, etc.

---

# Python Magic Methods

Magic methods, also known as dunder methods (short for **double underscore**), are special methods in Python that start and end with double underscores (`__`). They enable custom behavior for Python objects and support operator overloading, type conversion, and more. Below is an exhaustive table of Python's magic methods grouped by functionality.

| **Category**              | **Magic Method**       | **Description**                                                                                                   |
|---------------------------|------------------------|-------------------------------------------------------------------------------------------------------------------|
| **Initialization**        | `__init__`            | Called when an instance is initialized.                                                                           |
|                           | `__new__`             | Creates and returns a new instance of the class.                                                                 |
| **String Representation** | `__str__`             | Called by `str()` or `print()` to return a human-readable string representation.                                  |
|                           | `__repr__`            | Called by `repr()` to return an official string representation.                                                  |
|                           | `__format__`          | Called by `format()` or `f-strings`.                                                                             |
|                           | `__bytes__`           | Called by `bytes()` to return a byte representation.                                                             |
| **Arithmetic Operations** | `__add__`             | Implements addition (`+`).                                                                                       |
|                           | `__radd__`            | Implements reflected addition.                                                                                   |
|                           | `__sub__`             | Implements subtraction (`-`).                                                                                    |
|                           | `__rsub__`            | Implements reflected subtraction.                                                                                |
|                           | `__mul__`             | Implements multiplication (`*`).                                                                                 |
|                           | `__rmul__`            | Implements reflected multiplication.                                                                             |
|                           | `__truediv__`         | Implements true division (`/`).                                                                                  |
|                           | `__rtruediv__`        | Implements reflected true division.                                                                              |
|                           | `__floordiv__`        | Implements floor division (`//`).                                                                                |
|                           | `__rfloordiv__`       | Implements reflected floor division.                                                                             |
|                           | `__mod__`             | Implements modulus (`%`).                                                                                        |
|                           | `__rmod__`            | Implements reflected modulus.                                                                                    |
|                           | `__pow__`             | Implements exponentiation (`**`).                                                                                |
|                           | `__rpow__`            | Implements reflected exponentiation.                                                                             |
|                           | `__neg__`             | Implements unary negation (`-x`).                                                                                |
|                           | `__pos__`             | Implements unary positive (`+x`).                                                                                |
|                           | `__abs__`             | Implements absolute value (`abs(x)`).                                                                            |
|                           | `__invert__`          | Implements bitwise NOT (`~x`).                                                                                   |
|                           | `__and__`             | Implements bitwise AND (`&`).                                                                                    |
|                           | `__rand__`            | Implements reflected bitwise AND.                                                                                |
|                           | `__or__`              | Implements bitwise OR (`|`).                                                                                     |
|                           | `__ror__`             | Implements reflected bitwise OR.                                                                                 |
|                           | `__xor__`             | Implements bitwise XOR (`^`).                                                                                    |
|                           | `__rxor__`            | Implements reflected bitwise XOR.                                                                                |
|                           | `__lshift__`          | Implements left shift (`<<`).                                                                                    |
|                           | `__rlshift__`         | Implements reflected left shift.                                                                                 |
|                           | `__rshift__`          | Implements right shift (`>>`).                                                                                   |
|                           | `__rrshift__`         | Implements reflected right shift.                                                                                |
| **Comparison Operations** | `__lt__`             | Implements less than (`<`).                                                                                      |
|                           | `__le__`             | Implements less than or equal to (`<=`).                                                                         |
|                           | `__eq__`             | Implements equality (`==`).                                                                                      |
|                           | `__ne__`             | Implements inequality (`!=`).                                                                                    |
|                           | `__gt__`             | Implements greater than (`>`).                                                                                   |
|                           | `__ge__`             | Implements greater than or equal to (`>=`).                                                                      |
| **Container Emulation**   | `__getitem__`         | Called to retrieve an item using the index (`obj[key]`), Also functions as slice.                                                         |
|                           | `__setitem__`         | Called to set an item using the index (`obj[key] = value`).                                                      |
|                           | `__delitem__`         | Called to delete an item using the index (`del obj[key]`).                                                       |
|                           | `__len__`             | Returns the length of the object (`len(obj)`).                                                                   |
|                           | `__iter__`            | Returns an iterator object for the container.                                                                    |
|                           | `__next__`            | Returns the next item from an iterator.                                                                          |
|                           | `__contains__`        | Called to check membership (`value in obj`).                                                                     |
| **Callable Objects**      | `__call__`            | Makes an instance callable like a function.                                                                      |
| **Context Management**    | `__enter__`           | Defines the setup actions for a context manager (`with` statement).                                              |
|                           | `__exit__`            | Defines the cleanup actions for a context manager (`with` statement).                                            |
| **Type Conversion**       | `__int__`             | Converts an object to an integer (`int(obj)`).                                                                   |
|                           | `__float__`           | Converts an object to a float (`float(obj)`).                                                                    |
|                           | `__complex__`         | Converts an object to a complex number (`complex(obj)`).                                                         |
|                           | `__bool__`            | Converts an object to a boolean (`bool(obj)`).                                                                   |
|                           | `__hash__`            | Returns the hash value of an object (`hash(obj)`).                                                               |
| **Attribute Access**      | `__getattr__`         | Called when an attribute is accessed but not found in the instance.                                              |
|                           | `__setattr__`         | Called when an attribute is set.                                                                                 |
|                           | `__delattr__`         | Called when an attribute is deleted.                                                                             |
|                           | `__dir__`             | Called by `dir()` to list an object's attributes.                                                                |
| **Object Lifecycle**      | `__del__`             | Defines cleanup behavior when an object is garbage collected.                                                    |
| **Other Special Methods** | `__slots__`           | Limits the attributes that can be set on an object.                                                              |
|                           | `__sizeof__`          | Returns the size of an object in memory.                                                                         |
|                           | `__class__`           | Accesses the class of an instance.                                                                               |
|                           | `__subclasshook__`    | Used to customize `issubclass()` behavior.                                                                       |

### Notes:
- Magic methods allow developers to implement custom behavior and integrate seamlessly with Python's syntax.
- Most magic methods are optional; only use them when needed to add specific functionality.

---

# Python Primitive Data Types

| **Type**      | **Description**                                                                                  | **Example**                      |
|---------------|--------------------------------------------------------------------------------------------------|----------------------------------|
| `int`         | Represents whole numbers, positive or negative.                                                 | `x = 42`, `y = -10`              |
| `float`       | Represents real numbers with decimal points, positive or negative.                              | `x = 3.14`, `y = -2.71`          |
| `complex`     | Represents complex numbers with real and imaginary parts.                                        | `z = 1 + 2j`, `w = -3 - 4j`      |
| `bool`        | Represents truth values: `True` or `False`.                                                     | `x = True`, `y = False`          |
| `str`         | Represents a sequence of characters (text).                                                     | `x = "hello"`, `y = 'world'`     |
| `bytes`       | Represents immutable sequences of bytes.                                                        | `x = b"hello"`                   |
| `bytearray`   | Represents mutable sequences of bytes.                                                          | `x = bytearray(b"hello")`        |
| `memoryview`  | Represents a memory view object that provides access to internal buffer data of objects like `bytes`. | `x = memoryview(b"hello")`      |
| `NoneType`    | Represents the absence of a value or a null value.                                               | `x = None`                       |

---

# Python Collection Data Types

| **Type**         | **Description**                                                                                             | **Example**                              |
|-------------------|-----------------------------------------------------------------------------------------------------------|------------------------------------------|
| `list`           | An ordered, mutable collection of items, which can contain elements of different types.                    | `x = [1, 2, 3, "hello"]`                 |
| `tuple`          | An ordered, immutable collection of items, which can contain elements of different types.                  | `x = (1, 2, 3, "world")`                 |
| `set`            | An unordered, mutable collection of unique items.                                                         | `x = {1, 2, 3}`                          |
| `frozenset`      | An unordered, immutable collection of unique items.                                                       | `x = frozenset([1, 2, 3])`               |
| `dict`           | An unordered collection of key-value pairs, where keys are unique and immutable.                          | `x = {"a": 1, "b": 2}`                   |
| `collections.deque` | A double-ended queue that supports fast appends and pops from either end.                                  | `from collections import deque; x = deque([1, 2, 3])` |
| `collections.Counter` | A dictionary subclass for counting hashable objects.                                                   | `from collections import Counter; x = Counter("hello")` |
| `collections.OrderedDict` | A dictionary subclass that remembers the insertion order of keys.                                  | `from collections import OrderedDict; x = OrderedDict([('a', 1), ('b', 2)])` |
| `collections.defaultdict` | A dictionary subclass that provides a default value for missing keys.                              | `from collections import defaultdict; x = defaultdict(int)` |
| `collections.ChainMap` | Combines multiple dictionaries into a single, logical dictionary.                                     | `from collections import ChainMap; x = ChainMap({'a': 1}, {'b': 2})` |
| `collections.namedtuple` | Factory function for creating tuple subclasses with named fields.                                   | `from collections import namedtuple; Point = namedtuple('Point', 'x y'); p = Point(1, 2)` |


### Key Points:
1. **Mutability**:
   - Mutable: `list`, `set`, `dict`, `deque`, `Counter`, `defaultdict`, `ChainMap`.
   - Immutable: `tuple`, `frozenset`, `OrderedDict` (keys are ordered, values are mutable).
2. **Unique Elements**:
   - `set` and `frozenset` only allow unique items.
3. **Ordering**:
   - Ordered: `list`, `tuple`, `dict` (Python 3.7+), `OrderedDict`, `deque`, `namedtuple`.
   - Unordered: `set`, `frozenset`.

---

# Python List Methods

Below is a comprehensive table of Python's built-in list methods, their descriptions, and usage.

| **Method**      | **Description**                                                                                 | **Usage**                                     |
|------------------|-----------------------------------------------------------------------------------------------|-----------------------------------------------|
| `append(x)`     | Adds an item `x` to the end of the list.                                                       | `lst.append(10)`                              |
| `extend(iter)`  | Extends the list by appending all elements from the iterable `iter`.                           | `lst.extend([1, 2, 3])`                       |
| `insert(i, x)`  | Inserts an item `x` at the specified index `i`.                                                | `lst.insert(1, 'a')`                          |
| `remove(x)`     | Removes the first occurrence of the item `x`.                                                  | `lst.remove(2)`                               |
| `pop([i])`      | Removes and returns the item at index `i` (or the last item if `i` is omitted).                | `lst.pop()`                                   |
| `clear()`       | Removes all items from the list.                                                               | `lst.clear()`                                 |
| `index(x, [start, [end]])` | Returns the index of the first occurrence of `x` in the list, optionally within a range.     | `lst.index(3, 0, 5)`                          |
| `count(x)`      | Returns the number of occurrences of `x` in the list.                                          | `lst.count(4)`                                |
| `sort(key=None, reverse=False)` | Sorts the items in the list in ascending order (or descending if `reverse=True`).          | `lst.sort(reverse=True)`                      |
| `reverse()`     | Reverses the items in the list in place.                                                       | `lst.reverse()`                               |
| `copy()`        | Returns a shallow copy of the list.                                                            | `copied_list = lst.copy()`                    |


### Notes:
1. **Mutability**: All list methods (except `copy`) modify the list in place, which means they do not return a new list.
2. **Error Handling**: 
   - `remove(x)` raises a `ValueError` if `x` is not in the list.
   - `pop([i])` raises an `IndexError` if the list is empty or the index `i` is out of range.
3. **Sorting Customization**: The `sort()` method allows sorting based on a custom `key` function.

---

# Python Set Methods and Operators

## **Set Methods**

| **Method**            | **Description**                                                                                 | **Usage Example**                     |
|------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------|
| `add(x)`              | Adds an element `x` to the set. If `x` already exists, it has no effect.                        | `s.add(5)`                            |
| `clear()`             | Removes all elements from the set.                                                             | `s.clear()`                           |
| `copy()`              | Returns a shallow copy of the set.                                                             | `s2 = s.copy()`                       |
| `difference(*others)` | Returns a set containing the difference between the set and other sets.                        | `s.difference(t)`                     |
| `difference_update(*others)` | Removes elements found in other sets from the set.                                              | `s.difference_update(t)`              |
| `discard(x)`          | Removes the element `x` from the set if it exists. Does not raise an error if `x` is not found. | `s.discard(5)`                        |
| `intersection(*others)` | Returns a set containing elements common to the set and other sets.                             | `s.intersection(t)`                   |
| `intersection_update(*others)` | Updates the set with elements common to the set and other sets.                               | `s.intersection_update(t)`            |
| `isdisjoint(other)`   | Returns `True` if the set has no elements in common with `other`.                               | `s.isdisjoint(t)`                     |
| `issubset(other)`     | Returns `True` if the set is a subset of `other`.                                               | `s.issubset(t)`                       |
| `issuperset(other)`   | Returns `True` if the set is a superset of `other`.                                             | `s.issuperset(t)`                     |
| `pop()`               | Removes and returns an arbitrary element from the set. Raises `KeyError` if the set is empty.  | `s.pop()`                             |
| `remove(x)`           | Removes the element `x` from the set. Raises `KeyError` if `x` is not found.                   | `s.remove(5)`                         |
| `symmetric_difference(other)` | Returns a set with elements in either the set or `other`, but not in both.                     | `s.symmetric_difference(t)`           |
| `symmetric_difference_update(other)` | Updates the set with elements in either the set or `other`, but not in both.               | `s.symmetric_difference_update(t)`    |
| `union(*others)`      | Returns a set containing all unique elements from the set and other sets.                       | `s.union(t, u)`                       |
| `update(*others)`     | Updates the set with elements from other sets.                                                  | `s.update(t, u)`                      |


## **Set Operators**

| **Operator**          | **Description**                                                                                 | **Usage Example**                     |
|------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------|
| `s | t`               | Union of sets `s` and `t`.                                                                     | `{1, 2} | {2, 3}` → `{1, 2, 3}`       |
| `s & t`               | Intersection of sets `s` and `t`.                                                              | `{1, 2} & {2, 3}` → `{2}`            |
| `s - t`               | Difference of sets `s` and `t` (elements in `s` but not in `t`).                                | `{1, 2} - {2, 3}` → `{1}`            |
| `s ^ t`               | Symmetric difference of sets `s` and `t` (elements in either `s` or `t`, but not both).         | `{1, 2} ^ {2, 3}` → `{1, 3}`         |
| `s <= t`              | Checks if `s` is a subset of `t`.                                                              | `{1} <= {1, 2}` → `True`             |
| `s < t`               | Checks if `s` is a proper subset of `t`.                                                       | `{1} < {1, 2}` → `True`              |
| `s >= t`              | Checks if `s` is a superset of `t`.                                                            | `{1, 2} >= {2}` → `True`             |
| `s > t`               | Checks if `s` is a proper superset of `t`.                                                     | `{1, 2} > {2}` → `True`              |
| `s == t`              | Checks if `s` and `t` have the same elements.                                                  | `{1, 2} == {2, 1}` → `True`          |
| `s != t`              | Checks if `s` and `t` have different elements.                                                 | `{1, 2} != {2, 3}` → `True`          |


### Key Points:
1. **Mutability**:
   - `set` is mutable; methods like `add`, `remove`, and `update` modify the set in place.
   - `frozenset` is immutable and does not have mutating methods (e.g., `add`, `remove`).
2. **Efficiency**:
   - Sets are implemented using hash tables, providing average O(1) complexity for operations like `add`, `remove`, and `lookup`.
3. **Set Operators**:
   - Operators like `|`, `&`, `-`, and `^` do not modify the original sets; they return new sets.

---

# Dictionary

| Method/Operator               | Description                                                                                 |
|-------------------------------|---------------------------------------------------------------------------------------------|
| `dict.clear()`                 | Removes all items from the dictionary.                                                     |
| `dict.copy()`                  | Returns a shallow copy of the dictionary.                                                   |
| `dict.fromkeys(iterable, value=None)` | Creates a new dictionary with keys from `iterable` and values set to `value`.             |
| `dict.get(key, default=None)`  | Returns the value for `key` if `key` exists, else returns `default`.                        |
| `dict.items()`                 | Returns a view object that displays a list of a dictionary's key-value tuple pairs.         |
| `dict.keys()`                  | Returns a view object that displays a list of all the dictionary's keys.                   |
| `dict.pop(key, default=None)`  | Removes the specified key and returns its value. If the key does not exist, returns `default`.|
| `dict.popitem()`               | Removes and returns a random (key, value) pair from the dictionary.                         |
| `dict.setdefault(key, default=None)` | Returns the value of `key` if it exists, else sets and returns `default`.              |
| `dict.update([other])`         | Updates the dictionary with key-value pairs from another dictionary or an iterable.        |
| `dict.values()`                | Returns a view object that displays a list of all the dictionary's values.                 |
| `del dict[key]`                | Deletes the specified key and its associated value from the dictionary.                     |
| `key in dict`                  | Checks if the `key` exists in the dictionary (returns a boolean).                           |
| `key not in dict`              | Checks if the `key` does not exist in the dictionary (returns a boolean).                  |
| `dict == other`                | Compares if two dictionaries are equal (both have the same keys and values).               |
| `dict != other`                | Checks if two dictionaries are not equal.                                                   |
| `dict[key]`                    | Retrieves the value associated with `key`.                                                  |
| `dict[key] = value`            | Assigns `value` to the specified `key`.                                                     |
| `dict`                         | Represents the dictionary object.                                                           |

--- 

# String Methods

| Method/Operator                    | Description                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| `str.capitalize()`                  | Returns a copy of the string with the first character capitalized and the rest lowercased.          |
| `str.casefold()`                    | Returns a casefolded copy of the string, used for case-insensitive comparisons.                     |
| `str.center(width, fillchar=' ')`   | Centers the string in a field of width `width` and pads it with `fillchar` (default is a space).    |
| `str.count(substring, start=0, end=-1)` | Returns the number of occurrences of `substring` in the string between `start` and `end`.          |
| `str.encode(encoding='utf-8', errors='strict')` | Encodes the string using the specified `encoding` and returns a bytes object.              |
| `str.endswith(suffix, start=0, end=-1)` | Checks if the string ends with `suffix` within the specified range (`start` to `end`).           |
| `str.expandtabs(tabsize=8)`         | Expands tab characters (`\t`) in the string to spaces, with a default `tabsize` of 8.               |
| `str.find(substring, start=0, end=-1)` | Returns the lowest index where `substring` is found in the string, or -1 if not found.            |
| `str.format(*args, **kwargs)`       | Performs string formatting, inserting values into the placeholders within the string.               |
| `str.format_map(mapping)`           | Similar to `str.format()`, but uses a dictionary (`mapping`) for formatting instead of positional args. |
| `str.index(substring, start=0, end=-1)` | Like `find()`, but raises a `ValueError` if `substring` is not found.                            |
| `str.isalnum()`                     | Returns `True` if all characters in the string are alphanumeric (letters and digits), otherwise `False`. |
| `str.isalpha()`                     | Returns `True` if all characters in the string are alphabetic, otherwise `False`.                 |
| `str.isdecimal()`                   | Returns `True` if all characters in the string are decimal characters, otherwise `False`.         |
| `str.isdigit()`                     | Returns `True` if all characters in the string are digits, otherwise `False`.                     |
| `str.islower()`                     | Returns `True` if all characters in the string are lowercase, otherwise `False`.                   |
| `str.isnumeric()`                   | Returns `True` if all characters in the string are numeric, otherwise `False`.                     |
| `str.isprintable()`                 | Returns `True` if all characters in the string are printable, otherwise `False`.                   |
| `str.isspace()`                     | Returns `True` if all characters in the string are whitespace, otherwise `False`.                  |
| `str.istitle()`                     | Returns `True` if the string is in title case, otherwise `False`.                                  |
| `str.isupper()`                     | Returns `True` if all characters in the string are uppercase, otherwise `False`.                   |
| `str.join(iterable)`                | Concatenates the elements of `iterable` (strings) with the string as the separator.                 |
| `str.ljust(width, fillchar=' ')`    | Left-aligns the string in a field of width `width` and pads it with `fillchar` (default is a space). |
| `str.lower()`                       | Returns a copy of the string with all characters converted to lowercase.                           |
| `str.lstrip(chars=None)`            | Returns a copy of the string with leading whitespace (or specified `chars`) removed.               |
| `str.maketrans(x, y)`               | Returns a translation table usable for `str.translate()`.                                           |
| `str.partition(separator)`          | Splits the string into a tuple of three elements: the part before the separator, the separator itself, and the part after. |
| `str.replace(old, new, count=-1)`   | Returns a copy of the string with occurrences of `old` replaced by `new`, up to `count` occurrences.|
| `str.rfind(substring, start=0, end=-1)` | Returns the highest index where `substring` is found in the string, or -1 if not found.          |
| `str.rindex(substring, start=0, end=-1)` | Like `rfind()`, but raises a `ValueError` if `substring` is not found.                           |
| `str.rjust(width, fillchar=' ')`    | Right-aligns the string in a field of width `width` and pads it with `fillchar` (default is a space).|
| `str.rstrip(chars=None)`            | Returns a copy of the string with trailing whitespace (or specified `chars`) removed.              |
| `str.split(separator=None, maxsplit=-1)` | Splits the string into a list of substrings, using `separator` as the delimiter.                |
| `str.splitlines(keepends=False)`    | Splits the string at line breaks into a list of lines. If `keepends` is `True`, the line breaks are included. |
| `str.startswith(prefix, start=0, end=-1)` | Checks if the string starts with `prefix` within the specified range (`start` to `end`).         |
| `str.strip(chars=None)`             | Returns a copy of the string with leading and trailing whitespace (or specified `chars`) removed. |
| `str.swapcase()`                    | Returns a copy of the string with uppercase characters converted to lowercase and vice versa.     |
| `str.title()`                       | Returns a copy of the string with the first character of each word capitalized.                   |
| `str.upper()`                       | Returns a copy of the string with all characters converted to uppercase.                         |
| `str.zfill(width)`                  | Pads the string on the left with zeros to make it a given `width`.                                 |
| `str.__contains__(substring)`       | Checks if the string contains `substring` (used in `substring in str`).                           |
| `str.__eq__(other)`                 | Checks if two strings are equal (used in `str1 == str2`).                                          |
| `str.__ne__(other)`                 | Checks if two strings are not equal (used in `str1 != str2`).                                     |
| `str.__lt__(other)`                 | Compares if the string is less than another string (used in `str1 < str2`).                       |
| `str.__le__(other)`                 | Compares if the string is less than or equal to another string (used in `str1 <= str2`).           |
| `str.__gt__(other)`                 | Compares if the string is greater than another string (used in `str1 > str2`).                    |
| `str.__ge__(other)`                 | Compares if the string is greater than or equal to another string (used in `str1 >= str2`).        |

---
# String Format Conversion Characters

| Conversion Character | Description                                                                                       |
|----------------------|---------------------------------------------------------------------------------------------------|
| `%s`                 | String (uses `str()` or `repr()` depending on context).                                            |
| `%r`                 | String (uses `repr()` to get a detailed string representation of the object).                      |
| `%d`                 | Integer (decimal).                                                                                 |
| `%i`                 | Integer (decimal), same as `%d`.                                                                   |
| `%o`                 | Integer (octal).                                                                                  |
| `%x`                 | Integer (hexadecimal, lowercase letters a-f).                                                      |
| `%X`                 | Integer (hexadecimal, uppercase letters A-F).                                                      |
| `%f`                 | Floating point number (decimal notation).                                                          |
| `%F`                 | Floating point number (decimal notation), same as `%f`.                                            |
| `%e`                 | Floating point number (scientific notation, lowercase e).                                          |
| `%E`                 | Floating point number (scientific notation, uppercase E).                                          |
| `%g`                 | Floating point number (uses either `%f` or `%e` depending on the value and precision).            |
| `%G`                 | Floating point number (uses either `%F` or `%E` depending on the value and precision).            |
| `%c`                 | Character (converts the integer to the corresponding Unicode character).                           |
| `%u`                 | Unsigned integer (non-negative integer).                                                           |
| `%p`                 | Pointer (representation of a pointer, usually in hexadecimal format).                              |
| `%%`                 | Literal percent sign (`%`) without conversion.                                                      |
| `%a`                 | Floating point number (hexadecimal representation, with exponent, uses lowercase `p`).            |
| `%A`                 | Floating point number (hexadecimal representation, with exponent, uses uppercase `P`).            |
| `%n`                 | Number of characters written so far (used with specific format strings, not commonly used).        |
| `%b`                 | Boolean (converts `True` to `1` and `False` to `0`).                                                |

---
# Python String Formatting Modifiers

| Modifier         | Example        | Description                                                                                      |
|------------------|----------------|--------------------------------------------------------------------------------------------------|
| `number`         | `%20d`         | Put the value in a field width of 20 (right-justified by default).                               |
| `+`              | `%+20d`        | Include a sign (+ or -) for both positive and negative numbers.                                   |
| `0`              | `%020d`        | Put the value in a field 20 characters wide, fill in with leading zeros.                         |
| `.`              | `%20.2f`       | Put the value in a field 20 characters wide, with 2 characters to the right of the decimal point. |
| `-`              | `%-20d`        | Put the value in a field 20 characters wide, left-justified.                                     |
| `(name)`         | `%(name)d`      | Get the value from the supplied dictionary using `name` as the key.                              |
| `,`              | `%,.2f`        | Format the number with commas separating thousands, and 2 decimal places.                       |
| `#`              | `#x`           | Use alternative form for hexadecimal (`0x` prefix) and octal (`0o` prefix).                     |
| `width.precision`| `%10.3f`       | Set the width of the field to 10 and precision (decimal places) to 3.                            |
| `*`              | `'%*s' % 20`    | The width is specified dynamically using an argument (for example, width 20).                    |
| `%%`             | `%%`            | Literal percent sign `%`. This is used when you want to display a percent sign in the output.    |
---

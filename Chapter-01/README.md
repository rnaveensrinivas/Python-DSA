### What is Computer Science?

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

### What Is Programming?
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

### Why Study Data Structures and Abstract Data Types? 

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

### Why Study Algorithms? 

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

### Review of Basic Python

- **Python Overview:**
  - Modern, easy-to-learn, object-oriented programming language.
  - Features powerful built-in data types and intuitive control constructs.

- **Interactive Interpreter:**
  - Python is interpreted, making it easy to test and review code interactively.
  - The interpreter uses the `>>>` prompt to input and evaluate constructs, e.g., `print("Hello")`.

#### Getting Started with Data: 

- **Object-Oriented Paradigm:**
  - Python emphasizes data as the central element in problem-solving.
  - Classes define the **state** (attributes) and **behavior** (methods) of data.

- **Classes and Objects:**
  - Classes are like abstract data types; they encapsulate details visible only as state and behavior.
  - **Objects** are instances of classes, representing specific data items.

### Atomic Data Types in Python

- **Numeric Types:**
  - Python has `int` (integer) and `float` (floating-point) classes.
  - Arithmetic operations include `+`, `-`, `*`, `/`, `**` (exponentiation), `%` (modulo), and `//` (integer division).
  - Integer division returns the integer portion of the quotient.

- **Boolean Type:**
  - The `bool` class represents truth values: `True` and `False`.
  - Boolean operators: `and`, `or`, `not`.
  - Used in comparisons (e.g., `==`, `>`) and combined for complex logical expressions.

- **Identifiers and Variables:**
  - Identifiers are names for variables and must start with a letter or underscore, are case-sensitive, and can be any length.
  - Variables are created when assigned a value and hold a reference to data.
  - Python variables are dynamic, meaning their data type can change based on the assigned value.

| Operation Name               | Operator | Explanation                                         |
|------------------------------|----------|-----------------------------------------------------|
| less than                    | <        | Less than operator                                  |
| greater than                 | >        | Greater than operator                               |
| less than or equal           | <=       | Less than or equal to operator                      |
| greater than or equal        | >=       | Greater than or equal to operator                   |
| equal                        | ==       | Equality operator                                   |
| not equal                    | !=       | Not equal operator                                  |
| logical and                  | and      | Both operands True for result to be True            |
| logical or                   | or       | Either operand True for result to be True           |
| logical not                  | not      | Negates the truth value: False becomes True, True becomes False |

Table: Relational and Logical Operators

**Built-in Collection Data Types in Python:**

- **Lists, Strings, and Tuples**: Ordered collections with similar structure but key differences.
- **Sets and Dictionaries**: Unordered collections.

| Operation Name    | Operator | Explanation                                          |
|-------------------|----------|------------------------------------------------------|
| indexing          | [ ]      | Access an element of a sequence                      |
| concatenation     | +        | Combine sequences together                           |
| repetition        | *        | Concatenate a repeated number of times               |
| membership        | in       | Ask whether an item is in a sequence                 |
| length            | len      | Ask the number of items in the sequence              |
| slicing           | [ : ]    | Extract a part of a sequence                         |

Table: Operations on Any Sequence in Python

#### Lists

- **Lists in Python:**
  - A list is an ordered collection of references to Python data objects.
  - Lists are **heterogeneous**: they can contain elements of different types (e.g., integers, booleans, and floats).
  - Lists are written with **square brackets** and elements are separated by commas.
  - Example: `my_list = [1, 3, True, 6.5]`
  - Initializing empty list, `my_list = []`

- **Common List Operations:**
  - Lists support all the sequence operation, including modification using indexing and slicing. 

    | **Operation Name** | **Operator** | **Explanation**                                      | **Time Complexity**   |
    |--------------------|--------------|------------------------------------------------------|-----------------------|
    | indexing           | [ ]          | Access an element of a sequence                      | O(1)                  |
    | concatenation      | +            | Combine sequences together                           | O(k) where k is the length of the other sequence |
    | repetition         | *            | Concatenate a repeated number of times               | O(n) where n is the number of repetitions |
    | membership         | in           | Ask whether an item is in a sequence                 | O(n)                  |
    | length             | len          | Ask the number of items in the sequence              | O(1)                  |
    | slicing            | [ : ]        | Extract a part of a sequence                         | O(k) where k is the length of the slice |

    Table: list sequence operators and their time complexities

- **Indexing and Slicing:**
  - Lists are **sequentially ordered**, with indices starting from 0.
  - The slice operation, `my_list[1:3]`, returns items starting from index 1 up to but not including index 3.
  
- **Repetition:**
  - Lists can be initialized using repetition: `my_list = [0] * 6` results in `[0, 0, 0, 0, 0, 0]`.
  - The **repetition operator** creates copies of references, not actual data objects.
  
- **Repetition Caveat:**
  - When using repetition (e.g., `A = [my_list] * 3`), Python creates **references** to the same list, not copies of the data.
  - Modifying one reference affects all others.

- **Important List Methods:**
  - Lists in Python offer many built-in methods for manipulating data.
  - Methods include:
    Table: List Methods with Algorithmic Complexity

    | **Method Name** | **Use**                                                      | **Time Complexity**    |
    |-----------------|--------------------------------------------------------------|------------------------|
    | `append(item)`  | Adds an item to the end of the list.                         | O(1)                   |
    | `insert(i, item)`| Inserts an item at the ith position.                        | O(n)                   |
    | `pop()`          | Removes and returns the last item in the list.               | O(1)                   |
    | `pop(i)`         | Removes and returns the ith item in the list.                | O(n)                   |
    | `sort()`         | Sorts the list.                                              | O(n log n)             |
    | `reverse()`      | Reverses the list.                                           | O(n)                   |
    | `del`            | Deletes the item at the ith position.                        | O(n)                   |
    | `index(item)`    | Returns the index of the first occurrence of item.           | O(n)                   |
    | `count(item)`    | Returns the number of occurrences of item.                   | O(n)                   |
    | `remove(item)`   | Removes the first occurrence of item.                        | O(n)                   |

- **Range Function:**
  - The `range` function generates a sequence of numbers, which can be converted into a list using `list(range(...))`.
  - Example:
    - `list(range(10))` results in `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
    - `list(range(5, 10))` results in `[5, 6, 7, 8, 9]`
    - `list(range(5, 10, 2))` results in `[5, 7, 9]`
  
### Bullet Point Summary

- **Strings in Python**: Strings are ordered collections of characters, which can include letters, numbers, and symbols. They are enclosed in either single (`'`) or double (`"`) quotation marks.
- **String Examples**:
  - `"David"` is a string literal.
  - Strings are indexed, and their elements can be accessed using square brackets: `my_name[3]` returns `'i'` for `"David"`.
  - Strings can be repeated using the `*` operator: `"David" * 2` results in `'DavidDavid'`.
  - The length of a string can be found using `len()`: `len(my_name)` gives `5` for `"David"`.

- **String Operations**: Since strings are sequences, they support sequence operations like indexing, slicing, and concatenation.

| Operation Name    | Operator | Explanation                                          | Time Complexity |
|-------------------|----------|------------------------------------------------------|-----------------|
| indexing          | [ ]      | Access an element of a sequence                      | O(1)            |
| concatenation     | +        | Combine sequences together                           | O(n)            |
| repetition        | *        | Concatenate a repeated number of times               | O(n)            |
| membership        | in       | Ask whether an item is in a sequence                 | O(n)            |
| length            | len      | Ask the number of items in the sequence              | O(1)            |
| slicing           | [ : ]    | Extract a part of a sequence                         | O(k)            |

### Table: Methods Provided by Strings in Python

| Method Name    | Use                                         | Example                     | Time Complexity  |
|----------------|---------------------------------------------|-----------------------------|------------------|
| `center(w)`    | Returns a string centered in a field of size `w` | `'David'.center(10)`         | O(n)             |
| `count(item)`  | Returns the number of occurrences of `item` in the string | `'David'.count('i')`         | O(n)             |
| `ljust(w)`     | Returns a string left-justified in a field of size `w` | `'David'.ljust(10)`          | O(n)             |
| `lower()`      | Returns a string in all lowercase           | `'David'.lower()`            | O(n)             |
| `rjust(w)`     | Returns a string right-justified in a field of size `w` | `'David'.rjust(10)`          | O(n)             |
| `find(item)`   | Returns the index of the first occurrence of `item` | `'David'.find('v')`          | O(n)             |
| `split(s_char)`| Splits a string into substrings at `s_char` returns a list of strings | `'David'.split('v')`         | O(n)             |

### Key Differences between Lists and Strings
- **Mutability**:
  - **Lists**: Mutable; items can be changed by indexing and assignment.
    - Example: 
      ```python
      my_list = [1, 3, True, 6.5]
      my_list[0] = 2**10
      print(my_list)  # [1024, 3, True, 6.5]
      ```
  - **Strings**: Immutable; items cannot be changed after creation.
    - Example:
      ```python
      my_name = "David"
      my_name[0] = 'X'  # TypeError: 'str' object does not support item assignment
      ```

- **Tuples** are heterogeneous sequences, similar to lists.
- They are **immutable**, meaning their content cannot be changed after creation (unlike lists).
- Tuples are written as comma-delimited values enclosed in **parentheses** `( )`.
- Example:
  - `my_tuple = (2, True, 4.96)`
  - `len(my_tuple)` returns the number of elements: 3.
  - `my_tuple[0]` accesses the first element: 2.
  - `my_tuple * 3` repeats the tuple three times: `(2, True, 4.96, 2, True, 4.96, 2, True, 4.96)`.
  - `my_tuple[0:2]` slices the tuple from index 0 to 1: `(2, True)`.
- **Error** occurs if trying to modify a tuple element, as they are immutable.

### Concise Bullet Point Summary of Sets in Python:

- **Sets** are unordered collections of **immutable** data objects.
- They do not allow **duplicates** and are defined using curly braces `{}`.
- The empty set is represented as `set()`.
- Sets can store **heterogeneous** data types.
- **Operations** supported by sets:
  - Set membership (`in`), checking if an item is present in the set.
  - Cardinality (`len`), returning the number of elements in the set.
  - Set operations such as **union**, **intersection**, **difference**, and **subset**.
- Sets **do not support indexing** or **slicing** (since they are unordered).
- **Mutability**: Sets are mutable; elements can be added or removed, but the set itself is unordered.

### Table 1.5: Operations on a Set in Python

| Operator | Use                                   | Explanation                                          | Time Complexity |
|----------|---------------------------------------|------------------------------------------------------|-----------------|
| `in`     | Set membership                        | Check if an element is in the set                    | O(1)            |
| `len`    | Set cardinality                       | Returns the number of elements in the set            | O(1)            |
| `|`      | Union                                  | Returns a new set with all elements from both sets   | O(len(set1) + len(set2)) |
| `&`      | Intersection                           | Returns a new set with only common elements from both sets | O(min(len(set1), len(set2))) |
| `-`      | Difference                             | Returns a new set with elements in the first set but not in the second | O(len(set1)) |
| `<=`     | Subset                                 | Checks if all elements of the first set are in the second set | O(len(set1)) |

### Table 1.6: Methods Provided by Sets in Python

| Method Name   | Use                          | Explanation                                                                 | Time Complexity |
|---------------|------------------------------|-----------------------------------------------------------------------------|-----------------|
| `union`       | `set1.union(set2)`            | Returns a new set with all elements from both sets                           | O(len(set1) + len(set2)) |
| `intersection`| `set1.intersection(set2)`     | Returns a new set with elements common to both sets                          | O(min(len(set1), len(set2))) |
| `difference`  | `set1.difference(set2)`       | Returns a new set with items from the first set not in the second            | O(len(set1)) |
| `issubset`    | `set1.issubset(set2)`         | Checks if all elements of `set1` are in `set2`                               | O(len(set1)) |
| `add`         | `set.add(item)`               | Adds an item to the set                                                     | O(1)            |
| `remove`      | `set.remove(item)`            | Removes an item from the set                                                 | O(1)            |
| `pop`         | `set.pop()`                   | Removes an arbitrary element from the set                                     | O(1)            |
| `clear`       | `set.clear()`                 | Removes all elements from the set                                            | O(len(set))     |


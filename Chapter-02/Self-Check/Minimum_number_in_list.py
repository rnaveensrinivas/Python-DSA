import time
import random

def find_min_1(arr: list[int]) -> int:
    min_element = None
    for i in range(len(arr)):
        isMin = True
        for j in range(len(arr)):
            if i == j:
                continue
            if arr[i] > arr[j]:
                isMin = False
                break
        
        if isMin:
            min_element = arr[i] 
            # break # if commented we always take the worst case complexity
    return min_element

def find_min_2(arr: list[int]) -> int:
    min_element = arr[0]
    for num in arr:
        min_element = min(min_element, num)
    return min_element

SIZE = 10_000_000
RANDOM_RANGE = (-100_000_000_000, 100_000_000_000)
# Creating a random array
# Method 1
arr = [random.randint(*RANDOM_RANGE) for _ in range(SIZE)]
# Method 2 - shuffle takes more time
# arr = list(range(SIZE))
# random.shuffle(arr)

start = time.time()
min_element = find_min_1(arr)
stop = time.time()
time_taken = stop - start
print(f"Minimum element found using O(n^2): {min_element}")
print(f"Time taken for finding min element using O(n^2): %1.15fsecs."%time_taken)
print()

start = time.time()
min_element = find_min_2(arr)
stop = time.time()
time_taken = stop - start
print(f"Minimum element found using O(n): {min_element}")
print(f"Time taken for finding min element using O(n): %1.15fsecs."%time_taken)

# OUTPUT
# Minimum element found using O(n^2): -99999980463
# Time taken for finding min element using O(n^2): 17.940702199935913secs.

# Minimum element found using O(n): -99999980463
# Time taken for finding min element using O(n): 3.582488298416138secs.

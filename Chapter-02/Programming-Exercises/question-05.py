# Previous Question-4
# Given a list of numbers in random order write a linear time algorithm to 
# find the kth smallest number in the list. 
# Explain why your algorithm is linear.
# Present Question-5
# Can you improve the algorithm from the previous problem to be O(nlog(n))?
import random

# Background
SIZE = 1_000_000
RANDOM_RANGE = (-100_000_000_000, 100_000_000_000)
# Creating a random array
# Method 1
arr = [random.randint(*RANDOM_RANGE) for _ in range(SIZE)]
k = random.randrange(SIZE)

# Action
arr.sort()
print(f"k = {k} and kth smallest element: {arr[k]}")